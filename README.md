<h1 align="center">🎙️ <strong>LocalVoiceAI</strong></h1>

<p align="center">

  <!-- Dark-Mode Compatible Badges -->
  <img alt="Python 3.11" src="https://img.shields.io/badge/Python-3.11-3776AB.svg?style=for-the-badge&logo=python&logoColor=white&labelColor=2f3135">
  <img alt="Platform" src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-6b7073.svg?style=for-the-badge&labelColor=2f3135">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-2bbc8a.svg?style=for-the-badge&logo=github&logoColor=white&labelColor=2f3135">
  <img alt="Status" src="https://img.shields.io/badge/Status-Operational-1db954.svg?style=for-the-badge&labelColor=2f3135">

  <!-- GitHub Dynamic Badges (REPLACE YourUsername) -->
  <img alt="Release" src="https://img.shields.io/github/v/release/YourUsername/LocalVoiceAI?style=for-the-badge&logo=github&logoColor=white&labelColor=2f3135">
  <img alt="Last Commit" src="https://img.shields.io/github/last-commit/YourUsername/LocalVoiceAI?style=for-the-badge&logo=github&logoColor=white&labelColor=2f3135">
  <a href="https://github.com/YourUsername/LocalVoiceAI/archive/refs/heads/main.zip"><img alt="Download" src="https://img.shields.io/badge/Download-Zip-orange.svg?style=for-the-badge&labelColor=2f3135"></a>

</p>

<p align="center">
  <img src="ecb00225-dd12-4309-ab65-26659f726120.png.png" alt="Operational Terminal" width="650">
</p>

<blockquote>
<p><b>A privacy-centric, fully autonomous voice assistant architecture featuring Speech-to-Text, Local LLM integration via Gemma3 1B, and Text-to-Speech synthesis.</b></p>
</blockquote>

<hr>

<h2>📜 Description</h2>

<blockquote>
<p><b>LocalVoiceAI</b> implements a privacy-centric, fully autonomous voice assistant architecture.</p>
<p>The system is designed for <code>Central Processing Unit (CPU)</code> execution, enabling deployment on local hardware without reliance on cloud-based services.</p>
<p>The pipeline performs the following functions:</p>
<ul>
<li><code>Acoustic Input Processing</code>: Utilization of Vosk for offline Speech-to-Text (STT).</li>
<li><code>Cognitive Processing</code>: Integration of a local LLM via Ollama (Gemma3:1b).</li>
<li><code>Acoustic Output Synthesis</code>: Employment of Chatterbox TTS for localized voice synthesis.</li>
<li><code>Data Lifecycle Management</code>: Automated deletion of temporary audio artifacts.</li>
</ul>
</blockquote>

<hr>

<h2>✨ Key Features</h2>

<blockquote>
<ul>
<li><img src="https://img.shields.io/badge/Feature-Offline_Speech_Recognition-blue.svg"> High-fidelity transcription of Indian English and Hindi dialects utilizing the Vosk toolkit.</li>

<li><img src="https://img.shields.io/badge/Feature-Local_LLM_Hosting-blue.svg"> Deployment via Ollama (gemma3:1b), ensuring zero network latency and data transmission during runtime.</li>

<li><img src="https://img.shields.io/badge/Feature-Offline_Speech_Synthesis-blue.svg"> Generation of naturalistic speech patterns via the Chatterbox library.</li>

<li><img src="https://img.shields.io/badge/Feature-Privacy_Assurance-blue.svg"> The architecture ensures that no audio data or textual transcripts are transmitted to external servers.</li>

<li><img src="https://img.shields.io/badge/Feature-Cross_Platform-blue.svg"> Verified functionality on Windows, Linux, and macOS.</li>

<li><img src="https://img.shields.io/badge/Feature-Bilingual_Capabilities-blue.svg"> Native support for bilingual conversational exchanges in English and Hindi.</li>
</ul>
</blockquote>

<hr>

<h2>🛠️ Technology Stack</h2>

