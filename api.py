from flask import Flask
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.flask.flask_middleware import FlaskMiddleware

app = Flask(__name__)

# Configure logging to send to Application Insights
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(
    connection_string="InstrumentationKey=00ca0526-4314-4e5e-b462-9b3d8378f6db;IngestionEndpoint=https://eastus-8.in.applicationinsights.azure.com/"
))
logger.setLevel(logging.INFO)

# Enable middleware to capture all incoming requests automatically
middleware = FlaskMiddleware(app)

@app.route("/hello")
def hello():
    logger.info("Hello endpoint called")
    return {"message": "Hello Azure DevOps!"}

@app.route("/error")
def error():
    try:
        1 / 0
    except Exception as e:
        logger.error("An error occurred: %s", e)
        return {"error": "Something went wrong"}, 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
