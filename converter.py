class Converter:
    def __init__(self):
        self.conversion_rates = {
            'inch': {'cm': 2.54, 'foot': 0.0833333},
            'cm': {'inch': 0.393701, 'foot': 0.0328084},
            'foot': {'inch': 12, 'cm': 30.48}
        }

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value

        try:
            rate = self.conversion_rates[from_unit][to_unit]
            converted_value = value * rate
            return converted_value
        except KeyError:
            return None
