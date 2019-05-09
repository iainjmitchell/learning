class RomanNumerals:
    def __init__(self, arabic_to_numeral_mappings):
        self._arabic_to_numeral_mappings = arabic_to_numeral_mappings

    def convert(self, arabic):
        if arabic in self._arabic_to_numeral_mappings:
            return self._arabic_to_numeral_mappings[arabic]
        else:
            closest_arabic = self._closest_arabic_number_with_numeral(arabic)
            return self.convert(closest_arabic) + self.convert(arabic-closest_arabic)

    def _closest_arabic_number_with_numeral(self, arabic):
        return next(matching_arabic 
            for matching_arabic 
            in self._arabic_to_numeral_mappings 
            if arabic / matching_arabic >= 1)