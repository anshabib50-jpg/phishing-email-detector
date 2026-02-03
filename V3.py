import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("emails.csv")  
# columns: text , label (0 legit, 1 phishing)

X = data["text"]
y = data["label"]

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

def predict_email(text):
    vec = vectorizer.transform([text])
    result = model.predict(vec)
    prob = model.predict_proba(vec)

    return result[0], prob[0][1]

#email = input("Paste email:\n")
email = """Your account is suspended, click here to reset your password: http://reset-now.com
"""
result, confidence = predict_email(email)

if result == 1:
    print("Phishing ⚠️")
else:
    print("Legitimate ✅")

print("Confidence:", round(confidence*100,2), "%")
