"""Tests for pylitsense.py."""

import unittest
from unittest.mock import patch

from pylitsense.pylitsense import LitSenseResult, PyLitSense


class TestPyLitSense(unittest.TestCase):
    """Tests for the PyLitSense class."""

    @patch("requests.get")
    def test_query(self, mock_get):
        """Tests the query method."""

        mock_response_data = [
            {
                "annotations": ["177|4|gene|2064", "80|4|gene|2064"],
                "pmid": 29163853,
                "text": "Sample text",
                "pmcid": "PMC5685774",
                "section": "INTRO",
                "score": 0.94,
            }
        ]
        mock_get.return_value.json.return_value = mock_response_data
        mock_get.return_value.status_code = 200

        pylitsense = PyLitSense()
        results = pylitsense.query("sample query")

        self.assertEqual(len(results), 1)
        self.assertIsInstance(results[0], LitSenseResult)
        self.assertEqual(results[0].pmid, 29163853)
