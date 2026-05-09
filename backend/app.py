import streamlit as st
import requests
import time

API_CHAT = "http://127.0.0.1:8000/chat"
API_UPLOAD = "http://127.0.0.1:8000/upload"

st.set_page_config(page_title="PDF AI Chatbot", layout="wide")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.title("📄 PDF AI Bot")

    st.subheader("📤 Upload PDFs")

    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button("Upload"):
        if uploaded_files:
            files = [
                ("files", (f.name, f.getvalue(), "application/pdf"))
                for f in uploaded_files
            ]

            res = requests.post(API_UPLOAD, files=files)

            if res.status_code == 200:
                st.success("Uploaded successfully 🚀")
            else:
                st.error("Upload failed ❌")

        else:
            st.warning("Select files first")

    st.divider()
    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []

# ---------------- INIT STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- TITLE ----------------
st.title("💬 Chat with your PDFs")

# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- INPUT ----------------
user_input = st.chat_input("Ask something from your PDFs...")

if user_input:

    # USER MESSAGE
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # BOT RESPONSE PLACEHOLDER
    with st.chat_message("assistant"):
        placeholder = st.empty()
        placeholder.markdown("Thinking... 🤔")

        try:
            res = requests.get(API_CHAT, params={"query": user_input})
            answer = res.json().get("answer", "No response")

        except Exception as e:
            answer = f"Error: {str(e)}"

        # typing effect (PRO UI FEEL)
        typed_text = ""
        for char in answer:
            typed_text += char
            time.sleep(0.01)
            placeholder.markdown(typed_text)

    st.session_state.messages.append({"role": "assistant", "content": answer})