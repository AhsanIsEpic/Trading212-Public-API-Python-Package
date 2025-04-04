# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import trading212_api_client
from trading212_api_client.paths.api_v0_equity_pies import get  # noqa: E501
from trading212_api_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiV0EquityPies(ApiTestMixin, unittest.TestCase):
    """
    ApiV0EquityPies unit test stubs
        Fetch all pies  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
