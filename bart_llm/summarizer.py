from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from typing import List
from bart_llm.llm import BartModel

class Summarizer():
    """
    Custom Summarizer class
    
    Arguments:

    model: (BartModel) BartModel LLM object 
    """ 
    
    chunk_size:    int = 1024
    chunk_overlap: int = 20

    def __init__(self, model: BartModel) -> None:
        self.model = model
        self.chunk_size = model.model_context

    def split_article(self, article:str) -> List[Document]:
        """
        Split single article into chunks and convert them into Langchain Document format
        """
        splitter = RecursiveCharacterTextSplitter.from_huggingface_tokenizer(
            self.model.tokenizer,
            chunk_size = self.chunk_size,
            chunk_overlap = self.chunk_overlap
        )
        chunks = splitter.split_text(article)
        docs = [Document(page_content= t) for t in chunks]

        return docs
    
    def compute_num_tokens(self, text: str) -> int:
        """
        Compute number of tokens in a piece of text
        """
        tokenizer = self.model.tokenizer

        return len(tokenizer.encode(text))

    def summarize(self, article:str) -> str:
        """
        Pre-process and summarize articles
        """
        num_tokens = self.compute_num_tokens(article)
        docs = self.split_article(article)
        if num_tokens < self.model.model_context:
            chain = load_summarize_chain(llm= self.model, chain_type= 'stuff', verbose= True)
        else: 
            chain = load_summarize_chain(llm= self.model, chain_type= 'map_reduce', verbose= True)
        summary = chain.run(docs)

        return summary





    


    
