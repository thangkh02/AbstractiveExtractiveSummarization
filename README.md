# Tóm Tắt Văn Bản Bằng Mô Hình Ngôn Ngữ - Tiếng Việt

> Dự án tóm tắt văn bản tiếng Việt tự động bằng hai phương pháp Extractive (trích xuất) và Abstractive (trừu tượng)

## Giới Thiệu

Đây là dự án so sánh hai cách tiếp cận cho bài toán tóm tắt văn bản tiếng Việt:

### Tóm tắt trích xuất (Extractive Summarization)
Phương pháp này tìm kiếm và trích xuất các câu, cụm từ quan trọng nhất từ văn bản gốc.

Các mô hình sử dụng:
- PhoBERT + KMeans/DBSCAN (không cần dữ liệu huấn luyện)
- PhoBERT + Linear Layer (cần dữ liệu huấn luyện)

### Tóm tắt trừu tượng (Abstractive Summarization)
Phương pháp này tạo ra một bản tóm tắt hoàn toàn mới bằng cách diễn đạt lại ý chính của văn bản.

Các mô hình sử dụng:
- ViT5 (chế độ không huấn luyện và có huấn luyện)
- Llama 3.2 (chế độ không huấn luyện và có huấn luyện với QLoRA)

## Ý Nghĩa và Ứng Dụng

Tóm tắt văn bản tiếng Việt tự động giải quyết nhiều nhu cầu:
- Người dùng có thể nắm bắt nội dung chính mà không cần đọc hết
- Doanh nghiệp có thể tự động lọc, tổng hợp thông tin
- Ứng dụng trong phân tích tin tức, quản lý tài liệu, giám sát mạng xã hội

## Kết Quả Đạt Được

| Mô Hình | ROUGE-1 | ROUGE-2 | ROUGE-L | BLEU |
|---------|---------|---------|---------|------|
| PhoBERT + KMeans | 0.67 | 0.42 | 0.44 | 23 |
| PhoBERT + DBSCAN | 0.49 | 0.30 | 0.34 | 9 |
| PhoBERT + Linear | 0.69 | 0.51 | 0.50 | 29.83 |
| ViT5 (không huấn luyện) | 0.37 | 0.22 | 0.27 | 1.527 |
| ViT5 (có huấn luyện) | 0.71 | 0.49 | 0.50 | 30.11 |
| Llama 3.2 (không huấn luyện) | 0.61 | 0.43 | 0.43 | 24.15 |
| Llama 3.2 (có huấn luyện) | 0.70 | 0.51 | 0.52 | 35 |

Hai mô hình tốt nhất: Llama 3.2 (có huấn luyện) và ViT5 (có huấn luyện)

## Cấu Trúc Thư Mục

```
AbstractiveExtractiveSummarization/
├── README.md                          # File này
├── .env.example                       # Template biến môi trường
├── .gitignore                         # Các file không theo dõi
├── requirements.txt                   # Danh sách các thư viện cần cài
│
├── Data/                              # Dữ liệu huấn luyện
│   ├── abstractive_summarization.csv
│   ├── extractive_summarization.csv
│   └── oreo_news_summarization_vi_train.csv
│
├── notebooks/                         # Các notebook thí nghiệm
│   ├── extractive/                    # Phương pháp trích xuất
│   ├── abstractive/                   # Phương pháp trừu tượng
│   └── llama/                         # Thí nghiệm với Llama
│
├── models/                            # Mô hình đã huấn luyện
│   ├── extractive/
│   └── abstractive/
│
├── results/                           # Kết quả đánh giá
│   └── benchmarks/                    # Dữ liệu benchmark
│
├── src/                               # Mã lập trình tái sử dụng
│   └── __init__.py
│
├── docs/                              # Tài liệu
│   ├── SETUP.md                       # Hướng dẫn cài đặt
│   ├── STRUCTURE.md                   # Giải thích cấu trúc
│   └── docs.pdf                       # Slide thuyết trình
│
└── config/                            # File cấu hình
```

## Bắt Đầu Nhanh

Yêu cầu:
- Python >= 3.8
- pip (trình quản lý thư viện Python)

Cài đặt:
```bash
pip install -r requirements.txt
```

Thiết lập biến môi trường:
```bash
# Copy file template
cp .env.example .env

# Chỉnh sửa file .env và thêm token từ Hugging Face
# HF_TOKEN=token_của_bạn
```

Chạy các mô hình:

Tóm tắt trích xuất:
```bash
jupyter notebook notebooks/extractive/phoBERT_kmean_dbscan.ipynb
# hoặc
jupyter notebook notebooks/extractive/phobert-extractive-summarization.ipynb
```

Tóm tắt trừu tượng:
```bash
# ViT5
jupyter notebook notebooks/abstractive/sumarization-vit5.ipynb

# Llama 3.2
jupyter notebook notebooks/llama/llama31\ \(4\).ipynb
```

## Nền Tảng Kỹ Thuật

Kiến trúc Transformer:
- Encoder-only: BERT, PhoBERT, RoBERTa (tập trung vào hiểu ngữ nghĩa)
- Decoder-only: T5, ViT5, mT5 (tập trung vào sinh văn bản)
- Encoder-Decoder: LLaMA, Mistral, GPT-style (linh hoạt cho nhiều tác vụ)

