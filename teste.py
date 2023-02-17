import requests
url = 'http://127.0.0.1:5000/predicao2/'
dados = {
    "sepal length (cm)":0.8,
    "sepal width (cm)":1,
    "petal length (cm)":0.8,
    "petal width (cm)":1
}
response = requests.post(url, json=dados)
response.text