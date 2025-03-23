
# 📈 Stock-Wise

**Stock-Wise** is a comprehensive web application that performs both **sentiment analysis** and **financial forecasting** on stocks. It combines **real-time news scraping**, **natural language processing (NLP)**, and **technical analysis** to give users actionable insights into stock market trends.

---

## 🚀 Features

- 🔎 **Search by Stock Name or Ticker**  
  Enter a stock name in the search bar to get instant analysis.

- 📰 **Real-Time News Scraping**  
  - Scrapes news from [Pulse by Zerodha](https://pulse.zerodha.com/).  
  - Fetches additional news using [NewsData.io API](https://newsdata.io/).  
  - Aggregates the latest news about the selected stock.

- 🤖 **Sentiment Analysis (FinBERT)**  
  - Uses **FinBERT**, a BERT-based NLP model fine-tuned for financial sentiment analysis.  
  - Classifies news into **Positive**, **Neutral**, or **Negative** sentiments.  
  - Provides sentiment percentages for a clear overview of market sentiment.

- 📊 **Stock Price Prediction (LSTM Model)**  
  - Fetches historical stock data using **yFinance**.  
  - Applies **technical indicators** like EMA, RSI, MACD, and Bollinger Bands.  
  - Uses a custom **LSTM neural network** to predict the **next day's closing price**.  
  - Compares predicted closing price with the current price to forecast **price increase or decrease**.

- 💡 **Combined Insights**  
  Presents both **sentiment** and **financial** analyses on a single dashboard, helping you make informed trading decisions.

---

## 🏗️ How It Works

1. **User Input**  
   - User searches for a stock (e.g., *Tata Motors: TATAMOTORS.NS*).

2. **News Collection**  
   - Scrapes Pulse by Zerodha for the latest news.  
   - Fetches additional articles from NewsData.io API.

3. **Sentiment Analysis**  
   - Aggregated news articles are processed through **FinBERT**.  
   - Each article is classified as Positive, Negative, or Neutral.  
   - Generates sentiment distribution in percentage form.

4. **Financial Forecasting**  
   - Retrieves 2 years of historical data from yFinance.  
   - Calculates technical indicators (EMA, RSI, MACD, Bollinger Bands, etc.).  
   - Feeds processed data into an **LSTM neural network** to predict next day's closing price.

5. **Result Presentation**  
   - Displays **news sentiment**, **financial prediction**, and **detailed news breakdown** in a clean, responsive UI.

---

## 💻 Tech Stack

| Technology    | Description                                   |
|---------------|-----------------------------------------------|
| **Frontend**  | HTML, CSS, Bootstrap 5 (Responsive UI)        |
| **Backend**   | Python, Flask (API and Server Logic)          |
| **Web Scraping** | BeautifulSoup, Requests                   |
| **APIs**      | Zerodha Pulse, NewsData.io, yFinance          |
| **ML Models** | FinBERT (Sentiment), LSTM (Financial Forecast)|
| **Data Processing** | Pandas, NumPy, Scikit-learn             |
| **Deep Learning** | TensorFlow, Keras                         |

---

## 📂 Project Structure

```
├── backend
│   ├── yfDataProcessor.py        # Financial data processing (technical indicators, scaling)
│   ├── pulseNews.py              # Scrapes news from Zerodha Pulse
│   ├── newsAPi.py                # Fetches news from NewsData.io
│   ├── mainNewsHandler.py        # Combines news sources and handles errors
│   ├── mainModelSentiment.py     # FinBERT sentiment analysis model
│   ├── mainModelFinancial.py     # LSTM financial prediction model
│   └── main.py                   # Integration logic for analysis
├── templates
│   ├── temp.html                 # Main frontend page (Search & Display)
├── app.py                        # Flask app (API endpoints, routing)
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/stock-wise.git
cd stock-wise
```

### 2. Create and activate a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

### 5. Access the web app
- Open your browser and visit: `http://127.0.0.1:5000/`

---

## 🛠️ Customization

- **Add More Stocks**: Update the `companyNames` list in `templates/temp.html` with new stock names and tickers.
- **News Sources**: Extend functionality by adding new scraping sources in `backend/pulseNews.py` or `backend/newsAPi.py`.
- **ML Model Enhancements**: Improve the LSTM architecture or retrain FinBERT for custom datasets.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements
- [Zerodha Pulse](https://pulse.zerodha.com/)
- [NewsData.io](https://newsdata.io/)
- [FinBERT by yiyanghkust](https://huggingface.co/yiyanghkust/finbert-tone)
- [yFinance](https://pypi.org/project/yfinance/)
- TensorFlow, Keras, HuggingFace Transformers
