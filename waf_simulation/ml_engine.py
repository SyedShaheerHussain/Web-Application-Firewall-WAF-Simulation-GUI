# ml_engine.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import OneClassSVM

NORMAL_SAMPLES = [
    "hello user",
    "view profile",
    "product list",
    "search item",
    "contact support"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(NORMAL_SAMPLES)

model = OneClassSVM(gamma="auto")
model.fit(X)

def ml_detect(payload: str) -> bool:
    """Return True if payload is anomalous"""
    X_test = vectorizer.transform([payload])
    return model.predict(X_test)[0] == -1
