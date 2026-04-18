# Project Structure

This document explains the reorganized project structure for the Abstractive & Extractive Summarization project.

## Directory Organization

```
AbstractiveExtractiveSummarization/
│
├── 📄 README.md                    # Project overview & quick start
├── 📄 requirements.txt             # Python dependencies
├── 📄 .env.example                 # Environment variables template
├── 📄 .gitignore                   # Git ignore rules
│
├── 📁 notebooks/                   # Jupyter notebooks organized by approach
│   ├── extractive/                 # Extractive summarization experiments
│   │   ├── phoBERT_kmean_dbscan.ipynb
│   │   ├── phobert-extractive-summarization.ipynb
│   │   └── phoBERT inference.ipynb
│   │
│   ├── abstractive/                # Abstractive summarization experiments
│   │   ├── oreo-approach-ipynb.ipynb
│   │   └── (placeholder for ViT5 notebooks)
│   │
│   └── llama/                      # Large Language Model experiments
│       ├── llama31 (4).ipynb       # Main Llama 3.2 fine-tuning
│       └── nh-gi-m-h-nh-llama.ipynb # Llama Vietnamese experiments
│
├── 📁 Data/                        # Training & raw data
│   ├── abstractive_summarization.csv
│   ├── extractive_summarization.csv
│   └── oreo_news_summarization_vi_train.csv
│
├── 📁 models/                      # Pre-trained & fine-tuned models
│   ├── extractive/
│   │   └── best_phobert_extractive.pt  # Best extractive model checkpoint
│   │
│   └── abstractive/                    # (Placeholder for abstractive models)
│       └── (Fine-tuned ViT5, Llama models will go here)
│
├── 📁 results/                     # Evaluation & benchmark results
│   ├── benchmarks/                 # Benchmark datasets & results
│   │   ├── abstractive_summarization_benchmark.csv
│   │   ├── extractive_summarization_benchmark.csv
│   │   └── oreo_summarization_benchmark.csv
│   │
│   └── (Output results, metrics, comparisons)
│
├── 📁 src/                         # Reusable source code & utilities
│   ├── __init__.py                 # Package initialization
│   ├── extractive/                 # Extractive summarization modules
│   ├── abstractive/                # Abstractive summarization modules
│   ├── utils/                      # Helper utilities
│   └── evaluation/                 # Evaluation metrics & scripts
│
├── 📁 config/                      # Configuration files
│   ├── extractive_config.yaml      # Extractive model configs
│   ├── abstractive_config.yaml     # Abstractive model configs
│   └── training_config.yaml        # Training parameters
│
├── 📁 docs/                        # Documentation & presentation
│   ├── docs.pdf                    # Project presentation slides
│   ├── STRUCTURE.md                # This file
│   ├── SETUP.md                    # Setup & installation guide
│   └── USAGE.md                    # Detailed usage examples
│
└── 📁 Code Llama 3.2 1B/           # [Legacy] Original Llama notebooks
    └── (Will be deprecated - content moved to notebooks/llama/)
```

## File Organization Purpose

### **notebooks/**
- Clean separation between extractive, abstractive, and LLM approaches
- Easy navigation for researchers exploring different methods
- Self-contained experiments with clear naming

### **models/**
- Organized by approach (extractive/abstractive)
- Pre-trained and fine-tuned checkpoints
- Easy model loading in inference scripts

### **results/benchmarks/**
- Centralized evaluation results
- Comparison benchmarks for all methods
- CSV format for easy analysis

### **src/**
- Reusable Python modules (future)
- Shared utilities across notebooks
- Clean code for production use

### **config/**
- YAML configuration files
- Hyperparameters for reproducibility
- Easy experiment management

### **docs/**
- Project documentation
- Presentation materials
- Setup guides

## Migration Status

✅ **Completed:**
- README.md with full project description
- New directory structure created
- Notebooks reorganized by approach
- Models moved to models/extractive/
- Benchmarks copied to results/benchmarks/
- Documentation moved to docs/

⏳ **Future:**
- Move utilities to src/
- Create YAML config files
- Add evaluation scripts to src/evaluation/
- Add inference/deployment scripts

## How to Use

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Setup environment:**
   ```bash
   cp .env.example .env
   # Edit .env with your Hugging Face token
   ```

3. **Run experiments:**
   ```bash
   # Extractive summarization
   jupyter notebook notebooks/extractive/phoBERT_kmean_dbscan.ipynb
   
   # Abstractive with ViT5
   jupyter notebook notebooks/abstractive/oreo-approach-ipynb.ipynb
   
   # LLaMA experiments
   jupyter notebook notebooks/llama/llama31\ \(4\).ipynb
   ```

## Data Structure

- **Training Data**: Located in `Data/` (29,509 samples each for extractive & abstractive)
- **Benchmark Data**: Located in `results/benchmarks/` (5,000 test samples)
- **Models**: Located in `models/{approach}/`

---

**Last Updated:** April 19, 2026  
**Structure Version:** 1.0
