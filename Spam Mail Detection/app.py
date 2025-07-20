from flask import Flask, request, jsonify, render_template
import joblib
import pickle

app = Flask(__name__)

model = joblib.load("logistic_regression_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['email']
    data_features = vectorizer.transform([data])
    prediction = model.predict(data_features)[0]
    result = 'ham' if prediction == 1 else 'spam'
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
