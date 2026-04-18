import streamlit as st
import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModel
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics.pairwise import cosine_similarity
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="Summarization App",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Ứng Dụng Tóm Tắt Văn Bản Tiếng Việt")
st.markdown("Công cụ tóm tắt văn bản tự động bằng phương pháp **Extractive** hoặc **Abstractive**")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Cấu Hình")
    
    method = st.radio(
        "Chọn phương pháp tóm tắt:",
        ["Extractive (Trích xuất)", "Abstractive (Trừu tượng)"],
        help="Extractive: trích xuất câu quan trọng\nAbstractive: tạo câu mới"
    )
    
    st.markdown("---")
    st.info("💡 **Extractive**: Nhanh, chính xác, nhưng chỉ dùng nội dung gốc\n\n**Abstractive**: Sinh văn bản mới, tự nhiên hơn")

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Nhập Văn Bản")
    input_text = st.text_area(
        "Nhập văn bản cần tóm tắt:",
        height=250,
        placeholder="Hãy dán văn bản tiếng Việt ở đây..."
    )
    
    text_length = len(input_text.split())
    st.caption(f"📊 Số từ: {text_length}")

with col2:
    st.subheader("📤 Tóm Tắt Kết Quả")
    
    # Model selection based on method
    if "Extractive" in method:
        model_choice = st.selectbox(
            "Chọn mô hình:",
            ["PhoBERT + KMeans", "PhoBERT + DBSCAN", "PhoBERT + Linear"]
        )
        
        ratio = st.slider(
            "Tỉ lệ tóm tắt (%):",
            min_value=10,
            max_value=50,
            value=30,
            step=5
        )
    else:
        model_choice = st.selectbox(
            "Chọn mô hình:",
            ["ViT5 (Trained)", "Llama 3.2 (Trained)", "ViT5 (Untrained)"]
        )
        
        max_length = st.slider(
            "Độ dài tối đa (từ):",
            min_value=20,
            max_value=200,
            value=100,
            step=10
        )

# Run button
if st.button("🚀 Tóm Tắt", use_container_width=True, type="primary"):
    if not input_text.strip():
        st.error("❌ Vui lòng nhập văn bản để tóm tắt!")
    else:
        with st.spinner("⏳ Đang xử lý..."):
            try:
                # Simulated summarization results
                # In production, load actual models
                
                if "Extractive" in method:
                    if model_choice == "PhoBERT + KMeans":
                        summary = "Kết quả tóm tắt bằng phương pháp KMeans clustering trên PhoBERT embeddings."
                    elif model_choice == "PhoBERT + DBSCAN":
                        summary = "Kết quả tóm tắt bằng phương pháp DBSCAN clustering trên PhoBERT embeddings."
                    else:
                        summary = "Kết quả tóm tắt bằng mô hình PhoBERT với Linear Layer sau huấn luyện."
                else:
                    if "ViT5" in model_choice and "Trained" in model_choice:
                        summary = "Kết quả tóm tắt bằng mô hình ViT5 sau huấn luyện chi tiết."
                    elif "Llama" in model_choice:
                        summary = "Kết quả tóm tắt bằng mô hình Llama 3.2 với fine-tuning QLoRA."
                    else:
                        summary = "Kết quả tóm tắt bằng mô hình ViT5 ở chế độ không huấn luyện."
                
                st.success("✅ Tóm tắt hoàn thành!")
                st.text_area(
                    "Kết quả:",
                    value=summary,
                    height=250,
                    disabled=True
                )
                
                # Show statistics
                st.markdown("---")
                st.subheader("📊 Thống Kê")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Văn bản gốc", f"{len(input_text.split())} từ")
                
                with col2:
                    st.metric("Tóm tắt", f"{len(summary.split())} từ")
                
                with col3:
                    compression = (1 - len(summary.split()) / len(input_text.split())) * 100
                    st.metric("Nén", f"{compression:.1f}%")
                
            except Exception as e:
                st.error(f"❌ Lỗi: {str(e)}")

# Additional information
st.markdown("---")
st.subheader("ℹ️ Thông Tin Thêm")

tabs = st.tabs(["Về Phương Pháp", "Hướng Dẫn Sử Dụng", "Kết Quả So Sánh"])

with tabs[0]:
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔍 Extractive Summarization")
        st.markdown("""
        **Ưu điểm:**
        - ⚡ Xử lý nhanh
        - 🎯 Chính xác cao
        - 💾 Ít tài nguyên
        
        **Nhược điểm:**
        - 📌 Chỉ dùng câu gốc
        - 🚫 Không thể sáng tạo
        """)
    
    with col2:
        st.markdown("### ✨ Abstractive Summarization")
        st.markdown("""
        **Ưu điểm:**
        - 🎨 Sinh câu mới
        - 📝 Tự nhiên hơn
        - 🧠 Hiểu ngữ nghĩa sâu
        
        **Nhược điểm:**
        - ⏱️ Xử lý chậm hơn
        - 💿 Cần nhiều tài nguyên
        """)

with tabs[1]:
    st.markdown("""
    ### Hướng Dẫn Sử Dụng:
    
    1. **Chọn Phương Pháp**: Lựa chọn giữa Extractive hoặc Abstractive
    2. **Chọn Mô Hình**: Tùy chọn mô hình cụ thể
    3. **Nhập Văn Bản**: Dán văn bản cần tóm tắt
    4. **Điều Chỉnh Tham Số**: 
       - Extractive: Tỉ lệ tóm tắt (%)
       - Abstractive: Độ dài tối đa (từ)
    5. **Bấm "Tóm Tắt"**: Chờ kết quả
    """)

with tabs[2]:
    st.markdown("""
    ### 📈 Kết Quả So Sánh
    
    | Mô Hình | ROUGE-1 | ROUGE-2 | ROUGE-L | BLEU |
    |---------|---------|---------|---------|------|
    | PhoBERT + KMeans | 0.67 | 0.42 | 0.44 | 23 |
    | PhoBERT + Linear | 0.69 | 0.51 | 0.50 | 29.83 |
    | ViT5 (Trained) | 0.71 | 0.49 | 0.50 | 30.11 |
    | Llama 3.2 (Trained) | 0.70 | 0.51 | 0.52 | **35** 🏆 |
    
    **Mô hình tốt nhất**: Llama 3.2 (Trained) với BLEU = 35
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <small>
    Ứng dụng Tóm Tắt Văn Bản Tiếng Việt | 
    <a href="https://github.com/thangkh02/AbstractiveExtractiveSummarization">GitHub</a>
    </small>
</div>
""", unsafe_allow_html=True)
