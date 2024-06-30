from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from transformers import pipeline

app = Flask(__name__,template_folder='templates')

# Load sentiment analysis model
path = "C:/Users/LENOVO/Downloads/Documents/coding/model"
sentiment_analyzer = pipeline("sentiment-analysis", model=path, tokenizer=path)

# Load dataset
#dataset = pd.read_csv('data/Twitter_Sentiment.csv')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        sentiment = sentiment_analyzer(text)[0]['label']
        accuracy = sentiment_analyzer(text)[0]['score']
        return render_template('result.html', sentiment=sentiment, accuracy=accuracy)
    return render_template('predict.html')

@app.route('/visualization')
def visualization():
    return render_template('visualization.html')

@app.route('/read_dataset')
def dataset():
    filename = 'data/Twitter_Sentiment.csv' 
    data = pd.read_csv(filename, header=0) 
    myData = data.values 
    return render_template('read_dataset.html', myData=myData)

if __name__ == '__main__':
    app.run(debug=True)
