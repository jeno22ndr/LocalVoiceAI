#!/usr/bin/env python3
import os
import queue
import sys
import json
import sounddevice as sd
import vosk
import torch
import torchaudio as ta
import requests
import time

from chatterbox.tts import ChatterboxTTS

# --- Configuration ---
MODEL_EN_PATH = r"C:\Users\jeno22ndr\Downloads\vosk-model-small-en-in-0.4\vosk-model-small-en-in-0.4"
MODEL_HI_PATH = r"C:\Users\jeno22ndr\Downloads\vosk-model-small-hi-0.22\vosk-model-small-hi-0.22"

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:1b"

OUTPUT_WAV = "agent_reply.wav"
# -----------------------

# Check model paths
if not os.path.exists(MODEL_EN_PATH):
    print(f"Error: English model path not found: '{MODEL_EN_PATH}'"); sys.exit(1)
if not os.path.exists(MODEL_HI_PATH):
    print(f"Error: Hindi model path not found: '{MODEL_HI_PATH}'"); sys.exit(1)

# STT setup
q = queue.Queue()
def audio_callback(indata, frames, time_info, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

device_info = sd.query_devices(None, 'input')
samplerate = int(device_info['default_samplerate'])

model_en = vosk.Model(MODEL_EN_PATH)
model_hi = vosk.Model(MODEL_HI_PATH)
rec_en = vosk.KaldiRecognizer(model_en, samplerate)
rec_hi = vosk.KaldiRecognizer(model_hi, samplerate)

print("Loaded STT models.")

# TTS setup
device = "cuda" if torch.cuda.is_available() else "cpu"
tts_model = ChatterboxTTS.from_pretrained(device=device)
print(f"Using TTS device: {device}")

# Function to call LLM via Ollama
def call_llm(prompt_text):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt_text,
        "stream": False
    }
    headers = {"Content-Type": "application/json"}
    resp = requests.post(OLLAMA_API_URL, headers=headers, data=json.dumps(payload))
    if resp.status_code != 200:
        raise Exception(f"LLM API error {resp.status_code}: {resp.text}")
    resp_json = resp.json()
    result = resp_json.get("response")
    if result is None:
        raise Exception(f"No response field in LLM result: {resp_json}")
    return result

# At start, ask user language
print("Which language would you prefer for this conversation? Say ‘English’ or ‘Hindi’.")
lang = None

with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=None,
                       dtype='int16', channels=1, callback=audio_callback):
    try:
        # Wait to detect language choice
        while lang is None:
            data = q.get()
            if rec_en.AcceptWaveform(data):
                res = json.loads(rec_en.Result())
                txt = res.get("text","").strip().lower()
                if "english" in txt:
                    lang = "en"
                elif "hindi" in txt:
                    lang = "hi"
            # else ignore
        print(f"Language set to: {'English' if lang=='en' else 'Hindi'}")

        history = []

        print("Ready. Speak now. Press Ctrl+C to exit.")

        while True:
            data = q.get()
            user_text = None
            # Use only the selected language recognizer
            if lang == "en" and rec_en.AcceptWaveform(data):
                res = json.loads(rec_en.Result())
                txt = res.get("text","").strip()
                if txt:
                    user_text = txt
            elif lang == "hi" and rec_hi.AcceptWaveform(data):
                res2 = json.loads(rec_hi.Result())
                txt2 = res2.get("text","").strip()
                if txt2:
                    user_text = txt2
            else:
                continue

            if not user_text:
                continue

            print(f"You ({lang}): {user_text}")

            # Build prompt
            prompt = ""
            for turn in history[-4:]:
                prompt += f"User ({turn['lang']}): {turn['user']}\nAgent: {turn['agent']}\n"
            prompt += f"User ({lang}): {user_text}\nAgent:"

            response_text = call_llm(prompt)
            print(f"Agent: {response_text}")
            history.append({"lang": lang, "user": user_text, "agent": response_text})

            wav = tts_model.generate(response_text)
            ta.save(OUTPUT_WAV, wav, tts_model.sr)

            # Playback and wait
            if sys.platform.startswith("win"):
                os.system(f"start /wait {OUTPUT_WAV}")
            elif sys.platform.startswith("linux"):
                os.system(f"aplay {OUTPUT_WAV}")
            elif sys.platform.startswith("darwin"):
                os.system(f"afplay {OUTPUT_WAV}")
            else:
                print("Please play", OUTPUT_WAV, "manually.")

            # Delete file
            try:
                os.remove(OUTPUT_WAV)
            except OSError:
                pass

            time.sleep(0.3)  # short pause before listening again

    except KeyboardInterrupt:
        print("\nExiting…")
