from model.bbc_parser.parser import BBC_Parser
from model.bart_llm.llm_model import BartModel
from model.bart_llm.summarizer_model import Summarizer
from flask import current_app, abort, jsonify
import re

def get_available_categories():
    """
    Get list of news categories available on the BBC website
    """
    return current_app.config['CATEGORIES_LIST']

def initialize_summarizer():
    """
    Initialize LLM model
    """
    llm = BartModel(current_app.config['MODEL_PATH'], model_onnx= current_app.config['MODEL_ONNX'])
    return Summarizer(llm)

def category_headlines_summaries(category):
    """
    Return a summary of the headline articles for a given news category
    """
    categories_list = current_app.config['CATEGORIES_LIST']
    if category not in categories_list:
        abort(
            406,
            f"The category provided is not valid or does not exist",
        )
    endpoint = current_app.config["CATEGORIES_ENDPOINT_MAP"][category]
    url = BBC_Parser.WEBSITE_URL + endpoint
    article_link_pairs = BBC_Parser.get_link_name_pairs_articles_from_category_url(url)
    summarizer = initialize_summarizer()
    response = []
    for i in range(3):
        title, article_endpoint = article_link_pairs[i]
        article_url = BBC_Parser.WEBSITE_URL + article_endpoint
        text = BBC_Parser.get_text_from_article(article_url)
        summary = summarizer.summarize(text)
        response.append({'title': title, 'url': article_url, 'summary': summary})
    return jsonify(response)

def submit_free_url(url):
    """
    Retrieve article given the url and return its summary
    """
    url = url.get("url")
    summarizer = initialize_summarizer()
    url_pattern = re.compile(r'^https?://(www\.)?bbc\.com/.*$')
    if url_pattern.match(url):
        article = BBC_Parser.get_text_from_article(url)
        if article == "":
            return "Article content not available"
        summary = summarizer.summarize(article)
    else:
        abort(
            406,
            f"The string provided is not a valid BBC Url",
        )
    return summary
    



