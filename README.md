# 🎗️ Breast Cancer Prediction App

An interactive Machine Learning web application built with **Streamlit** and **XGBoost** to classify breast cancer tumors as **Benign (2)** or **Malignant (4)** based on cell feature values.

---

## 🚀 Live Demo

You can access the deployed application here:  
🔗 **[Breast Cancer Prediction Web App](https://data-classification-by-using-xgboost-hwbathwdbxd2m78n7djsgs.streamlit.app/)**

---

## 📌 Project Overview

This project aims to assist in early detection and diagnosis of breast cancer by processing cell feature measurements. The application utilizes an **XGBoost Classifier** model trained on clinical dataset metrics to predict tumor malignancy with calculated confidence scores.

---

## ✨ Features

- **Interactive UI**: Custom sliders in the sidebar for real-time input parameter adjustment.
- **Dynamic Data Display**: Shows a live DataFrame preview of the user's selected parameters.
- **Accurate Prediction**: Powered by an XGBoost Machine Learning model.
- **Confidence Metrics**: Displays probability percentage alongside prediction results (**Benign** or **Malignant**).

---

## 🧬 Dataset Features

The model uses the following cell characteristics (scaled from 1 to 10):

| Feature Name | Description |
| :--- | :--- |
| **Clump Thickness** | Assesses cell layering (1 = single layer, 10 = multi-layered). |
| **Uniformity of Cell Size** | Evaluates consistency in cell size. |
| **Uniformity of Cell Shape** | Evaluates consistency in cell shape. |
| **Marginal Adhesion** | Measures cell adhesion/clustering. |
| **Single Epithelial Cell Size** | Relates to cell enlargement. |
| **Bare Nuclei** | Presence of nuclei unsupported by cytoplasm. |
| **Bland Chromatin** | Textural appearance of nuclear chromatin. |
| **Normal Nucleoli** | Presence/size of small structures within the cell nucleus. |
| **Mitoses** | Rates of cell division. |

---

## 🛠️ Tech Stack & Libraries

- **Language**: Python 3.x
- **Machine Learning**: XGBoost, Pandas
- **Web Framework**: Streamlit
- **Deployment**: Streamlit Community Cloud

```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME
