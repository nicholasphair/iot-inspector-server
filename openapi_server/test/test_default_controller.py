# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.upload import Upload  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_generate_user_key(self):
        """Test case for generate_user_key

        Generate a new user key.
        """
        headers = { 
            'Accept': 'text/html',
        }
        response = self.client.open(
            '/generate_user_key',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_submit_data(self):
        """Test case for submit_data

        Upload data to the backend.
        """
        upload = openapi_server.Upload()
        headers = { 
            'Accept': 'text/plain',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/submit_data/{user_key}'.format(user_key='user_key_example'),
            method='POST',
            headers=headers,
            data=json.dumps(upload),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_submit_utc_offset(self):
        """Test case for submit_utc_offset

        Send client's timezone to the server.
        """
        headers = { 
            'Accept': 'text/html',
        }
        response = self.client.open(
            '/submit_utc_offset/{user_key}/{offset_seconds}'.format(user_key='user_key_example', offset_seconds=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
