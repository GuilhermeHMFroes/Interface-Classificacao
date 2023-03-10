from flask import Flask, request, render_template, redirect, url_for, session
import pickle


modelo = pickle.load(open('models/modelo-iris.pkl','rb'))


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html',titulo="Previsão")


@app.route('/soma/<int:valor>')
def soma(valor):
    return "Resultado: {}".format(valor+5)


@app.route('/predicao/<float:v1>/<float:v2>/<float:v3>/<float:v4>')
def predicao(v1,v2,v3,v4):
    resultado = modelo.predict([[v1,v2,v3,v4]])
    return "Classe: {}".format(resultado)


@app.route('/predicao2/',methods=['POST'])
def predicao2():
    dados = request.get_json()
    colunas = ['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']
    dados_input = [dados[col] for col in colunas]
    result = modelo.predict([dados_input])
    return "Classe: {}".format(result)

@app.route('/predicaoform',methods=['POST'])
def form():
    sepall = request.form['sepall']
    sepalw = request.form['sepalw']
    petall = request.form['petall']
    petalw = request.form['petalw']
    result = modelo.predict([[sepall,sepalw,petall,petalw]])
    if result[0]==0:
        resultado='Iris setosa'
    elif result[0]==1:
        resultado='Iris versicolour'
    else:
        resultado='Iris virginica'


    return render_template('resultado.html',titulo="Previsão", resultado=resultado)


app.run(debug=True)

