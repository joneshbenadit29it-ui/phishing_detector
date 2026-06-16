import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ==========================================
# 1. CREATE MOCK DATASET (If file doesn't exist)
# ==========================================
csv_filename = "emails.csv"

if not os.path.exists(csv_filename):
    print(f"[{csv_filename}] not found. Creating a quick sample dataset for you...")
    sample_data = {
        'text': [
            "URGENT: Your bank account is locked. Click here to verify your identity now!",
            "Dear valued customer, please update your login credentials immediately at http://secure-bank-login.com",
            "Hey, are we still meeting for lunch today at 12:30? Let me know.",
            "Get a free $500 Amazon gift card! Just click this link and enter your SSN.",
            "Attached is the project schedule for Q3 review. Please look it over before the meeting.",
            "Your Netflix subscription renewal failed. Update your credit card here.",
            "Hi Mom, I'll be home late tonight. Don't wait up for dinner.",
            "Congratulations! You won the lottery! Claim your prize money inside."
        ],
        'label': ["Phishing", "Phishing", "Safe", "Phishing", "Safe", "Phishing", "Safe", "Phishing"]
    }
    df = pd.DataFrame(sample_data)
    df.to_csv(csv_filename, index=False)
else:
    # Load your actual dataset here
    df = pd.read_csv(csv_filename)

print("\n--- Dataset Preview ---")
print(df.head())

# ==========================================
# 2. DATA PREPROCESSING & FEATURE EXTRACTION
# ==========================================
X = df['text']   # Features (Email content)
y = df['label']  # Target (Phishing or Safe)

# Split dataset into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text data into numerical features using TF-IDF Vectorizer
# This automatically extracts keywords and evaluates their importance
vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# ==========================================
# 3. TRAIN THE MACHINE LEARNING MODEL
# ==========================================
# Logistic Regression handles text-classification probabilities incredibly well
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# ==========================================
# 4. EVALUATION: ACCURACY & CONFUSION MATRIX
# ==========================================
# Make predictions on the test set
y_pred = model.predict(X_test_tfidf)

# Calculate Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\n==================================")
print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("==================================")

# Detailed Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Generate Confusion Matrix
labels = sorted(list(set(y)))
cm = confusion_matrix(y_test, y_pred, labels=labels)

# Plot the Confusion Matrix using Seaborn
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
plt.title('Phishing Detection - Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.tight_layout()

print("\nDisplaying Confusion Matrix plot... (Close the window to finish execution)")
plt.show()