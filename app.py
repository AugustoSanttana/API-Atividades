from atividades.controller import atividades_blueprint
from config import app

app.register_blueprint(atividades_blueprint)

if __name__ == "__main__":
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"]
    )
    