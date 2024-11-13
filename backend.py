from mainModelSentiment import instantitateModelSentiment
from mainNewsHandler import handleNewsResponse
from mainModelFinancial import buildModelFinance, trainModelFinance, predictValueFinance
from yfDataProcessor import processData, scaleData, prerpareDataForLSTM, inverseTransformer
companyName = "Micrsoft"
tickerName = "MSFT"
backcandles = 30


# modelSentiment = instantitateModelSentiment()
# news = handleNewsResponse(companyName)
# resultsSentiment = modelSentiment(news[0])

data_set_finance = processData(tickerName)
if (data_set_finance == -1):
    print("Problem With Downloading Data from YFinance")
data_set_finance_scaled = scaleData(data_set_finance)
X_train, y_train, lastSequence = prerpareDataForLSTM(data_set_finance_scaled, backcandles)
modelFinance = buildModelFinance(backcandles, data_set_finance)
print("Training Data Please Wait")
modelTrainedFinance = trainModelFinance(modelFinance, X_train, y_train)
nextDaysPrediction = predictValueFinance(modelTrainedFinance, lastSequence)
nextDaysValue = inverseTransformer(lastSequence, nextDaysPrediction)
print("Predicted next day's closing price:", nextDaysValue[0])
