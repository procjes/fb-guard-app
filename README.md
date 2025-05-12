# fb-guard-app# Facebook Guard Android App

A Python-based Facebook Profile Guard tool packaged as an Android APK using Kivy & Buildozer.

## Files

- `guard.py` — core logic module  
- `main.py` — Kivy app launcher  
- `requirements.txt` — Python dependencies  
- `buildozer.spec` — Buildozer configuration  

## Build Steps

1. **Install system dependencies**  
   ```bash
   sudo apt update
   sudo apt install -y python3-pip python3-setuptools git \
       libffi-dev libssl-dev openjdk-11-jdk unzip
   pip3 install --upgrade cython==0.29.19 buildozer
   
