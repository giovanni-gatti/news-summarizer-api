from langchain.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://arxiv.org/pdf/1404.7828.pdf")
data = loader.load()
print(data)