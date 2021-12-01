import unittest
from one_hot_encoder import fit_transform


class TestFT(unittest.TestCase):
    def test_all_features_are_different(self):
        """
        checks if the method works correctly if all arguments are different.
        """
        actual = fit_transform(['Alpha', 'Beta', 'Gamma', 'Delta'])
        expected = [('Alpha', [0, 0, 0, 1]),
                    ('Beta', [0, 0, 1, 0]),
                    ('Gamma', [0, 1, 0, 0]),
                    ('Delta', [1, 0, 0, 0])]
        self.assertEqual(actual, expected)

    def test_some_features_are_equal(self):
        """
        checks if the method works correctly if there are identical arguments.
        """
        actual = fit_transform(['Alpha', 'Alpha', 'Alpha', 'Delta'])
        expected = [('Alpha', [0, 1]),
                    ('Alpha', [0, 1]),
                    ('Alpha', [0, 1]),
                    ('Delta', [1, 0])]
        self.assertEqual(actual, expected)

    def test_ft_returns_list(self):
        """
        checks if the method returns a list object.
        """
        actual = fit_transform(['Alpha', 'Beta', 'Gamma'])
        self.assertIsInstance(actual, list)

    def test_at_least_one_arg(self):
        """
        checks if an exception is thrown when the method
        is called with no arguments.
        """
        with self.assertRaises(TypeError) as context:
            actual = fit_transform()


if __name__ == '__main__':
    unittest.main()
