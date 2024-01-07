import connexion
from model.bbc_parser.parser import BBC_Parser
from dotenv import load_dotenv
import os

def create_app():
    app = connexion.FlaskApp(__name__, specification_dir= "./")
    app.add_api("swagger.yml")
    flask_app = app.app

    category_endpoint_map = BBC_Parser.get_link_name_pairs_categories()
    categories = list(category_endpoint_map.keys())
    flask_app.config['CATEGORIES_LIST'] = categories
    flask_app.config['CATEGORIES_ENDPOINT_MAP'] = category_endpoint_map

    flask_app.config['MODEL_PATH'] = os.environ.get("model_path")
    flask_app.config['MODEL_ONNX'] = False if os.environ.get("model_onnx").lower() == "false" else True

    return app

if __name__ == "__main__":
    load_dotenv()
    create_app().run(host="0.0.0.0", port=8000, debug=True)