PhoBERT & BERT:
- Mô hình BERT được tối ưu cho tiếng Việt
- Hiểu được ngữ cảnh hai chiều
- Rất tốt cho trích xuất và phân loại văn bản

ViT5:
- Phiên bản tiếng Việt của T5 của Google
- Kiến trúc Sequence-to-Sequence
- Được thiết kế để chuyển tất cả bài toán NLP thành dạng text-to-text

Llama 3.2 (1 Tỷ Tham Số):
- Mô hình nhẹ, hiệu quả với 1 tỷ tham số
- Hỗ trợ cửa sổ ngữ cảnh 128K token
- Được huấn luyện với QLoRA để tiết kiệm bộ nhớ

QLoRA Fine-tuning:
- Kỹ thuật kết hợp Low-Rank Adaptation với lượng tử hóa
- Giảm đáng kể yêu cầu bộ nhớ
- Vẫn duy trì hiệu suất cao
- Rất phù hợp cho GPU consumer

Chỉ Số Đánh Giá:

ROUGE (Recall-Oriented Understudy for Gisting Evaluation):
- ROUGE-1: So sánh unigram (từ đơn)
- ROUGE-2: So sánh bigram (cặp từ)  
- ROUGE-L: Độ dài của dãy con chung dài nhất

BLEU (Bilingual Evaluation Understudy):
- Precision dựa trên n-gram kèm theo hình phạt
- Phạt những bản tóm tắt quá ngắn so với bản tham chiếu

## Thông Tin Dữ Liệu

- Dữ liệu huấn luyện: 29.509 mẫu (cho cả trích xuất và trừu tượng)
- Dữ liệu benchmark: 5.000 mẫu kiểm tra
- Ngôn ngữ: Tiếng Việt
- Định dạng: CSV chứa nội dung gốc và bản tóm tắt tham chiếu

## Các Công Nghệ Sử Dụng

- NLP Models: Transformers (Hugging Face)
- Deep Learning: PyTorch
- Fine-tuning: PEFT (Parameter-Efficient Fine-Tuning)
- Lượng tử hóa: BitsAndBytes
- Clustering: scikit-learn (KMeans, DBSCAN)
- Đánh giá: ROUGE, BLEU
- Xử lý dữ liệu: Pandas, NumPy

## Những Phát Hiện Chính

Phương pháp Trích xuất:
- PhoBERT + Linear Layer: Hiệu suất cân bằng tốt nhất (ROUGE-1: 0.69, BLEU: 29.83)
- Suy luận nhanh, độ chính xác tin cậy
- Bị giới hạn chỉ có thể dùng nội dung từ văn bản gốc

Phương pháp Trừu tượng (chưa huấn luyện):
- ViT5 và Llama ở chế độ không huấn luyện có hiệu suất kém
- Cần phải huấn luyện để hoạt động tốt với tiếng Việt

Phương pháp Trừu tượng (đã huấn luyện):
- Llama 3.2 có huấn luyện: Điểm BLEU cao nhất (35) - độ lưu loát xuất sắc
- ViT5 có huấn luyện: Hiệu suất cân bằng mạnh (ROUGE-1: 0.71)
- Tạo ra các bản tóm tắt tự nhiên, ngắn gọn hơn
- Hiểu rõ hơn về ngữ nghĩa sâu của văn bản

## Những Điểm Nổi Bật về Kiến Trúc

Thuật toán OREO:
- Lựa chọn câu tối ưu bằng cách ước tính kỳ vọng oracle
- Beam search kèm cắt tỉa để tăng hiệu quả
- Kỳ vọng được tiền tính toán để hội tụ nhanh hơn

Clustering cho Trích xuất:
- KMeans: Xác định k cụm, chọn câu đại diện
- DBSCAN: Dựa trên mật độ, xử lý tốt hơn với độ dài tóm tắt khác nhau

## Ví Dụ Sử Dụng

Xem các notebook riêng lẻ để biết chi tiết:
- Tải và tiền xử lý dữ liệu
- Sử dụng mô hình để dự đoán
- Huấn luyện các mô hình
- Đánh giá trên dữ liệu benchmark

## Đóng Góp

Đây là dự án học tập và nghiên cứu. Nếu bạn có ý kiến cải thiện hoặc phát hiện lỗi, hãy tạo một issue.

## Giấy Phép

Dự án này dành cho mục đích giáo dục và nghiên cứu.

## Nhóm Phát Triển

Dự án Nghiên Cứu Học Thuật
- Tập trung: Tóm tắt văn bản tiếng Việt
- Phương pháp: Trích xuất & Trừu tượng
- Mô hình: PhoBERT, ViT5, Llama 3.2

## Hỗ Trợ

Nếu có câu hỏi hoặc gặp sự cố:
1. Kiểm tra notebook liên quan để xem chi tiết triển khai
2. Xem docs.pdf để hiểu rõ hơn về dự án
3. Đọc các chú thích trong code và ô markdown

## Tài Liệu Tham Khảo

- PhoBERT: https://github.com/VinAIResearch/PhoBERT
- Hugging Face Models: https://huggingface.co/models
- PEFT for Parameter-Efficient Fine-tuning: https://github.com/huggingface/peft
- ROUGE Evaluation: https://github.com/google-research/rouge

---

Lần cập nhật cuối: 19 tháng 4 năm 2026  
Trạng thái: Đang phát triển tích cực
