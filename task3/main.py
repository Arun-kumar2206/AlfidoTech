import joblib
from fastapi import FastAPI
from pydantic import BaseModel

model = joblib.load('spam_classifier.joblib')

app = FastAPI(title='Email Spam Detection API')

class EmailData(BaseModel):
    email_text: str

@app.get('/')
def read_root():
    return {'message': 'Server running.'}

@app.post('/predict')
def predict_spam(data: EmailData):
    email_text = data.email_text

    prediction = model.predict([email_text])

    if prediction[0] == 1:
        return {'prediction': 'spam'}
    else:
        return {'prediction': 'not spam'}