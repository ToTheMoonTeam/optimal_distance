from flask import Flask, jsonify, request
from example_find_path import get_path_len
from flask_cors import CORS
import logging

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})


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

shops = [
    {
        "name": "Карьер Дачное",
        "lon_1": 59.778673,
        "lat_1": 30.976736,
        "products": {"песок": 170, "супесь": 100},
        "contact": "89213238747, Заффор",
    },
    {
        "name": "Карьер Приморское шоссе",
        "lon_1": 60.176215,
        "lat_1": 29.324035,
        "products": {"песок": 190, "супесь": 90},
        "contact": "7921-924-67-37, 905-45-35",
    }
]


def koeff_from_transport_type(transport_type):
    # самосвала 20м3
    if transport_type == "1":
        return 10
    # самосвала 10м3
    elif transport_type == "2":
        return 20
    else:
        koeff = 1


@app.route('/')
def get_routes():
    request_keys = ["target_lon", "target_lat", "material", "transport_type", "amount"]
    for item in request_keys:
        if item not in request.args:
            return no_request_argument_provided_error(item)

    transport_type = request.args["transport_type"]
    material = request.args["material"]
    amount = int(request.args["amount"])
    k = koeff_from_transport_type(transport_type)
    candidates = []
    for shop in shops:
        if material in shop["products"]:
            final_price = shop["products"][material] * amount + \
                          get_path_len(shop["lon_1"], shop["lat_1"],
                                       float(request.args["target_lon"]), float(request.args["target_lat"])) * k
            response_row = {"final_price": final_price, "contact": shop["contact"], "name": shop["name"]}
            candidates.append(response_row)

    resp = jsonify({
        "body": {
            "shops": sorted(candidates, key=lambda x: x["final_price"], reverse=True)
        }})
    resp.status_code = 200
    return resp


app.run()
