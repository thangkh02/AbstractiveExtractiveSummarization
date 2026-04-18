# Abstractive & Extractive Summarization Using Language Models

> **Vietnamese Text Summarization using Extractive and Abstractive Methods with Large Language Models**

## 📋 Project Overview

This project implements and compares two approaches for automatic Vietnamese text summarization:

### **Extractive Summarization** (Tóm tắt trích xuất)
Identifies and extracts important sentences/phrases from the original text.

**Methods:**
- PhoBERT + KMeans/DBSCAN (Unsupervised)
- PhoBERT + Linear Layer (Supervised)

### **Abstractive Summarization** (Tóm tắt trừu tượng)
Generates a concise summary by rephrasing and synthesizing the main ideas.

**Methods:**
- ViT5 (Zero-shot & Fine-tuned)
- Llama 3.2 (Zero-shot & Fine-tuned with QLoRA)

## 🎯 Motivation

Vietnamese text summarization is crucial for:
- **Users:** Save time by quickly understanding main content
- **Businesses:** Automate information filtering and aggregation
- **Applications:** News analysis, document management, social media monitoring

## 📊 Results & Performance

| Model | ROUGE-1 | ROUGE-2 | ROUGE-L | BLEU |
|-------|---------|---------|---------|------|
| PhoBERT + KMeans | 0.67 | 0.42 | 0.44 | 23 |
| PhoBERT + DBSCAN | 0.49 | 0.30 | 0.34 | 9 |
| PhoBERT + Linear | 0.69 | 0.51 | 0.50 | 29.83 |
| ViT5 (No Fine-tune) | 0.37 | 0.22 | 0.27 | 1.527 |
| **ViT5 (Fine-tuned)** | **0.71** | **0.49** | **0.50** | **30.11** |
| Llama 3.2 (No Fine-tune) | 0.61 | 0.43 | 0.43 | 24.15 |
| **Llama 3.2 (Fine-tuned)** | **0.70** | **0.51** | **0.52** | **35** |

✅ **Best Models:** Llama 3.2 (Fine-tuned) & ViT5 (Fine-tuned)

## 📁 Project Structure

```
AbstractiveExtractiveSummarization/
├── README.md                          # This file
├── .env.example                       # Environment template
├── .gitignore                         # Git ignore rules
│
├── Data/                              # Training & test data
│   ├── abstractive_summarization.csv
│   ├── extractive_summarization.csv
│   └── oreo_news_summarization_vi_train.csv
│
├── Benchmark/                         # Benchmark datasets
│   ├── abstractive_summarization_benchmark.csv
│   ├── extractive_summarization_benchmark.csv
│   └── oreo_summarization_benchmark.csv
│
├── Code/                              # Implementation notebooks
│   ├── phoBERT_kmean_dbscan.ipynb     # Extractive with KMeans/DBSCAN
│   ├── phobert-extractive-summarization.ipynb  # Extractive with Linear
│   ├── phoBERT inference.ipynb        # PhoBERT inference examples
│   ├── sumarization-vit5.ipynb        # Abstractive with ViT5
│   ├── oreo-approach-ipynb.ipynb      # OREO algorithm approach
│   └── best_phobert_extractive.pt     # Pre-trained extractive model
│
├── Code Llama 3.2 1B/                 # Large Language Model implementations
│   ├── nh-gi-m-h-nh-llama.ipynb       # Llama Vietnamese summarization
│   └── llama31 (4).ipynb              # Llama fine-tuning experiments
│
└── docs.pdf                           # Project presentation slides
```

## 🚀 Quick Start

### Prerequisites
```bash
python >= 3.8
pip install -r requirements.txt
```

### Setup Environment
```bash
# Copy environment template
cp .env.example .env

# Add your Hugging Face token
# Edit .env and set: HF_TOKEN=your_token_here
```

### Running Models

**Extractive Summarization:**
```bash
jupyter notebook Code/phoBERT_kmean_dbscan.ipynb
# or
jupyter notebook Code/phobert-extractive-summarization.ipynb
```

**Abstractive Summarization:**
```bash
# ViT5
jupyter notebook Code/sumarization-vit5.ipynb

# Llama 3.2
jupyter notebook "Code Llama 3.2 1B/llama31 (4).ipynb"
```

