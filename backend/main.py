from . import mainNewsHandler
from . import mainModelSentiment
from . import mainModelFinancial
from . import yfDataProcessor


def setupModelSentiment():
    modelSentiment = mainModelSentiment.instantitateModelSentiment()
    return modelSentiment

def giveAnalysis(companyName, tickerName, modelSentiment,backcandles=30):
    news = mainNewsHandler.handleNewsResponse(companyName)
    resultsSentiment = modelSentiment(news[0])
    data_set_finance = yfDataProcessor.processData(tickerName)
    data_set_finance_scaled = yfDataProcessor.scaleData(data_set_finance)
    X_train, y_train, lastSequence = yfDataProcessor.prerpareDataForLSTM(backcandles, data_set_finance_scaled)
    modelFinance = mainModelFinancial.buildModelFinance(backcandles, data_set_finance)
    modelTrainedFinance = mainModelFinancial.trainModelFinance(modelFinance, X_train, y_train, epochs=40)
    nextDaysPrediction = mainModelFinancial.predictValueFinance(modelTrainedFinance, lastSequence)
    nextDaysValue = yfDataProcessor.inverseTransformer(lastSequence, nextDaysPrediction, data_set_finance)
    last_day_actual = data_set_finance['Adj Close'].values[-1]  
    return news[0], resultsSentiment, nextDaysValue, last_day_actual
