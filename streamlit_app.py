# copyright [2025] [Phat Nguyen Cong] (Github: https://github.com/paht2005)

import streamlit as st
from model_loader import load_classifier
from classify import classify_text

st.set_page_config(page_title="Phân loại cảm xúc tiếng Việt", layout="centered", page_icon="🧠")

st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
    }
    .stTextInput>div>div>input {
        font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 Phân loại cảm xúc văn bản tiếng Việt")
st.markdown("Nhập một câu hoặc đoạn văn tiếng Việt để phân tích cảm xúc.")

text_input = st.text_area("✍️ Nhập văn bản tại đây", height=150)

if "tokenizer" not in st.session_state or "model" not in st.session_state:
    with st.spinner("🔄 Đang tải mô hình..."):
        tokenizer, model = load_classifier()
        st.session_state.tokenizer = tokenizer
        st.session_state.model = model

if st.button("Phân loại"):
    with st.spinner("🤖 Đang phân tích..."):
        result = classify_text(text_input, st.session_state.tokenizer, st.session_state.model)
        st.success(result)