## 📚 Technical Foundations

### Transformer Architecture
- **Encoder-only:** BERT, PhoBERT, RoBERTa (understanding focused)
- **Decoder-only:** T5, ViT5, mT5 (text generation focused)
- **Encoder-Decoder:** LLaMA, Mistral, GPT-style (versatile)

### Key Techniques

#### **BERT & PhoBERT**
- Vietnamese-optimized BERT model
- Bidirectional context understanding
- Excellent for semantic understanding & extraction

#### **ViT5**
- Vietnamese version of Google's T5
- Sequence-to-Sequence architecture
- Text-to-text framework for summarization

#### **Llama 3.2 (1B)**
- Efficient 1 billion parameter model
- 128K token context window
- Fine-tuned with QLoRA for reduced memory usage

#### **QLoRA Fine-tuning**
- Low-Rank Adaptation with quantization
- Reduces memory requirements
- Maintains high performance
- Ideal for consumer GPUs

### Evaluation Metrics

**ROUGE (Recall-Oriented Understudy for Gisting Evaluation)**
- ROUGE-1: Unigram overlap
- ROUGE-2: Bigram overlap  
- ROUGE-L: Longest common subsequence

**BLEU (Bilingual Evaluation Understudy)**
- N-gram precision with brevity penalty
- Penalizes overly short summaries

## 📖 Dataset Information

- **Training Data:** 29,509 samples (both extractive & abstractive)
- **Benchmark Data:** 5,000 test samples
- **Language:** Vietnamese
- **Format:** CSV with source content and reference summaries

## 🔧 Technologies & Libraries

- **NLP Models:** Transformers (Hugging Face)
- **Deep Learning:** PyTorch
- **Fine-tuning:** PEFT (Parameter-Efficient Fine-Tuning)
- **Quantization:** BitsAndBytes
- **Clustering:** scikit-learn (KMeans, DBSCAN)
- **Evaluation:** ROUGE, BLEU
- **Data Processing:** Pandas, NumPy

## 📝 Key Findings

✅ **Extractive Methods:**
- PhoBERT + Linear Layer: Best balanced performance (ROUGE-1: 0.69, BLEU: 29.83)
- Fast inference, reliable accuracy
- Limited to existing content

❌ **Abstractive Methods (Untuned):**
- ViT5 & Llama zero-shot show lower performance
- Requires fine-tuning for Vietnamese

✅ **Abstractive Methods (Fine-tuned):**
- Llama 3.2 FT: Highest BLEU score (35) - excellent fluency
- ViT5 FT: Strong balanced performance (ROUGE-1: 0.71)
- Generate more natural, concise summaries
- Better semantic understanding

## 🎓 Architecture Highlights

### OREO Algorithm
- Optimized sentence selection using oracle expectation
- Beam search with pruning for efficiency
- Pre-scaled expectation for better convergence

### Clustering for Extraction
- **KMeans:** Determines k clusters, selects representative sentences
- **DBSCAN:** Density-based, handles variable-length summaries better

## 📌 Usage Examples

See individual notebook files for detailed usage:
- Data loading and preprocessing
- Model inference
- Fine-tuning procedures
- Evaluation on benchmark dataset

## 🤝 Contributing

This is an academic/research project. For improvements or bug reports, please create an issue.

## 📄 License

This project is for educational and research purposes.

## 👥 Project Team

**Academic Research Project**
- Focus: Vietnamese Text Summarization
- Approaches: Extractive & Abstractive
- Models: PhoBERT, ViT5, Llama 3.2

## 📞 Support

For questions or issues:
1. Check the relevant notebook for implementation details
2. Review the `docs.pdf` for project presentation
3. Examine the code comments and markdown cells

## 🔗 Resources

- [PhoBERT](https://github.com/VinAIResearch/PhoBERT)
- [Hugging Face Models](https://huggingface.co/models)
- [PEFT for Parameter-Efficient Fine-tuning](https://github.com/huggingface/peft)
- [ROUGE Evaluation](https://github.com/google-research/rouge)

---

**Last Updated:** April 19, 2026  
**Status:** ✅ Active Development
