"""
    De Lijn Kern Open Data Services (v1)

    Dit document beschrijft de kern operaties van de Open Data API (v1)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import unittest

import delijn_api_kern
from delijn_api_kern.api.lijnen_api import LijnenApi  # noqa: E501


class TestLijnenApi(unittest.TestCase):
    """LijnenApi unit test stubs"""

    def setUp(self):
        self.api = LijnenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_geef_dienstregeling_voor_lijnrichting(self):
        """Test case for geef_dienstregeling_voor_lijnrichting

        geef de dienstregeling voor de opgegeven lijnrichting  # noqa: E501
        """
        pass

    def test_geef_doorkomst_voor_lijnrichting(self):
        """Test case for geef_doorkomst_voor_lijnrichting

        geef de real-time doorkomsten voor de opgegeven lijnrichting  # noqa: E501
        """
        pass

    def test_geef_gemeenten_voor_lijn(self):
        """Test case for geef_gemeenten_voor_lijn

        geef de gemeenten die bediend worden voor de opgegeven lijn  # noqa: E501
        """
        pass

    def test_geef_geplande_storingen_voor_lijnrichting(self):
        """Test case for geef_geplande_storingen_voor_lijnrichting

        geef de omleidingen voor de opgegeven lijnrichting  # noqa: E501
        """
        pass

    def test_geef_geplande_storingen_voor_lijnrichtingen_lijst(self):
        """Test case for geef_geplande_storingen_voor_lijnrichtingen_lijst

        geef de omleidingen voor de opgegeven lijst van lijnrichtingen  # noqa: E501
        """
        pass

    def test_geef_haltes_voor_lijnrichting(self):
        """Test case for geef_haltes_voor_lijnrichting

        geef de haltes die de door opgegeven lijnrichting worden bediend  # noqa: E501
        """
        pass

    def test_geef_lijn(self):
        """Test case for geef_lijn

        geef een lijn op basis van het opgegeven lijnnummer  # noqa: E501
        """
        pass

    def test_geef_lijn_lijst(self):
        """Test case for geef_lijn_lijst

        geef een lijst van lijnen op basis van een lijst van lijn sleutels  # noqa: E501
        """
        pass

    def test_geef_lijnen(self):
        """Test case for geef_lijnen

        geef alle lijnen  # noqa: E501
        """
        pass

    def test_geef_lijnkleur(self):
        """Test case for geef_lijnkleur

        geef de lijnkleuren voor het opgegeven lijnnummer  # noqa: E501
        """
        pass

    def test_geef_lijnkleur_lijst(self):
        """Test case for geef_lijnkleur_lijst

        geef de lijnkleuren van lijnen op basis van een lijst van lijn sleutels  # noqa: E501
        """
        pass

    def test_geef_lijnrichting(self):
        """Test case for geef_lijnrichting

        geef een lijnrichting voor de opgegeven lijnrichtingcode  # noqa: E501
        """
        pass

    def test_geef_lijnrichtingen(self):
        """Test case for geef_lijnrichtingen

        geef de lijnrichtingen voor het opgegeven lijnnummer  # noqa: E501
        """
        pass

    def test_geef_lijnrichtingen_lijst(self):
        """Test case for geef_lijnrichtingen_lijst

        geef de lijnrichtingen van lijnen op basis van een lijst van lijn sleutels  # noqa: E501
        """
        pass

    def test_geef_on_geplande_storingen_voor_lijnrichting(self):
        """Test case for geef_on_geplande_storingen_voor_lijnrichting

        geef de storingen voor de opgegeven lijnrichting  # noqa: E501
        """
        pass

    def test_geef_on_geplande_storingen_voor_lijnrichtingen_lijst(self):
        """Test case for geef_on_geplande_storingen_voor_lijnrichtingen_lijst

        geef de storingen voor de opgegeven lijst van lijnrichtingen  # noqa: E501
        """
        pass

    def test_geef_rit_voor_lijnrichting(self):
        """Test case for geef_rit_voor_lijnrichting

        geef rit(ten) voor de opgegeven lijnrichting  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
