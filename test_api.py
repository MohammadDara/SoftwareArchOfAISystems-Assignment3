# Ref: https://stackoverflow.com/questions/10313001/is-it-possible-to-make-post-request-in-flask
# Ref: https://www.programiz.com/python-programming/json
import pickle
import json
import requests

sample_df = pickle.load(open("resources/samples.pickle", 'rb'))

true_prediction = 0
false_prediction = 0
for index, row in sample_df.iterrows():
    # print(f"{row['conf']}\t{row['title']}")
    dictToSend = {'title' : row['title']}
    res = requests.post('http://localhost:5000/api/predict', json=dictToSend)
    res_dict = json.loads(res.text)
    print(f"predict:{res_dict['prediction']} \t Actual:{row['conf']}")
    if res_dict['prediction'] == row['conf']:
        true_prediction += 1
    else:
        false_prediction += 1

print(f"true_prediction : {true_prediction}")
print(f"false_prediction : {false_prediction}")