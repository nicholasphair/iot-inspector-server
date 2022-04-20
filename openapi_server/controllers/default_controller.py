import connexion
import six

from flask import request, current_app

from openapi_server.models.fingerprint import Fingerprint    # noqa: E501
from openapi_server.models.partner import Partner    # noqa: E501
from openapi_server.models.upload import Upload    # noqa: E501
from openapi_server import util

from collections import defaultdict

PEER_TIMEOUT = 3


def generate_user_key():    # noqa: E501
    """Generate a new user key.

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


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
    return 'do some magic!'


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
