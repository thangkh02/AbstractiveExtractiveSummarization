# Setup & Installation Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for version control)
- CUDA-capable GPU (optional but recommended for training)

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/thangkh02/AbstractiveExtractiveSummarization.git
cd AbstractiveExtractiveSummarization
```

### 2. Create Virtual Environment (Recommended)

**Using venv:**
```bash
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

**Using conda:**
```bash
conda create -n summarization python=3.10
conda activate summarization
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**For GPU support (CUDA 12.1):**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### 4. Setup Environment Variables

```bash
# Copy the template
cp .env.example .env

# Edit .env and add your credentials
# Get HF_TOKEN from: https://huggingface.co/settings/tokens
nano .env  # or use your preferred editor
```

**Example .env file:**
```
# Hugging Face API Token
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxx
```

### 5. Verify Installation

```bash
# Test PyTorch installation
python -c "import torch; print(f'PyTorch {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}')"

# Test transformers installation
python -c "import transformers; print(f'Transformers {transformers.__version__}')"

# Test other dependencies
python -c "import sklearn, pandas, numpy; print('All dependencies installed ✓')"
```

## Jupyter Notebook Setup

### Install Jupyter (if not included)
```bash
pip install jupyter jupyterlab
```

### Launch Jupyter
```bash
# Use Jupyter Lab (recommended)
jupyter lab

# Or use Jupyter Notebook
jupyter notebook
```

Navigate to the `notebooks/` folder and select an experiment to run.

## GPU Setup (For Training)

### Check CUDA Installation
```bash
# Check if CUDA is available
nvidia-smi

# Check PyTorch CUDA support
python -c "import torch; print(torch.cuda.is_available()); print(torch.cuda.get_device_name())"
```

### Memory Optimization

For limited GPU memory, fine-tuning uses:
- **QLoRA**: Low-rank adaption with quantization
- **Gradient Checkpointing**: Reduces memory usage
- **Mixed Precision**: float16 training

These are already configured in the notebooks.

## Project Structure

After installation, your project structure should look like:

```
AbstractiveExtractiveSummarization/
├── README.md
├── requirements.txt
├── .env                    # ← Created in step 4
├── notebooks/
│   ├── extractive/
│   ├── abstractive/
│   └── llama/
├── Data/
├── models/
├── results/
└── src/
```

## Quick Start

### 1. Run Extractive Summarization

```bash
jupyter lab notebooks/extractive/phoBERT_kmean_dbscan.ipynb
```

### 2. Run Abstractive Summarization (ViT5)

```bash
jupyter lab notebooks/abstractive/oreo-approach-ipynb.ipynb
```

### 3. Run LLaMA Fine-tuning

```bash
jupyter lab notebooks/llama/llama31\ \(4\).ipynb
```

## Troubleshooting

### Issue: "Module not found" errors

**Solution:**
```bash
# Reinstall all dependencies
pip install --upgrade -r requirements.txt

# Or install specific package
pip install transformers --upgrade
```

### Issue: CUDA out of memory

**Solution:**
1. Reduce batch size in notebook configuration
2. Enable gradient checkpointing (already in Llama notebooks)
3. Use smaller model variants

### Issue: Hugging Face authentication fails

**Solution:**
1. Verify HF_TOKEN in `.env` file:
   ```bash
   cat .env  # Check if token is set
   ```
2. Regenerate token from https://huggingface.co/settings/tokens
3. Make sure you're logged into Hugging Face:
   ```bash
   huggingface-cli login
   ```

### Issue: "No module named 'dotenv'"

**Solution:**
```bash
pip install python-dotenv
```

## Environment Variables

The project uses a `.env` file to manage sensitive credentials. Required variables:

| Variable | Description | Source |
|----------|-------------|--------|
| `HF_TOKEN` | Hugging Face API token | https://huggingface.co/settings/tokens |

## Useful Commands

```bash
# List installed packages
pip list

# Update all packages
pip install --upgrade -r requirements.txt

# Deactivate virtual environment
deactivate  # or: conda deactivate

# Remove virtual environment
rm -rf venv  # or: conda remove --name summarization --all

# Check Python version
python --version

# Check CUDA availability
python -c "import torch; print(torch.cuda.is_available())"
```

## Next Steps

1. Read [STRUCTURE.md](STRUCTURE.md) to understand the project organization
2. Check [README.md](../README.md) for project overview
3. Start with extractive summarization notebooks
4. Explore abstractive approaches
5. Review model performance in results/benchmarks/

## Support & Issues

For setup issues or questions:
1. Check this guide again
2. Review the README.md
3. Check notebook comments and markdown cells
4. Refer to official documentation:
   - [PyTorch](https://pytorch.org)
   - [Hugging Face Transformers](https://huggingface.co/docs/transformers)
   - [PEFT](https://github.com/huggingface/peft)

---

**Last Updated:** April 19, 2026
