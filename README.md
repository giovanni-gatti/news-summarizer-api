# News Summarizer API

This project utilizes Flask, Swagger, and Connexion to create a REST API for obtaining summaries of news articles from the [BBC](https://www.bbc.com/news) website. The API endpoints are defined following the OpenAPI specification and leverage a Language Model (LLM) running in the backend to generate the summaries. The full documentation is available using Swagger UI.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- Pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/giovanni-gatti/news-summarizer-api.git
   ```

2. Navigate to the project directory:

    ```bash
    cd news-summarizer-api
    ```

3. (Optional, recommended) Create and activate a virtual environment: 

	```bash
	python -m venv venv 
	source venv/bin/activate
	```

4. Install the required dependencies (using pip):
    ```bash
    make install
    ```

### Running the API
Start the API server with the following command (the entrypoint to the application is located in [flaskr/app.py](flaskr/app.py)):
```bash
make run
```

## API Documentation
The API endpoints are documented using Swagger UI. Once the server is running, you can access the documentation at [http://127.0.0.1:8000/api/ui/](http://127.0.0.1:8000/api/ui/). The documentation is interactive and allows users to directly play with the endpoints.


## Large Language Model (LLM)
The backend of this application is designed to run on both CPUs and GPUs, leveraging the capabilities of the Hugging Face and LangChain libraries. It is specifically built to support Transformer Encoder-Decoder (Seq2Seq) Models. A wide range of such models is available on the Hugging Face Hub, including small models already finetuned on news data such as:

- [bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn)
- [distilbart-cnn](https://huggingface.co/sshleifer/distilbart-cnn-12-6)

When choosing a model, consider your device specifications, including hardware accelerators and available RAM.
To speed up inference on CPUs, the applications supports models also in ONNX format and allows to run inference with the accelerated ONNX Runtime and graph optimizations. To convert and optimize an Hugging Face model to ONNX format, run the following command from a terminal:

```bash
optimum-cli export onnx --model model_name --optimize O2 --framework pt --task text2text-generation-with-past local_model_folder
```
To customize your model selection when running the application, navigate to the `.env` file and specify the fields appropriately:

```
model_path: either the path to a local directory or the identifier name of a pre-trained model on Hugging Face, to be loaded from cache
model_onnx: set to True if the selected model is in ONNX format
```

## References and Resources
 - [ONNX Runtime](https://onnxruntime.ai/)
 - [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
 - [HuggingFace Documentation](https://huggingface.co/docs)
 - [OpenAPI Specification](https://spec.openapis.org/oas/v3.0.0.html)
