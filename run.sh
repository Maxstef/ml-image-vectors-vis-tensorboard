#!/usr/bin/env bash
set -e

echo "🚀 Creating virtual environment (if needed)..."

python3 -m venv venv

source venv/bin/activate  # Linux/Mac

echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo "📥 Downloading datasets..."
python scripts/download_data.py

echo "🧹 Preparing datasets..."
python scripts/prepare_data.py

echo "🧠 Building embeddings + TensorBoard files..."
python scripts/build_projector.py

echo "📊 Starting TensorBoard..."
tensorboard --logdir ./vis