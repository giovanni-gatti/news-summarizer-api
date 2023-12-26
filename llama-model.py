from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import LLMChain
from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document

path = "./models/stablelm-zephyr-3b.Q4_K_M.gguf"

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

print("Loading model...")
llm = LlamaCpp(
    model_path       = path,
    n_ctx            = 1024,
    temperature      = 0.3,
    max_tokens       = 2000,
    top_p            = 0.1,
    callback_manager = callback_manager,
    verbose          = True,
)
print("Successfully loaded!")

def generate_prompt():
    chat_template = """
    <|user|>
    Summarize the following news article in a concise way:
    {text}<|endoftext|>
    <|assistant|>
    """
    prompt = PromptTemplate(template= chat_template, input_variables= ["text"])
    return prompt

def summarize(input):
    prompt  = generate_prompt()
    chain   = LLMChain(prompt= prompt, llm= llm)
    summary = chain.run(input)
    return summary

def split_text(input):
    for article in input: 
        splitter = CharacterTextSplitter(separator= '\n', chunk_size= 500, chunk_overlap= 20)
        chunks   = splitter.split_text(article)

        docs = [Document(page_content= t) for t in chunks]


story = """
Once upon a time in the quaint town of Eldoria, nestled between rolling hills and lush meadows, there lived a curious young girl named Lila. With her bright blue eyes and a mop of unruly brown hair, Lila was known for her insatiable curiosity and boundless imagination.

One sunny afternoon, as the golden rays of the sun danced upon the cobblestone streets, Lila discovered a mysterious, dusty old book in the corner of the town's forgotten library. The book, titled "The Enchanted Atlas," beckoned her with its worn leather cover and ornate golden lock. Intrigued, Lila eagerly opened the pages to find a world beyond her wildest dreams.

As she traced her fingers over the pages, an ancient map caught her eye—a map of Eldoria with unexplored territories marked in shimmering ink. Unable to resist the allure, Lila decided to embark on a journey to uncover the secrets hidden in the uncharted lands.

Armed with a backpack filled with snacks, a trusty flashlight, and her favorite red scarf, Lila set out early the next morning. The townsfolk waved her goodbye, some with concern, others with admiration for her adventurous spirit.

The journey was not without challenges. Lila traversed dense forests, crossed bubbling brooks, and climbed towering mountains. Along the way, she encountered magical creatures that had never before been seen in Eldoria. Each encounter brought new lessons and friendships.

As Lila ventured deeper into the uncharted territories, she discovered a hidden valley bathed in the soft glow of bioluminescent flowers. The air was filled with a sweet melody, and the ground beneath her feet seemed to pulse with a gentle energy. In the heart of the valley, Lila uncovered an ancient temple, its entrance guarded by majestic stone statues.

Braving the unknown, Lila entered the temple and found a chamber filled with the soft hum of ancient magic. At the center, she discovered a shimmering portal, its surface rippling like a pool of liquid light. The portal revealed glimpses of distant lands and realms unknown to Eldoria.

With a sense of awe and excitement, Lila stepped through the portal, her heart pounding with anticipation. Little did she know that her journey was just beginning, and that the enchanted atlas held more secrets than she could have ever imagined.

And so, in the mystical realms beyond, Lila's adventures continued, her courage and curiosity lighting the way through unexplored wonders and enchanting landscapes. The story of the girl who dared to venture beyond the known echoed through Eldoria, inspiring generations to come.
"""
summarize(story)