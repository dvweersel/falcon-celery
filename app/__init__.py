from dotenv import load_dotenv
load_dotenv()

import falcon
from falcon_cors import CORS
from app.routes import register_routes


def create_api():
    cors = CORS(allow_all_origins=True)
    api = falcon.API(middleware=[cors.middleware])

    register_routes(api)

    return api
