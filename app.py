from logging import exception
from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    logging.info("Testing the logging module")
    logging.info("App is started")
    try:
        raise Exception('Demo exception is added')
    except Exception as e:
        housing_exception = HousingException(e, sys)
        logging.info(housing_exception.error_message)
    return '<h1>Hello Flask</h1>'

if __name__ == '__main__':
    app.run(debug=True)
