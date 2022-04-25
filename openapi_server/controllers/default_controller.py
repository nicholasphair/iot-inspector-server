import connexion
import six

from flask import request, current_app, jsonify, send_file, abort
from openapi_server.models.client import Client    # noqa: E501
from openapi_server.models.fingerprint import Fingerprint    # noqa: E501
from openapi_server.models.partner import Partner    # noqa: E501
from openapi_server.models.upload import Upload    # noqa: E501
from openapi_server import util

from collections import defaultdict

PEER_TIMEOUT = 3


def clients():    # noqa: E501
    """List all connected clients and if they are free for computation.

     # noqa: E501


    :rtype: List[Client]
    """
    clients = current_app.config['connection_manager'].clients()
    clients = [Client(k, v[0], v[1]) for k, v in clients]
    return jsonify(clients)


def generate_user_key():    # noqa: E501
    """Generate a new user key.

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def get_model():    # noqa: e501
    """return the latest version of the model. 

     # noqa: e501


    :rtype: file
    """
    mmanager = current_app.config['model_manager']
    if not mmanager.model_available():
        abort(404)

    path = mmanager.path
    return send_file(path, attachment_filename='model.pt', mimetype='application/octet-stream')


def heart_beat():    # noqa: E501
    """send a heartbeat to the server to let it know we are connected.

     # noqa: E501


    :rtype: str
    """
    ip = request.remote_addr
    print(ip)
    current_app.config['connection_manager'].refresh(ip)
    return 'OK'


def home():    # noqa: E501
    """displays consent page

     # noqa: E501


    :rtype: str
    """
    return 'do some magic!'


def partner():    # noqa: E501
    """Ask the server for a partner to compute with.

     # noqa: E501


    :rtype: Partner
    """
    na = current_app.config['connection_manager'].next_available()
    return Partner(bool(na), na)


def separate():    # noqa: E501
    """Tell the server you have disconnected from your partner. A client should send this after a secure computation is complete. 

     # noqa: E501


    :rtype: Partner
    """
    ip = request.remote_addr
    current_app.config['connection_manager'].separate(ip)
    return 'OK'


def submit_data(user_key, upload=None):    # noqa: E501
    """Upload data to the backend.

     # noqa: E501

    :param user_key: the current user&#39;s key
    :type user_key: str
    :param upload: 
    :type upload: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        upload = Upload.from_dict(connexion.request.get_json())    # noqa: E501
    print(upload)
    # client_action = {start_fast_arp_discovery, quit} U {}
    # ui_last_active_ts = int
    # status = 'status'
    # inspected_devices = []
    resp = {'status': 'success', 'inspected_devices': []}
    return resp


def submit_fingerprint(user_key, fingerprint=None):    # noqa: E501
    """Upload device fingerprints to the backend.

     # noqa: E501

    :param user_key: the current user&#39;s key
    :type user_key: str
    :param fingerprint: 
    :type fingerprint: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        fingerprint = Fingerprint.from_dict(connexion.request.get_json())    # noqa: E501
    print(fingerprint)
    return 'do some magic!'


def submit_model(body=None):    # noqa: E501
    """Clients send updated model. 

     # noqa: E501

    :param body: 
    :type body: str

    :rtype: str
    """
    mmanager = current_app.config['model_manager']
    mmanager.save_model(body)
    return 'OK'


def submit_utc_offset(user_key, offset_seconds):    # noqa: E501
    """Send client&#39;s timezone to the server.

     # noqa: E501

    :param user_key: the current user&#39;s key
    :type user_key: str
    :param offset_seconds: The user&#39;s utc offset in seconds.
    :type offset_seconds: int

    :rtype: None
    """
    try:
        int(offset_seconds)
        return 'SUCCESS'
    except ValueError:
        pass
    return 'ERROR: Invalid offset_seconds.'


def user_user_key(user_key):    # noqa: E501
    """na

     # noqa: E501

    :param user_key: the current user&#39;s key
    :type user_key: str

    :rtype: None
    """
    return 'do some magic!'
