# 🌍 TransLangAI – AI-Powered Translator Web App

**TransLangAI** is a smart, minimalistic AI-powered translation platform that allows users to translate text across multiple languages instantly. It’s built using Python and Flask, powered by modern NLP libraries such as `googletrans` or `transformers`, and styled with simple HTML/CSS for a lightweight yet impactful interface.

---

## ✨ Features

- 🔁 Real-time text translation between multiple languages
- 🧠 AI/NLP-based language detection and translation
- 🎯 Clean, responsive frontend using HTML & CSS
- 🧪 Error handling for invalid inputs and edge cases
- 💻 Runs locally in your browser via Flask server

---

## 🗂️ Project Structure

TransLangAI/
├── app.py # Flask application (backend)
├── templates/
│ └── index.html # HTML frontend
├── static/
│ └── style.css # Custom styling (optional)
├── requirements.txt # Dependencies
├── .gitignore # Ignore files/folders
└── README.md # This file!

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/senviii/TransLangAI.git
cd TransLangAI

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
http://127.0.0.1:5000
