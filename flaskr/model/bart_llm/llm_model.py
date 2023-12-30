from optimum.onnxruntime import ORTModelForSeq2SeqLM
from transformers import AutoTokenizer
from langchain.llms.base import LLM
from langchain.callbacks.manager import CallbackManagerForLLMRun
from typing import Any, Optional, List, Mapping
import time


class BartModel(LLM):
    """
    Custom Langchain LLM class
    
    Arguments:

    model_path: (str) Path to the directory where the model is saved or identifier name of pre-trained model to load from cache
    """    

    # system arguments
    model_path:    str = None
    model_context: int = 1024

    # optional model arguments
    min_length:     Optional[int]   = 150
    max_length:     Optional[int]   = 500
    early_stopping: Optional[bool]  = True
    num_beams:      Optional[float] = 4
    length_penalty: Optional[float] = 2.0

    # optional tokenizer arguments
    truncation:          Optional[bool]  = True
    skip_special_tokens: Optional[bool]  = True
    return_tensors:      Optional[str]   = 'pt'

    # model instance
    model:     Any = None
    tokenizer: Any = None

    def __init__(self, model_path):
        super(BartModel, self).__init__()
        self.model_path: str = model_path 
        self.model = ORTModelForSeq2SeqLM.from_pretrained(model_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)

    @property
    def _get_model_default_parameters(self):
        return {
            "min_length": self.min_length,    
            "max_length": self.max_length,  
            "early_stopping": self.early_stopping,
            "num_beams": self.num_beams,       
            "length_penalty": self.length_penalty         
        }
    
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {
            'model_name' : self._llm_type,
            'model_path' : self.model_path,
            **self._get_model_default_parameters
        }
    
    @property
    def _llm_type(self) -> str:
        return "facebook/bart"
    
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        if stop is not None:
            stop = None 
        if run_manager is not None:
            run_manager = None

        model_params = {
            **self._get_model_default_parameters, 
            **kwargs
        }

        start = time.time()
        inputs = self.tokenizer.encode(prompt, return_tensors= self.return_tensors, truncation= self.truncation)
        token_ids = self.model.generate(inputs, **model_params)
        summary = self.tokenizer.decode(token_ids[0], skip_special_tokens= self.skip_special_tokens)
        end = time.time()

        print(end - start)
        return summary

        
        
    
