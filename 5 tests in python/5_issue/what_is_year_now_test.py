import unittest, urllib.request
from unittest.mock import patch
from what_is_year_now import what_is_year_now
import io

class Test_what_is_year_now(unittest.TestCase):
    def test_value_error(self):
        json_date = '{"currentDateTime": "без пятнадцати двенадцать"}'
        with patch.object(urllib.request, "urlopen", return_value=io.StringIO(json_date)):
            with self.assertRaises(ValueError):
                actual_date = what_is_year_now()

    def test_first_type_data(self):
        """
        checks the correctness of execution in the case of the format ymd
        """
        json_date = '{"currentDateTime": "2021-12-31"}'
        with patch.object(urllib.request, "urlopen", return_value=io.StringIO(json_date)):
            actual_date = what_is_year_now()
        expected_date = 2021
        self.assertEqual(actual_date, expected_date)

    def test_second_type_data(self):
        """
        checks the correctness of execution in the case of the format dmy
        """
        json_date = '{"currentDateTime": "31.12.2021"}'
        with patch.object(urllib.request, "urlopen", return_value=io.StringIO(json_date)):
            actual_date = what_is_year_now()
        expected_date = 2021
        self.assertEqual(actual_date, expected_date)

def main(): # pragma: no cover
    pass

if __name__ == '__main__': # pragma: no cover
    unittest.main()
