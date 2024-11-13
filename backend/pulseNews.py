# Web Scrapping Pulse Data

import requests
from bs4 import BeautifulSoup

def get_pulse():
    url = "https://pulse.zerodha.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'identity',
        'Connection': 'keep-alive'
    }
    try:
        session = requests.Session()
        response = session.get(url, headers=headers)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return parse_news_data(response.text)
        
    except requests.exceptions.RequestException as e:
        return -1;

def parse_news_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    print(soup)
    news_container = soup.find('ul', id='news')
    if not news_container:
        return -2;
    news_data = []
    news_items = news_container.find_all('li', class_='box item')
    
    for item in news_items:
        # Get title
        title_tag = item.find('a', {'data-id': True})
        title = title_tag.get_text().strip() if title_tag else ""
        
        # Get description
        desc_div = item.find('div', class_='desc')
        description = desc_div.get_text().strip() if desc_div else ""
        
        # Combine title and description
        if title or description:
            combined_text = f"{title} {description}".strip()
            if combined_text:  # Only add if there's actual content
                news_data.append(combined_text)
        
        # Check for similar news items
        similar_items = item.find_all('li')
        for similar in similar_items:
            similar_title = similar.find('a', class_='title2')
            if similar_title:
                similar_text = similar_title.get_text().strip()
                if similar_text:  # Only add if there's content
                    news_data.append(similar_text)
    print(news_data)
    return news_data

# Example usage
def getResponsePulse(companyName):
    news_list = get_pulse()
    if (news_list == -1):
        return -1 #HTTP Request Failed
    elif (news_list == -2):
        return -2 #No News Found
    finalList = []
    for item in news_list:
        if (companyName in item.lower()):
            finalList.append(item)
    if len(finalList) > 0:
        return finalList
    else:
        return 0 #No News Regarding Given Company Name

if __name__ == "__main__":
    print(len(getResponsePulse("tata")))