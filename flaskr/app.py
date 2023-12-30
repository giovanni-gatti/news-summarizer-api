import connexion

def create_app():
    app = connexion.FlaskApp(__name__, specification_dir= "./")
    app.add_api("swagger.yml")

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=8000, debug=True)