<blockquote>
<p>
<code>Core Language</code> : Python 3.11 (Strict Requirement)
<br><br>
<code>Computer Vision/Audio</code> : Vosk, SoundDevice
<br><br>
<code>Machine Learning</code> : Ollama (Gemma3:1b)
<br><br>
<code>Speech Synthesis</code> : Chatterbox TTS
<br><br>
<code>Build Tools</code> : Cython, Wheel, Setuptools
</p>
</blockquote>

<hr>

<h2>🖥️ System Requirements</h2>

<blockquote>
<p><b>Note:</b> This architecture utilizes a <code>CPU-First Design</code>, optimized for execution on standard laptop processors.</p>

<table width="100%">
<thead>
<tr>
<th>Component</th>
<th>Minimum Specification</th>
<th>Recommended Specification</th>
</tr>
</thead>
<tbody>
<tr>
<td><b>CPU</b></td>
<td>4 Cores (e.g., Intel i5 / Ryzen 5)</td>
<td>6-8 Cores (e.g., Intel i7 / Ryzen 7)</td>
</tr>
<tr>
<td><b>RAM</b></td>
<td>8 GB</td>
<td>16 GB+</td>
</tr>
<tr>
<td><b>Storage</b></td>
<td>20 GB SSD</td>
<td>500 GB SSD</td>
</tr>
<tr>
<td><b>GPU</b></td>
<td>Integrated Graphics</td>
<td>Optional (NVIDIA 6GB+ VRAM)</td>
</tr>
</tbody>
</table>
</blockquote>

<hr>

<h2>⚙️ Installation</h2>

<blockquote>

<h3>Prerequisites</h3>
<ul>
<li><code>Python 3.11</code></li>
<li><code>Ollama</code> (Installed and active)</li>
<li><code>Microsoft Visual C++ Build Tools</code> (Windows)</li>
</ul>

<h3>Steps</h3>

<p><b>1. Clone the repository:</b></p>

<pre><code>
git clone https://github.com/YourUsername/LocalVoiceAI.git
cd LocalVoiceAI
</code></pre>

<p><b>2. Environment Initialization:</b></p>

<pre><code>
Windows:
py -3.11 -m venv .venv
.venv\Scripts\activate

Linux/macOS:
python3.11 -m venv .venv
source .venv/bin/activate
</code></pre>

<p><b>3. ⚠️ Critical Installation Sequence:</b></p>

<pre><code>
pip install --upgrade pip setuptools wheel
pip install "numpy<1.26"
pip install cython
pip install --no-build-isolation "pkuseg==0.0.25"
pip install -r requirements.txt
</code></pre>

<p><b>4. Model Acquisition:</b></p>

<pre><code>
ollama pull gemma3:1b
</code></pre>

<ul>
<li>Download from: https://alphacephei.com/vosk/models</li>
<li>Extract into: <code>models/</code></li>
</ul>

</blockquote>

<hr>

<h2>🚀 Usage</h2>

<blockquote>
<ol>
<li>Ensure microphone is connected.</li>
<li>Start Ollama.</li>
<li>Run the assistant:</li>

<pre><code>
python voice_chat_process.py
</code></pre>

<li>Speak to interact.</li>
</ol>
</blockquote>

<hr>

<h2>📂 Repository Structure</h2>

<blockquote>
<pre><code>
LocalVoiceAI/
├── assets/
├── models/
│   ├── vosk-model-small-en-in-0.4/
│   └── vosk-model-small-hi-0.22/
├── .gitignore
├── requirements.txt
├── README.md
└── voice_chat_process.py
</code></pre>
</blockquote>

<hr>

<h2>📄 License</h2>

<blockquote>
<p>This project is distributed under the <img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat-square" alt="MIT License">.</p>
</blockquote>

<hr>

<h2>📧 Contact</h2>

<blockquote>
<p>Project Link: https://github.com/YourUsername/LocalVoiceAI</p>
</blockquote>
