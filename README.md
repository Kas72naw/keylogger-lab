

# 🛡️ Keylogger Lab – Python Key Capture Demo

This project demonstrates a basic keylogger written in Python using the `pynput` library. It is intended for **ethical hacking and cybersecurity education only**.

## 📌 What It Does

- Logs all keystrokes from the system
- Records them into `keylog.txt` with timestamps
- Runs silently in the background
- Easy to extend and modify for ethical experiments

## 🛠 Tools & Technologies

- Python 3
- pynput module
- Kali Linux (tested)
- Virtual environment (venv)

## 📂 Files in This Project

| File           | Description                          |
|----------------|--------------------------------------|
| `keylogger.py` | Main Python script for logging keys  |
| `keylog.txt`   | Sample output with key timestamps     |
| `*.png`        | Screenshots of terminal + log view   |

## ▶️ How to Run

```bash
python3 -m venv env
source env/bin/activate
pip install pynput
python keylogger.py

=======
# keylogger-lab
 A simple Python keylogger for cybersecurity learning purposes
>>>>>>> bb2fafa5b2df15b4dec4e81ced0685c6245bbba1
