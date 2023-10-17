from core.settings import FLASK_DEBUG, FLASK_HOST, FLASK_PORT
from routes import create_app


app = create_app()

if __name__ == "__main__":
    app.run(debug=FLASK_DEBUG, host=FLASK_HOST, port=FLASK_PORT)
