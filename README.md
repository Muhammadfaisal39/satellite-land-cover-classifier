# 🛰️ Satellite Land Cover Classifier

A deep learning project that classifies land use and land cover 
from satellite imagery using Convolutional Neural Networks (CNN) 
with Grad-CAM explainability analysis.

---

## 🎯 Project Overview

Satellites capture thousands of images of Earth every day. 
Manually analyzing every image to understand land use — 
forests, cities, farmland, rivers — is impossible at scale.

This project answers one question:

> **Can a deep learning model automatically classify what's 
> in a satellite image — and explain why it made that decision?**

Using the EuroSAT dataset of 27,000 real satellite images 
across 10 land cover classes, this project builds an 
end-to-end image classification pipeline with explainability.

---

## 🗺️ Dataset — EuroSAT

- **Source:** EuroSAT — Sentinel-2 Satellite Imagery
- **Total Images:** 27,000
- **Classes:** 10 land cover types
- **Image Size:** 64×64 pixels (RGB)
- **Download:** [Kaggle EuroSAT Dataset](https://www.kaggle.com/datasets/apollo2506/eurosat-dataset)

### Land Cover Classes

| Class | Description |
|---|---|
| AnnualCrop | Seasonal farmland |
| Forest | Dense tree coverage |
| HerbaceousVegetation | Grasslands and shrubs |
| Highway | Roads and transport corridors |
| Industrial | Factories and warehouses |
| Pasture | Open grazing land |
| PermanentCrop | Orchards and vineyards |
| Residential | Housing and neighborhoods |
| River | Water channels |
| SeaLake | Large water bodies |

---

## 📊 Dataset Exploration

### Sample Images — One Per Class
![Sample Images](sample_images.png)

### Class Distribution
![Class Distribution](class_distribution.png)

> The dataset is slightly imbalanced — AnnualCrop has 3,007 
> images while Pasture has only 2,000. This will be addressed 
> during preprocessing.

---

## 🏗️ Project Pipeline

| Stage | Status | Description |
|---|---|---|
| Day 1 — Exploration | ✅ Done | Load dataset, visualize classes, analyze distribution |
| Day 2 — Preprocessing | 🔄 In Progress | Normalize, augment, split train/val/test |
| Day 3 — Model Training | ⬜ Upcoming | Train CNN classifier on 10 classes |
| Day 4 — Evaluation | ⬜ Upcoming | Accuracy, confusion matrix, per-class metrics |
| Day 5 — Explainability | ⬜ Upcoming | Grad-CAM visualization of model decisions |
| Day 6 — README + Polish | ⬜ Upcoming | Full documentation and results |

---

## 🛠️ Tech Stack

- **Python** — Core programming language
- **PyTorch** — Deep learning framework
- **Torchvision** — Image transforms and pretrained models
- **Matplotlib** — Visualization
- **Grad-CAM** — Explainability analysis
- **Google Colab** — GPU training environment

---

## 📁 Project Structure
satellite-land-cover-classifier/
│
├── day1_exploration.py       # Dataset exploration and visualization
├── sample_images.png         # One sample per land cover class
├── class_distribution.png    # Class frequency chart
└── README.md                 # Project documentation

---

## 🔍 Why Explainability Matters

Most satellite image classifiers are black boxes — they 
output a class label without explaining which visual 
features drove the decision.

This project adds **Grad-CAM (Gradient-weighted Class 
Activation Mapping)** to highlight exactly which regions 
of the satellite image the model focused on — making the 
system transparent and trustworthy for real-world use.

This directly addresses the interpretability gap identified 
in remote sensing and Earth observation literature.

---

## 🚀 How to Run

**1. Open in Google Colab**

**2. Mount Google Drive and set dataset path:**
```python
from google.colab import drive
drive.mount('/content/drive')
dataset_path = '/content/drive/MyDrive/satellite-project/EuroSAT'
```

**3. Run exploration:**
```python
!python day1_exploration.py
```

---

## 👨‍💻 About the Author

**Muhammad Faisal**
CS Graduate | ML Researcher | Software Engineer

- 🎓 CGPA: 3.87/4.0 — Hazara University Mansehra
- 📝 Presented ML research at HEC National Conference 2023
- 🏆 IBM Machine Learning with Python — Coursera 2026
- 💼 [LinkedIn](https://www.linkedin.com/in/muhammadfaisal39)
- 🐙 [GitHub](https://github.com/Muhammadfaisal39)

---

⭐ If you found this project useful, please give it a star!
