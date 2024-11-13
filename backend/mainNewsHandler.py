from . import newsAPi
from . import pulseNews

def handleNewsResponse(companyName):
    
    newsApiResponse = newsAPi.getResponseNewsApi(companyName)
    pulseResponse = pulseNews.getResponsePulse(companyName)
    
    responseMessage1 = ""
    responseMessage2 = ""

    # Handling NewsApiResponse Codes
    if  newsApiResponse == -1:
        responseMessage1 = "Parameter Missing"
    elif newsApiResponse == -2:
        responseMessage1 =  "Invalid API or No API"
    elif newsApiResponse == -3:
        responseMessage1 = "IP/Domain restricted"
    elif newsApiResponse == -4:
        responseMessage1 = "Server Not Understanding Request"
    elif newsApiResponse == -5:
        responseMessage1 = "Overexcceded Free Api Limit"
    elif newsApiResponse == -6:
        responseMessage1 = "Internal Server Error"
    elif newsApiResponse == 0:
        responseMessage1 = "No News Found"
        newsApiResponse = []
    
    if  pulseResponse == -1:
        responseMessage2 = "HTTP Request Failed"
    elif pulseResponse == -2:
        responseMessage2 = "No News Found on PULSE (Issue on Pulse)"
        pulseResponse = []
    elif pulseResponse == 0:
        responseMessage1 = "No News Found"
        pulseResponse = []
    print(newsApiResponse)
    print(pulseResponse)
    finalNews = newsApiResponse + pulseResponse
    return finalNews, responseMessage1, responseMessage2