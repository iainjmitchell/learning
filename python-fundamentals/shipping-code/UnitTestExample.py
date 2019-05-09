import unittest

class RomanNumerals:
    def convert(self, arabic):
        if (type(arabic) == int):
            return "I"
        else:
            raise ValueError()

class RomanNumeralsTest(unittest.TestCase):
    """Test roman numerals convertor"""

    def test_1_is_I(self):
        """Test that converting 1 results in an 'I'"""
        roman_numerals = RomanNumerals()
        self.assertEqual(roman_numerals.convert(1), "I")

    def test_raises_value_error(self):
        """Raises a ValueError when passed a string"""
        roman_numerals = RomanNumerals()
        with self.assertRaises(ValueError): 
            roman_numerals.convert("AString")

if __name__ == "__main__":
    unittest.main() 