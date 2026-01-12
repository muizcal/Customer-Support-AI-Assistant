import streamlit as st
import requests


st.set_page_config(
    page_title="Customer Support AI Assistant",
    page_icon="🤖",
    layout="centered",
)


st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>Customer Support AI Assistant 🤖</h1>", unsafe_allow_html=True)
st.markdown("---") 


st.sidebar.header("About")
st.sidebar.info(
    "This app lets you ask questions to the AI assistant based on company documents.\n\n"
    "It uses a Retrieval-Augmented Generation (RAG) pipeline."
)


st.markdown("### Ask a question:")
question = st.text_input("Type your question here...", "")

if st.button("Ask AI", type="primary"):
    if question.strip() == "":
        st.warning("Please type a question before hitting Ask!")
    else:
        with st.spinner("AI is thinking... 🤔"):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/ask",
                    json={"question": question}
                )
                if response.status_code == 200:
                    answer = response.json()["answer"]
                    st.markdown(
                        f"<div style='background-color:#E8F0FE; padding:15px; border-radius:10px;'>"
                        f"<strong>Answer:</strong> {answer}</div>",
                        unsafe_allow_html=True
                    )
                else:
                    st.error("❌ Error contacting AI backend")
            except Exception as e:
                st.error(f"❌ Something went wrong: {e}")
