import connexion
import six

from openapi_server.models.upload import Upload    # noqa: E501
from openapi_server import util


def generate_user_key():    # noqa: E501
    """Generate a new user key.

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def home():    # noqa: E501
    """root debug page

     # noqa: E501


    :rtype: str
    """
    return f'iot-inspector debug backend'


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
    return f'received {upload}'


def submit_utc_offset(user_key, offset_seconds):    # noqa: E501
    """Send client&#39;s timezone to the server.

     # noqa: E501

    :param user_key: the current user&#39;s key
    :type user_key: str
    :param offset_seconds: The user&#39;s utc offset in seconds.
    :type offset_seconds: int

    :rtype: None
    """
    return f'received {offset_seconds}'
