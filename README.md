# 🤖 Chatbot Mini Project

A collection of three chatbot implementations in Python, each using a different approach — from simple rule-based to AI-powered.

---

## 📁 Project Structure

```
chatbot/
├── nltk_rule_bot.py        # Rule-based chatbot using NLTK
├── gpt2_bot.py             # AI chatbot powered by GPT-2
├── mon_chatbot/            # Conversational AI chatbot using Rasa
│   ├── config.yml
│   ├── domain.yml
│   ├── stories.yml
│   ├── actions.py
│   └── data/
│       └── nlu.yml
├── requirements.txt
├── requirements_rasa.txt
└── requirements_gpt2.txt
```

---

## 🧩 Bot 1 — Rule-Based Bot (NLTK)

A simple pattern-matching chatbot using `nltk.chat.util`. Responds to fixed phrases with predefined replies.

**Supported inputs:** `hello`, `who are you?`, `my name is ...`, `help`, `bye`

### ▶️ How to run

```bash
pip install nltk
python nltk_rule_bot.py
```

---

## 🧠 Bot 2 — GPT-2 Bot

A generative AI chatbot using Hugging Face's `transformers` library with the pretrained GPT-2 model. Takes a prompt and generates a natural language response.

### ▶️ How to run

```bash
pip install -r requirements_gpt2.txt
python gpt2_bot.py
```

> Type your message after the `>` prompt and press Enter.

---

## 🚀 Bot 3 — Rasa Chatbot (`mon_chatbot`)

A full conversational AI chatbot built with [Rasa Open Source](https://rasa.com/). Handles intents like greetings, farewells, asking how the bot is, and help requests.

**Intents:** `greet`, `goodbye`, `ask_how_are_you`, `bot_challenge`, `help`

### ▶️ How to run

**1. Install dependencies**
```bash
pip install -r requirements_rasa.txt
```

**2. Train the model**
```bash
cd mon_chatbot
rasa train
```

**3. Start the Rasa server**
```bash
rasa run --enable-api --cors "*"
```

The bot will be available at: `http://localhost:5005`

**4. Test via REST API**
```bash
curl -X POST http://localhost:5005/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d "{\"sender\": \"user\", \"message\": \"hello\"}"
```

**Or chat directly in the terminal:**
```bash
rasa shell
```

---

## 🛠️ Requirements

| Bot | Python | Key Dependencies |
|-----|--------|-----------------|
| NLTK Bot | 3.7+ | `nltk` |
| GPT-2 Bot | 3.7+ | `transformers`, `torch` |
| Rasa Bot | 3.8+ | `rasa` |

---

## 👤 Author

**FatihAmine** — [github.com/FatihAmine](https://github.com/FatihAmine)
