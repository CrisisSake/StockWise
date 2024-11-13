# Using news Data to fetch news https://newsdata.io
# Gives Latest News Delayed By 12 Hours

apiKEy = "pub_35468960b26fdf480e824a9d57ce67e2e01a7"
import requests

def getResponseNewsApi(companyName):
    url = "https://newsdata.io/api/1/latest"
    params = {
        "apikey": apiKEy,
        "qInTitle": companyName,   ###############SHOudl we use q or qinTitle
        "country": "in",
        "language": "en"   
    }

    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        articles = data.get("results", [])
        if (len(articles) <= 0):
            return 0   # No News Regarding Company
        data = []
        for article in articles:
            title = article.get("title", "")
            description = article.get("description", "")
            title_description = f"{title} {description}".strip()
            data.append(title_description)
        return data
    else:
        if response.status_code == 400:
            return -1 #Parameter Missing
        if response.status_code == 401:
            return -2 #Invalid API or No API
        if response.status_code == 403:
            return -3 #IP/Domain restricted
        if response.status_code == 422:
            return -4 #Server Not Understanding Request
        if response.status_code == 429:
            return -5 #Overexcceded Free Api Limit
        if response.status_code == 500:
            return -6 #Internal Server Error