import time
from flask import Flask, request, jsonify, render_template
from backend import main

app = Flask(__name__)
def myFxn(text):
    return (text+"is gay")

@app.route('/')
def index():
    return render_template('temp.html')


def calculate_sentiment_percentages(classifications):
    total = len(classifications)
    sentiment_counts = {
        'Neutral': 0,
        'Negative': 0,
        'Positive': 0
    }
    for item in classifications:
        label = item['label']
        sentiment_counts[label] += 1
    sentiment_percentages = {
        sentiment: (count / total) * 100 
        for sentiment, count in sentiment_counts.items()
    }
    return sentiment_percentages

def combine_sentences_labels(sentences, labels):
    pairs = []
    for sentence, label_dict in zip(sentences, labels):
        label = label_dict['label']
        pairs.append(f"{sentence};;;{label}")
    return "<><>".join(pairs)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    text = data.get('query', '')
    if (len(text) < 3):
        return jsonify("Invalid Search")
    if (":" not in text):
        return jsonify("No Ticker Name Provided")
    companyName, tickerName = text.split(":")
    try:
        news, resultsSentiment, nextDaysValue, last_day_actual = main.giveAnalysis(companyName, tickerName, sentimentModel)
        sentimentPercentages = calculate_sentiment_percentages(resultsSentiment)
        newsLabels = combine_sentences_labels(news, resultsSentiment)
        nextDayBinary = int((nextDaysValue - last_day_actual))
        result = [sentimentPercentages, newsLabels, nextDayBinary]
        return jsonify(result)
    except:
        return jsonify("Some Error Occured")
    

if __name__ == '__main__':
    global sentimentModel
    sentimentModel = main.setupModelSentiment()
    app.run(debug=True)