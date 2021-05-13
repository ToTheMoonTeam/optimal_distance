from flask import Flask, jsonify, request
from example_find_path import get_path_len

import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def no_request_argument_provided_error(argument):
    error_msg = f"failed: missed {argument} argument in request"
    logger.error(error_msg)
    resp = jsonify({"body": error_msg})
    resp.status_code = 400
    return resp


lon_1 = 60.01774
lat_1 = 30.23169


@app.route('/')
def hello_world():
    request_keys = ["target_lon", "target_lat", "material", "transport_type"]
    for item in request_keys:
        if item not in request.args:
            return no_request_argument_provided_error(item)
    transport_type = request.args["transport_type"]
    if transport_type == "1":
        koeff = 1
    elif transport_type == "2":
        koeff = 2
    elif transport_type == "3":
        koeff = 3
    else:
        koeff = 1
    material_price = 0 * 0

    price = material_price + \
            get_path_len(lon_1, lat_1, float(request.args["target_lon"]), float(request.args["target_lat"])) * \
            koeff

    return price
