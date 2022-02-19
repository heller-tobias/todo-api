from flask_cors import CORS
import connexion
from waitress import serve
import logging
import logging.config
from os import path
import logging

logging.config.fileConfig(path.join(path.dirname(path.abspath(__file__)), 'logger.conf'))

# Create the application instance
app = connexion.FlaskApp(__name__, specification_dir='./')

# Add Swagger
app.add_api('swagger.yaml')

CORS(app.app)

# TODO: Run on proper webserver
if __name__ == '__main__':
    logging.info("Start Server...")
    serve(app, host='0.0.0.0', port=5001)
    #app.run(host='0.0.0.0', port=5001, debug=True)
