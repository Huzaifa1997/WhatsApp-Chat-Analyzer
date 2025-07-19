# 📊 WhatsApp Chat Analyzer

Analyze your WhatsApp conversations like never before!  
This project lets you **visually explore** your WhatsApp chat exports to uncover hidden patterns, relationships, and activity insights in a clean, modern dashboard.

---

## 🔍 Features

- 📅 **Daily, Monthly, and Yearly** message activity tracking  
- 👥 **User-based** message contribution analysis (for group chats)  
- 💬 **Word frequency** and most common **emojis**  
- 🕰️ **Peak messaging hours** (Hourly Activity Map)  
- ☁️ **WordCloud** of most used words  
- 📈 Interactive **charts** and **data breakdown**

---

## 🧠 Built With

- 🐍 **Python** – Core backend logic and data processing  
- 🧠 **Streamlit** – For building the interactive UI  
- 📊 **Pandas** – For efficient data wrangling  
- 📉 **Matplotlib** & **Seaborn** – Data visualizations  
- 🔍 **Regex** – To parse messages from raw text  
- 🖥️ **PyCharm** – IDE used for development

---

## 🚀 How It Works

1. Export your WhatsApp chat (without media) from your phone  
2. Upload the `.txt` file into the app  
3. Get instant insights with beautiful graphs and stats

---

## 🌐 Live Demo

https://whatsapp-chat-analyzer-huzi.streamlit.app/

---

## 📂 File Structure

```bash
.
├── app.py                # Main Streamlit app script
├── helper.py             # Logic for message counting, plotting, etc.
├── preprocessor.py       # Preprocesses raw chat text
├── stop_hinglish.txt     # Stop words used for word cloud cleaning
├── requirements.txt      # Python dependencies
├── Whatsapp Analyzer.ipynb  # Optional notebook version (if needed)
└── .gitignore
