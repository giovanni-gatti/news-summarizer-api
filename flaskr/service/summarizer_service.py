from model.bbc_parser.parser import BBC_Parser
from model.bart_llm.llm_model import BartModel
from model.bart_llm.summarizer_model import Summarizer

def test():
    return BBC_Parser.get_link_name_pairs_categories()

def initialize_summarizer():
    llm = BartModel("./flaskr/model/files/distilbart-onnx")
    return Summarizer(llm)

def get_summary(prompt):
    summarizer = initialize_summarizer()
    return summarizer.summarize(prompt.get("text"))

