# AI Voice Assistant (Python)

A simple Python voice assistant that greets you by name, listens for voice commands, and responds with a **natural, human-like voice** (not robotic text-to-speech) using Microsoft's neural TTS engine.

---

## Features

- Greets you on startup: *"Hi Meghana"* + time-based greeting (Good morning/afternoon/evening)
- Listens to voice commands via microphone
- Opens applications on command (Notepad, Calculator, Paint)
- Tells the current time
- Responds out loud using a natural neural voice (via `edge-tts`)
- Exits gracefully on command ("exit", "stop", "quit")

---

## Files

| File | Description |
|---|---|
| `voice_assistant.py` | Basic version using `pyttsx3` (offline, robotic voice) |
| `voice_assistant_natural.py` | Natural voice version using `edge-tts` + `playsound` |
| `voice_assistant_pygame.py` | **Recommended** — natural voice using `edge-tts` + `pygame` (more reliable playback on Windows) |

---

## Requirements

- Python 3.8 or higher
- Internet connection (required for `edge-tts` to generate voice audio and for Google Speech Recognition)
- A working microphone

---

## Installation

Open PowerShell/Terminal in the project folder and run:

```bash
pip install edge-tts SpeechRecognition pyaudio pygame
```

### If `pyaudio` fails to install

This is the most common install issue on Windows. Try these in order:

```bash
# 1. Upgrade pip, setuptools, and wheel first
python -m pip install --upgrade pip setuptools wheel

# 2. Retry
pip install pyaudio
```

If it still fails, download a prebuilt wheel matching your Python version (e.g. `cp311` for Python 3.11) and architecture (`win_amd64` for 64-bit Windows) from a trusted wheel source, then install it directly:

```bash
pip install path\to\PyAudio‑<version>‑cp311‑cp311‑win_amd64.whl
```

Alternatively, if you have Anaconda/Miniconda installed:

```bash
conda install pyaudio
```

---

## Running the Assistant

```bash
py voice_assistant_pygame.py
```

(Use `python` instead of `py` if `py` isn't recognized on your system.)

---

## Usage

1. Run the script — it will speak a greeting and start listening.
2. Speak a command clearly into your microphone, e.g.:
   - **"open notepad"**
   - **"open calculator"**
   - **"open paint"**
   - **"what's the time"**
   - **"exit"** / **"stop"** / **"quit"** — to close the assistant

---

## Customizing the Voice

Open the script and change the `VOICE` variable near the top to any of these:

| Voice | Description |
|---|---|
| `en-IN-NeerjaNeural` | Indian English, female (default) |
| `en-IN-PrabhatNeural` | Indian English, male |
| `en-US-JennyNeural` | US English, warm female |
| `en-US-AriaNeural` | US English, expressive female |
| `en-GB-SoniaNeural` | British English, female |

To see the full list of available voices, run this in Python:

```python
import asyncio, edge_tts

async def list_voices():
    voices = await edge_tts.list_voices()
    for v in voices:
        print(v["ShortName"])

asyncio.run(list_voices())
```

---

## Troubleshooting

| Problem | Likely Cause | Fix |
|---|---|---|
| `ModuleNotFoundError` | Package not installed | Run the `pip install` command above |
| No sound plays, no error shown | `playsound` failing silently | Use `voice_assistant_pygame.py` instead |
| `[VOICE ERROR]` printed in terminal | Audio playback issue | Read the printed error message for the exact cause |
| `ModuleNotFoundError: No module named 'pyaudio'` and pip fails to build it | Missing prebuilt binary | See "If pyaudio fails to install" above |
| `command not recognized` when running `voice_assistant.py` directly | PowerShell doesn't run scripts from current folder by default | Use `python voice_assistant.py` or `py voice_assistant.py` instead of running the filename alone |
| Assistant doesn't respond to speech | Mic not detected / too quiet / no internet | Check mic permissions in Windows Settings, and confirm you have an internet connection (needed for Google Speech Recognition) |

---

## Notes

- `edge-tts` requires an internet connection since it streams audio generation from Microsoft's servers — it is **not** a fully offline solution.
- For a fully offline voice, `pyttsx3` (see `voice_assistant.py`) works without internet but sounds noticeably more robotic.
- Speech recognition (`SpeechRecognition` + Google Web Speech API) also requires internet.

---

## Possible Extensions

- Add more voice commands (open browser, search Google, tell jokes, weather, etc.)
- Wake-word detection (e.g. "Hey Assistant") instead of listening continuously
- GUI interface instead of terminal-only
- Offline speech recognition (e.g. using `Vosk`) for full offline capability
