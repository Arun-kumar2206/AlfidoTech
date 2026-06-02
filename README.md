# AlfidoTech - Setup and Run Guide

## Environment Setup (macOS/Linux)

```bash
cd /Users/arun/Developer/AlfidoTech
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r task3/requirements.txt
```

## Run Notebooks

If you use Jupyter Lab:

```bash
cd /Users/arun/Developer/AlfidoTech
source .venv/bin/activate
jupyter lab
```

If you use Jupyter Notebook:

```bash
cd /Users/arun/Developer/AlfidoTech
source .venv/bin/activate
jupyter notebook
```

Open the notebook files in VS Code or the Jupyter UI:

- task1/Email_Spam_Detection_with_Machine_Learning.ipynb
- task2/CIFAR100_with_ResNet50.ipynb
- task4/Fairness_Bias_Explainability.ipynb

## Run Task 3 API Locally (FastAPI)

### Option A: Run with Python

```bash
cd /Users/arun/Developer/AlfidoTech/task3
source ../.venv/bin/activate
python -m pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

Test request:

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"email_text":"Free entry in 2 a wkly comp to win FA Cup final tkts"}'
```

### Option B: Run with Docker Compose

```bash
cd /Users/arun/Developer/AlfidoTech/task3
docker compose up --build
```

Test request:

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"email_text":"Free entry in 2 a wkly comp to win FA Cup final tkts"}'
```

## Inference (Task 2)

The task2 notebook contains an inference cell that loads a saved model and predicts a single image. Update the `image_path` in that cell before running it.
