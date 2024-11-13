import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def downloadData(tickerName):
    try:
        data = yf.download(tickers=tickerName, period='2y', interval='1d', threads=True)
        return data
    except:
        return -1
    
def processData(tickerName):
    data = downloadData(tickerName)
    # Adding technical indicators
    data['EMAF'] = data['Close'].ewm(span=50, adjust=False).mean()
    data['EMAM'] = data['Close'].ewm(span=100, adjust=False).mean()
    data['EMAS'] = data['Close'].ewm(span=150, adjust=False).mean()
    data['RSI'] = 100 - (100 / (1 + data['Close'].pct_change().rolling(14).mean()))
    data['MACD'] = data['Close'].ewm(span=12, adjust=False).mean() - data['Close'].ewm(span=26, adjust=False).mean()
    data['Bollinger_Upper'] = data['Close'].rolling(window=20).mean() + (data['Close'].rolling(window=20).std() * 2)
    data['Bollinger_Lower'] = data['Close'].rolling(window=20).mean() - (data['Close'].rolling(window=20).std() * 2)
    data['TargetNextClose'] = data['Adj Close'].shift(-1)
    data.dropna(inplace=True)
    data.reset_index(inplace=True)

    # Selecting features for the model
    data = data[['Open', 'High', 'Low', 'Adj Close', 'EMAF', 'EMAM', 'EMAS', 'RSI', 'MACD', 'Bollinger_Upper', 'Bollinger_Lower', 'TargetNextClose']]
    data_set = data.iloc[:, :-1]   # Exclude target column from features
    return data_set

def scaleData(data_set):
    #Scaling Data between 0 and 1
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_set_scaled = scaler.fit_transform(data_set)
    return data_set_scaled

def prerpareDataForLSTM(backcandles, data_set_scaled):
    X = []
    y = []

    for i in range(backcandles, len(data_set_scaled)):
        X.append(data_set_scaled[i-backcandles:i, :])
        y.append(data_set_scaled[i, -1])

    X, y = np.array(X), np.array(y)
    y = y.reshape(-1, 1)

    last_sequence = data_set_scaled[-backcandles:]
    last_sequence = np.expand_dims(last_sequence, axis=0)
    return X, y, last_sequence

def inverseTransformer(last_sequence, next_day_prediction, data_set):
    last_sequence_for_scaling = np.copy(last_sequence[0]) 
    last_sequence_for_scaling = np.vstack([last_sequence_for_scaling, last_sequence_for_scaling[-1]])
    last_sequence_for_scaling[-1, -1] = next_day_prediction[0, 0]
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler.fit_transform(data_set)
    next_day_prediction = scaler.inverse_transform(last_sequence_for_scaling)[-1, -1]
    return next_day_prediction