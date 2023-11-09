# Ref: https://stackoverflow.com/questions/10313001/is-it-possible-to-make-post-request-in-flask
import pickle

import requests

sample_df = pickle.load(open("resources/samples.pickle", 'rb'))

for index, row in sample_df.iterrows():
    print(f"{row['conf']}\t{row['title']}")
    dictToSend = {'title' : row['title']}
    res = requests.post('http://localhost:5000/api/predict', json=dictToSend)
    print(res.text)