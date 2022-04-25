#!/usr/bin/env python3

import connexion

from openapi_server import encoder
from openapi_server.client_connection_manager import ClientConnectionManager
from openapi_server.model_manager import ModelManager


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml', arguments={'title': 'IOT-Inspector-Server'}, pythonic_params=True)

    manager = ClientConnectionManager()
    model_manager = ModelManager()

    flask_app = app.app
    flask_app.config['connection_manager'] = manager
    flask_app.config['model_manager'] = model_manager

    manager.start()
    app.run(port=8080)
    manager.cancel()


if __name__ == '__main__':
    main()
