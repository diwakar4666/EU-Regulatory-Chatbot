# ⚖️ EU Regulatory Chatbot (GDPR | EU AI Act | DORA)

## 📌 Overview

This project is a **production-style AI chatbot** built using Streamlit and Ollama.

It provides domain-restricted answers strictly for:

* GDPR (General Data Protection Regulation)
* EU AI Act (Artificial Intelligence Act)
* DORA (Digital Operational Resilience Act)

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

## 🧠 Design Choices

* Local LLM → Privacy + zero cost
* Guardrails → Prevent hallucination
* Streaming → Better UX

---

## 🔮 Future Improvements

* RAG with official EU legal documents
* FastAPI backend
* Feedback analytics dashboard

---

## ⚠️ Limitations

* Depends on LLM knowledge (no real legal validation)
* Basic keyword-based guardrail

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

This project demonstrates a **controlled AI chatbot with guardrails**.

It is a strong foundation for building a **RegTech AI system**.
