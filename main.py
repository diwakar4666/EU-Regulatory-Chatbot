import streamlit as st
import ollama
import json
from datetime import datetime

# -------------------- CONFIG --------------------
st.set_page_config(
    page_title="EU Regulatory Expert",
    page_icon="⚖️",
    layout="wide"
)

SYSTEM_PROMPT = """
You are a highly specialized EU Regulatory Expert.
Your knowledge is STRICTLY limited to:
1. GDPR (General Data Protection Regulation)
2. EU AI Act (Artificial Intelligence Act)
3. DORA (Digital Operational Resilience Act)

RULES:
- ONLY answer questions related to these three regulations.
- If a question is unrelated, respond exactly with:
  "I am only authorized to discuss GDPR, EU AI Act, and DORA."
- Always cite the specific Article or Recital.
- If unsure, say you don’t know. Do NOT hallucinate.
- Be concise and professional.
"""

# -------------------- STATE --------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------- FEEDBACK STORAGE --------------------
def save_feedback(question, answer, feedback):
    data = {
        "timestamp": str(datetime.now()),
        "question": question,
        "answer": answer,
        "feedback": feedback
    }

    try:
        with open("feedback.json", "a") as f:
            f.write(json.dumps(data) + "\n")
    except Exception as e:
        st.error(f"Feedback save failed: {e}")

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.title("⚙️ Control Panel")

    model = st.selectbox(
        "Model",
        ["llama3.2"],
        index=0
    )

    if st.button("🧹 Reset Conversation"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.caption("Strict Regulatory Mode Enabled")

# -------------------- HEADER --------------------
st.title("⚖️ EU Regulatory Chatbot")
st.markdown("**GDPR | EU AI Act | DORA — Production Mode**")

# -------------------- DISPLAY CHAT --------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------- GUARDRAIL --------------------
def is_valid_query(query: str) -> bool:
    keywords = ["gdpr", "ai act", "dora", "data protection", "regulation"]
    return any(k in query.lower() for k in keywords)

# -------------------- RESPONSE GENERATOR --------------------
def generate_response(messages):
    try:
        stream = ollama.chat(
            model=model,
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages,
            stream=True,
            options={"temperature": 0.0}
        )

        full_response = ""
        placeholder = st.empty()

        for chunk in stream:
            token = chunk["message"]["content"]
            full_response += token
            placeholder.markdown(full_response)

        return full_response

    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# -------------------- INPUT --------------------
user_input = st.chat_input("Ask about GDPR, EU AI Act, or DORA...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Guardrail check
    if not is_valid_query(user_input):
        reply = "I am only authorized to discuss GDPR, EU AI Act, and DORA."

        with st.chat_message("assistant"):
            st.markdown(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})

    else:
        with st.chat_message("assistant"):
            with st.spinner("Analyzing regulation..."):
                response = generate_response(st.session_state.messages)

            # Save assistant response
            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )

            # -------------------- FEEDBACK BUTTONS --------------------
            col1, col2 = st.columns(2)

            with col1:
                if st.button("👍 Helpful", key=f"up_{len(st.session_state.messages)}"):
                    save_feedback(user_input, response, "up")
                    st.success("Feedback recorded")

            with col2:
                if st.button("👎 Not Helpful", key=f"down_{len(st.session_state.messages)}"):
                    save_feedback(user_input, response, "down")
                    st.warning("Feedback recorded")