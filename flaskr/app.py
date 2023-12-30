import connexion
from model.bbc_parser.parser import BBC_Parser


def create_app():
    app = connexion.FlaskApp(__name__, specification_dir= "./")
    app.add_api("swagger.yml")
    flask_app = app.app

    # Now you can set configurations on the Flask app instance
    category_endpoint_map = BBC_Parser.get_link_name_pairs_categories()
    print(category_endpoint_map)
    categories = list(category_endpoint_map.keys())
    print(categories)
    flask_app.config['CATEGORIES_LIST'] = categories
    flask_app.config['CATEGORIES_ENDPOINT_MAP'] = category_endpoint_map
    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=8000, debug=True)