import unittest
from unittest.mock import Mock, patch, MagicMock
from src.Jewishcal import Jewishcal


class MyTestCase(unittest.TestCase):

    @patch('src.Jewishcal.requests.get')
    def test_input_date(self, mockJson):
        jewishcal_data = {"location": {"geo": "none"},
                          "link": "https://www.hebcal.com",
                          "title": "Hebcal February 2000",
                          "date": "2020-03-15T15:44:11-00:00",
                          "items":
                              {"category": "holiday", "hebrew": "בדיקות", "link": "https://www.hebcal.com",
                               "date": "2000-02-02", "title": "testing holiday"}
                          }

        # Configure the mock to return a response with an OK status code. Also, the mock should have
        # a `json()` method that returns.
        mockJson.return_value = Mock(ok=True)
        mockJson.return_value.json.return_value = jewishcal_data
        # assume
        stub = {"month": 2, "year": 2000}

        # expected
        expected_item = {"category": "holiday", "hebrew": "בדיקות", "link": "https://www.hebcal.com",
                         "date": "2000-02-02", "title": "testing holiday"}

        # action
        date_result = Jewishcal.specific_date_holiday(**stub)

        # assert
        self.assertDictEqual(expected_item, date_result)

if __name__ == '__main__':
    unittest.main()
