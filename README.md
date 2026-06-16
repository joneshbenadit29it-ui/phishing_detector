# 🛡️ Phishing Email Detection Model

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

An intelligent, automated security tool built with **Python** and **Scikit-learn** designed to detect and block malicious phishing attempts before they cause harm. 🚀

---

## 💡 Why This Project?

> **In 2 Lines:** 
> This project builds an automated security tool that uses machine learning to scan text patterns and URLs inside emails to instantly block cyber threats. By sorting scams from safe messages, it protects users from data breaches and identity theft before they ever click a dangerous link.

---

## ✨ Key Features

* **🧠 Smart Dataset Training** – Processes both safe (legitimate) and malicious (phishing) email corpora.
* **🔍 Advanced Feature Extraction** – Leverages **TF-IDF Vectorization** to automatically parse text patterns, urgent keywords, and suspicious URLs.
* **🛡️ Accurate Classification** – Instantly categorizes emails as either **"Phishing"** or **"Safe"** using Machine Learning.
* **📊 Visual Evaluation** – Outputs real-time accuracy scoring and plots a **Confusion Matrix heatmap** to measure precision and recall.

---

## 🛠️ Tech Stack & Libraries

* **Language:** Python 🐍
* **Machine Learning:** Scikit-learn🤖
* **Data Manipulation:** Pandas & NumPy 🐼
* **Data Visualization:** Matplotlib & Seaborn 📊

---

## 🚀 Getting Started (VS Code)

Follow these simple steps to run the model locally in your VS Code environment:

### 1. Clone the Repository
```bash
git clone [https://github.com/joneshbenadit29it-ui/phishing_detector.git](https://github.com/joneshbenadit29it-ui/phishing_detector.git)
cd phishing_detector
2. Install Required Dependencies
Make sure you have your terminal open in VS Code (Ctrl + ~) and run:

Bash
pip install pandas scikit-learn matplotlib seaborn
3. Run the Detection Model
Execute the main script to train and test the model:

Bash
python main.py
🎯 Expected Outcome & Results
Upon running the model, it evaluates the textual features and yields high classification accuracy. A pop-up window will automatically display a beautifully formatted Confusion Matrix Heatmap, allowing you to analyze true positives versus false positives seamlessly.

Output Includes:

📈 Overall Model Accuracy %

📋 Precision, Recall, and F1-Score breakdown

🗺️ Interactive Confusion Matrix Graphic

🧑‍💻 Developed with ❤️ by Jonesh Benadit
