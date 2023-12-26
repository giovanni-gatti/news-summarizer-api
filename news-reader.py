from newsdataapi import NewsDataApiClient
import config

api = NewsDataApiClient(apikey= config.news_api_key)

response = api.news_api(
    timeframe    = 48,  
    language     = 'en', 
    domainurl    = 'bbc.com',
    full_content = True,
    size         = 5
    )['results']

titles   = [article['title'] for article in response] 
contents = [article['content'] for article in response]
print(titles)
print(contents)