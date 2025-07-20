📧 Spam Mail Detection using Machine Learning

A simple yet effective spam email classifier built using **TF-IDF** vectorization and **Logistic Regression**. The model takes raw email text input and classifies it as **Spam** or **Ham (Not Spam)**. A red ❌ icon indicates spam, while a green ✅ confirms it is safe (ham).

## 🚀 Features

- Clean and minimal UI for user input.
- Real-time spam classification.
- Visual feedback:
  - ✅ for ham (safe emails)
  - ❌ for spam (malicious/unwanted emails)
- Built using:
  - `scikit-learn` for machine learning
  - `TF-IDF Vectorizer` for feature extraction
  - `Logistic Regression` for classification

## 📊 Model Details

- **Vectorization**: TF-IDF (Term Frequency–Inverse Document Frequency)
- **Classifier**: Logistic Regression
- **Dataset**: Trained on a labeled spam email dataset.

## 🖥️ How It Works

1. User enters the email message in the input box.
2. The model converts the text into a TF-IDF vector.
3. Logistic Regression predicts the label.
4. Output is shown with:
   - ✅ if it's **ham**
   - ❌ if it's **spam**

## 🧠 Tech Stack

- **Python**
- **Flask** (for backend API and web rendering)
- **HTML/CSS/JavaScript** (for frontend)
- **scikit-learn**
- **pandas**, **numpy**

## 📦 Installation

1. Clone the repo:
   https://github.com/crazy-coder-neel/SpamMailDetection

2. To run the project , open the terminal and run app.py as :
   python app.py
