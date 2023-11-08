import pickle

vec = pickle.load(open("models/vec.pkl", 'rb'))
clf = pickle.load(open("models/clf.pkl", 'rb'))
le = pickle.load(open("models/le.pkl", 'rb'))

def model_predict(email):
    if email == "":
        return ""
    tokenized_email = vec.transform([email])
    prediction = clf.predict(tokenized_email)
    str=le.inverse_transform(prediction)[0]
    return str