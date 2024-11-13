from mainModelSentiment import instantitateModelSentiment
from mainNewsHandler import handleNewsResponse
from mainModelFinancial import buildModelFinance, trainModelFinance, predictValueFinance
from yfDataProcessor import processData, scaleData, prerpareDataForLSTM, inverseTransformer
companyName = "tata"
tickerName = "MSFT"
backcandles = 30


modelSentiment = instantitateModelSentiment()
news = handleNewsResponse(companyName)
resultsSentiment = modelSentiment(news[0])
print(resultsSentiment)

data_set_finance = processData(tickerName)
data_set_finance_scaled = scaleData(data_set_finance)
X_train, y_train, lastSequence = prerpareDataForLSTM(backcandles, data_set_finance_scaled)
modelFinance = buildModelFinance(backcandles, data_set_finance)
print("Training Data Please Wait")
modelTrainedFinance = trainModelFinance(modelFinance, X_train, y_train, epochs=40)
nextDaysPrediction = predictValueFinance(modelTrainedFinance, lastSequence)
nextDaysValue = inverseTransformer(lastSequence, nextDaysPrediction, data_set_finance)
last_day_actual = data_set_finance['Adj Close'].values[-1]  
print("Last day's actual closing price:", last_day_actual)
print("Predicted next day's closing price:", nextDaysValue)
