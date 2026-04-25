# Image Embedding Visualization with TensorBoard Projector

This project visualizes image datasets in a 2D/3D embedding space using a pretrained CNN and TensorBoard Projector.

## 📦 Datasets

Two datasets are used:

* 🐾 Animal image classification (5 species)
* 🔢 Handwritten digits (0–9)

Original sources:

* [Kaggle - Animal Image Classification – 5 Species](https://www.kaggle.com/datasets/miadul/animal-image-classification-5-species)
* [Kaggle - Handwritten Digits 0–9](https://www.kaggle.com/datasets/olafkrastovski/handwritten-digits-0-9)

---

## 🧠 Goal of the project

This project is primarily educational and aims to:

* understand how CNN embeddings represent images in high-dimensional space
* visualize embeddings in an interpretable way using TensorBoard Projector
* practice building clean, reproducible ML workflows

---

## 🧠 What this project does

The pipeline extracts feature vectors from images using a pretrained **ResNet18** model and visualizes them in TensorBoard Projector.

### Workflow:

```
Images → ResNet18 embeddings → metadata + sprite → TensorBoard Projector
```

---

## 📊 Visualization example

Once running, you can explore:
- clusters of similar animals
- digit groupings (0–9 separation)
- image similarity in embedding space

---

## 📁 Project structure
```
.
├── notebooks/
│ ├── prepare_data.ipynb
│ ├── build_projector_v0.ipynb
│ ├── build_projector.ipynb
│ └── build_projector_legacy.ipynb
│
├── scripts/
│ ├── download_data.py
│ ├── prepare_data.py
│ └── build_projector.py
│
├── vis/ # generated TensorBoard files
├── images/ # animal dataset
├── digits/ # digit dataset
├── requirements.txt
└── README.md
```

---

## 🚀 Quick start

### 1. Clone Repo

```bash
git https://github.com/Maxstef/ml-image-vectors-vis-tensorboard.git
cd ml-image-vectors-vis-tensorboard
```

### 2. (Optional but recommended) Create a virtual environment
Using conda:

```bash
conda create -n projector-env python=3.10
conda activate projector-env
```

Or using venv:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download datasets

```
python scripts/download_data.py
```

### 5. Prepare datasets

```
python scripts/prepare_data.py
```

This step:
- limits dataset size (digits)
- normalizes folder structure
- renames files for consistency

### 6. Build embeddings + Projector files

```
python scripts/build_projector.py
```

This generates:
- feature vectors (.tsv)
- metadata (.tsv)
- sprite image (.jpg)
- TensorBoard config (.pbtxt)

### 7. Launch TensorBoard

```
tensorboard --logdir ./vis
```

Then open:
```
http://localhost:6006
```

Go to the Projector tab.

## 🧪 Notebooks (educational purpose)

This repository includes a set of Jupyter notebooks that document the evolution of the project from an initial prototype to a fully modular and reproducible pipeline.

They are intended for **learning and transparency**, showing why certain design decisions were made.

### 📓 `build_projector_legacy.ipynb`

* Original approach based on a Medium article
* Demonstrates naive implementation and its limitations

### 📓 `build_projector_v0.ipynb`

* First working full pipeline
* Manual but deterministic implementation

### 📓 `build_projector.ipynb`

* Refactored reusable pipeline
* Supports multiple datasets

### 📓 `prepare_data.ipynb`

* Data ingestion + preprocessing explanation
* Why dataset normalization is required

---

Together, these notebooks document the transition from a **manual experimental workflow** to a **modular, reproducible machine learning pipeline**.

## 📚 Inspiration and references

This project was inspired by existing approaches to visualizing high-dimensional image embeddings and by tools that make feature spaces interpretable.

### 📖 Blog posts and tutorials

* Hanna Pylieva — *How to visualize image feature vectors*
  [https://hanna-shares.medium.com/how-to-visualize-image-feature-vectors-1e309d45f28f](https://hanna-shares.medium.com/how-to-visualize-image-feature-vectors-1e309d45f28f)
  This article served as the starting point for the initial implementation and the “legacy” notebook version of this project.

* Takuma Yamaguchi — *Visualizing Image Feature Vectors through TensorBoard*
  [https://medium.com/@kumon/visualizing-image-feature-vectors-through-tensorboard-b850ce1be7f1](https://medium.com/@kumon/visualizing-image-feature-vectors-through-tensorboard-b850ce1be7f1)
  Demonstrates a TensorBoard-based approach to embedding visualization and helped validate the general pipeline idea.

---

### 🧠 Official tools and documentation

* TensorBoard Embedding Projector
  [https://projector.tensorflow.org/](https://projector.tensorflow.org/)
  Interactive environment for exploring high-dimensional embeddings using PCA, t-SNE, and UMAP projections.

* TensorBoard Projector documentation
  [https://www.tensorflow.org/tensorboard/tensorboard_projector_plugin](https://www.tensorflow.org/tensorboard/tensorboard_projector_plugin)
  Official documentation describing how embeddings, metadata, and sprite images are structured and visualized.

---

### 🧭 Project context

While the resources above provide foundational ideas, this project extends them by:

* supporting real-world nested datasets (train/test/validation structures)
* automating dataset cleaning and normalization
* providing a fully reproducible script-based pipeline
* enabling multi-dataset processing within a single workflow
* separating experimental notebooks from production-ready code



## 🧭 Future improvements

Future improvement might include:

- Add caching for extracted embeddings
- Replace ResNet18 with modern vision models (ViT, CLIP)
- Add UMAP/t-SNE comparison visualizations
- Introduce Streamlit or web-based interactive viewer
- Support incremental / streaming dataset updates
- Improve scalability for very large datasets

