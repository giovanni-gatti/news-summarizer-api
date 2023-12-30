import requests
from bs4 import BeautifulSoup as bs 
from typing import Tuple, List
import re

class BBC_Parser:

    MAIN_PAGE_URL = "https://www.bbc.com/news"
    WEBSITE_URL = "https://www.bbc.com"

    @classmethod
    def get_text_from_article(cls, url:str) -> str:
        """Parses article and return its text"""
        article = requests.get(url)
        soup = bs(article.content, "html.parser")
        body = soup.find_all("div", {'data-component': 'text-block'})
        text = [p.text for p in body] 
        text = "".join(text)
        return text
    
    @classmethod
    def get_link_name_pairs_categories(cls) -> List[Tuple[str,str]]:
        """Retreives the categories of the news available on BBC and the corresponding path"""
        main_page = requests.get(cls.MAIN_PAGE_URL)

        soup = bs(main_page.content, "html.parser")
        first_tag = soup.find('div', class_ = 'gs-u-display-none gs-u-display-block@m nw-o-news-wide-navigation')
        tags = first_tag.find_all('a', class_ = 'nw-o-link')
        result = [(tag.get_text(), tag.get('href')) for tag in tags if tag and tag.get_text() and tag.get('href')]
        return result[1::]# skipping the first element since it represents the main page
    
    @classmethod
    def get_link_name_pairs_articles_from_main_page(cls) -> List[Tuple[str, str]]:
        """Parses the news articles available on the main page"""
        pattern = re.compile(r'^gs-c-promo-heading')
        page = requests.get(cls.MAIN_PAGE_URL)
        soup = bs(page.content, "html.parser")
        tags = soup.find_all('a',class_ = pattern)
        result = []
        for tag in tags:
            if tag and tag.find('h3') and tag.get('href') and "news" in tag.get('href'):
                result.append((tag.find('h3').get_text(),tag.get('href')))
        
        return result
    
    @classmethod
    def get_link_name_pairs_articles_from_category_url(cls, url: str) -> List[Tuple[str, str]]:
        """Parse the news articles available for a specific category"""
        page = requests.get(url)
        soup = bs(page.content, "html.parser")
        tags = soup.find_all('div', {"type" : "article"})
        result = []
        for tag in tags:
            result.append((tag.find('a').get_text(),tag.find('a').get('href')))
        return result
    
if __name__ == "__main__":
    print(BBC_Parser.get_link_name_pairs_categories())

    
    
    
    

    

    
    

    

