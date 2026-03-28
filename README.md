# ⚖️ EU Regulatory Chatbot (GDPR | EU AI Act | DORA)

## 📌 Overview

This project is a **production-style AI chatbot** built using Streamlit and Ollama.

It provides domain-restricted answers strictly for:

* GDPR (General Data Protection Regulation)
* EU AI Act (Artificial Intelligence Act)
* DORA (Digital Operational Resilience Act)

The system enforces strict guardrails and includes a feedback loop for continuous improvement.

---

## 🚀 Features

### ✅ Chatbot UI

* Interactive chat interface
* Real-time streaming responses
* Persistent conversation history

### ✅ Guardrails

* Rejects unrelated queries
* Prevents hallucinated responses
* Enforces domain-specific answers

### ✅ Feedback Loop (NEW)

* 👍 / 👎 buttons for each response
* Stores feedback in `feedback.json`
* Enables future model improvement

### ✅ Deterministic Responses

* Temperature set to 0
* Ensures consistent outputs

### ✅ Error Handling

* Prevents crashes
* Displays meaningful errors

---

## 🏗️ Architecture

```
[Streamlit UI]
      ↓
[Ollama Local API]
      ↓
[LLaMA 3.2 Model]
      ↓
[Feedback संग्रह (JSON)]
```

---

## 📦 Requirements

```
pip install streamlit ollama
```

---

## ⚙️ Setup

### 1. Install Ollama

https://ollama.com

### 2. Pull Model

```
ollama pull llama3.2
```

### 3. Start Server

```
ollama serve
```

### 4. Run App

```
streamlit run app.py
```

---

## 💡 Usage

Ask questions like:

* "What is GDPR Article 5?"
* "Explain EU AI Act risk categories"
* "What does DORA say about ICT risk?"

---

## 🔁 Feedback System

Each response includes:

* 👍 Helpful
* 👎 Not Helpful

Feedback is stored in:

```
feedback.json
```

Example:

```
{
  "question": "...",
  "answer": "...",
  "feedback": "up"
}
```

---

## 🧠 Design Choices

* Local LLM → Privacy + zero cost
* Guardrails → Prevent hallucination
* Feedback loop → Enables RL-style improvement
* Streaming → Better UX

---

## 🔮 Future Improvements

* RAG with official EU legal documents
* FastAPI backend
* Feedback analytics dashboard
* Cloud deployment (AWS / Azure)

---

## ⚠️ Limitations

* Depends on LLM knowledge (no real legal validation)
* Basic keyword-based guardrail
* No backend persistence (JSON only)

---

## 👨‍💻 Author

Diwakar Gunasekaran
MSc Artificial Intelligence
National College of Ireland

---

## 📜 License

Academic / educational use

---

## 💬 Final Note

This project demonstrates a **controlled AI chatbot with guardrails and feedback learning**.

It is a strong foundation for building a **RegTech AI system**.
