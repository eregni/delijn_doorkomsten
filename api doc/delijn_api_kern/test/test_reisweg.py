"""
    De Lijn Kern Open Data Services (v1)

    Dit document beschrijft de kern operaties van de Open Data API (v1)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import delijn_api_kern
from delijn_api_kern.model.duur import Duur
from delijn_api_kern.model.reisweg_stap import ReiswegStap
globals()['Duur'] = Duur
globals()['ReiswegStap'] = ReiswegStap
from delijn_api_kern.model.reisweg import Reisweg


class TestReisweg(unittest.TestCase):
    """Reisweg unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReisweg(self):
        """Test Reisweg"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Reisweg()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
