import pandas as pd
import plotly.graph_objs as go
from flask import Flask, render_template, render_template_string, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
@app.route('/', methods=['GET','POST'])
def home():
    return render_template('visual.html')
@app.route('/result',methods = ['POST', 'GET'])
def result():

   if request.method == 'POST':
      result = request.form
      nivel = request.form.get('options')
      afazer = ''
      if nivel == 'Cor':
          data = pd.read_excel('cor01023.xlsx')
          labels = data['legenda']
          values = data['raçacor']

      #fig = go.Figure([go.Bar(x=data['pcd'], y=data['tipodedeficiência'])])
          fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

          return render_template("visual.html",plot=fig.to_html(),nivel=nivel,afazer=afazer)
      if nivel == 'Tipo de Deficiência':
          data = pd.read_excel('pcd.xlsx')
          labels = data['legenda']
          values = data['tipodedeficiência']

      #fig = go.Figure([go.Bar(x=data['pcd'], y=data['tipodedeficiência'])])
          fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
          return render_template("visual.html", plot=fig.to_html(), nivel=nivel, afazer=afazer)

      elif nivel != 'Cor' or nivel != 'Tipo de Deficiência':
            afazer = 'Em Desenvolvimento'
            return render_template("visual.html", afazer=afazer, nivel=nivel)


if __name__ == '__main__':
    app.run(debug=True)