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

2. Navigate to the project directory:

    ```bash
    cd news-summarizer-api

3. (Optional, recommended) Create and activate a virtual environment: 

	```bash
	python -m venv venv 
	source venv/bin/activate
	```

4. Install the required dependencies (using pip):
    ```bash
    make install


### Running the API
Start the API server with the following command (the entrypoint to the application is located in [flaskr/app.py](flaskr/app.py)):
    ```bash
    make run


## API Documentation
The API endpoints are documented using Swagger UI. Once the server is running, you can access the documentation at [http://127.0.0.1:8000/api/ui/](http://127.0.0.1:8000/api/ui/). The documentation is interactive and allows users to directly interact with the endpoints.


## Usage
