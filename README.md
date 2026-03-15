# 👗 Fashion Model Pose Classifier

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12+-orange)
![Accuracy](https://img.shields.io/badge/Accuracy-89.92%25-brightgreen)

A deep learning model that classifies **fashion model poses in e-commerce images** into 7 categories:

front • back • side • crop • full • flat • infographic

The model achieved **89.92% validation accuracy** using **DenseNet121 architecture** with **300×300 resolution images**.

---

# 📊 Model Performance

| Metric | Value |
|------|------|
| Validation Accuracy | **89.92%** |
| Input Size | 300 × 300 × 3 |
| Classes | 7 pose categories |
| Architecture | DenseNet121 + Custom Head |
| Inference Time (CPU) | ~0.5–1.5s per image |
| Inference Time (GPU) | ~0.05–0.15s per image |

---

# 🎯 Pose Categories

| Class | Description |
|------|-------------|
| front | Front-facing model shot |
| back | Back view |
| side | Side profile |
| crop | Close-up product detail |
| full | Full body product shot |
| flat | Flat lay product image |
| infographic | Catalog infographic / design |

---

# 🚀 Real-World Use Case

Fashion marketplaces receive **thousands of product images** that need to be organized by viewing angle.

This model can help automate:

• e-commerce catalog organization  
• visual content pipelines  
• product image QA  
• dataset labeling workflows  

This project was inspired by work done while building **Picxcale**, an AI-powered platform for automating large-scale e-commerce image processing.

---

# 📦 Download Trained Model

The trained model is available in **GitHub Releases**.

Download here:
https://github.com/Aaksh-tech/fashion-angle-classifier/releases

Model file:


final_production_model.keras


---

# ⚡ Quick Start

## Install dependencies


pip install -r requirements.txt


## Run prediction


python demo.py sample_front.jpg


Example output:


📸 Image: sample_front.jpg
🎯 Predicted angle: front
📊 Confidence: 96.3%
⏱️ Inference time: 0.087s


---

# 🧠 Project Workflow


Image dataset
↓
Dataset cleaning
↓
Pose labeling
↓
Image preprocessing
↓
Model training
↓
Validation evaluation


Training was performed using **GPU on Google Colab**.

---

# 🛠 Tech Stack

Python  
TensorFlow / Keras  
NumPy  
Pillow  
OpenCV  

Infrastructure used during development:

AWS Lambda  
Amazon S3  
DynamoDB  
Google Cloud Vertex AI  
Firebase  

---

# 📁 Repository Structure


fashion-angle-classifier
│
├── README.md
├── demo.py
├── requirements.txt
├── sample_front.jpg
├── sample_back.jpg
├── sample_side.jpg


The trained model is stored in **GitHub Releases** due to file size.

---

# 👤 Author

**Akash Kumar Deep**

Founder of **Picxcale**

AI platform for automated **e-commerce image processing pipelines** handling large-scale visual workflows.

Website:


https://picxcale.com


AI Studio:


https://picxcale.com/studio/


---

# ⭐ If you find this useful

Consider giving the repository a **star ⭐**
