import unittest

class Temperature:
    def __init__(self, kelvin = None, celsius = None, farenheit = None):
        values =  [x for x in [kelvin, celsius, farenheit]if x]

        if len(values) < 1:
            raise ValueError('Need argument')
        if len(values) > 1:
            raise ValueError('Only one argument')
       
        if celsius is not None:
            self.kelvin = celsius + 273.15

        elif farenheit is not None:
            self.kelvin = (farenheit - 32) * 5/9 + 273.15

        else:
            self.kelvin = kelvin
        
        if self.kelvin < 0:
            raise ValueError('Temperature in Kelvin cannot be negative')

    def __str__(self):
        return f'Temperature = {self.kelvin} Kelvins'

class testTemp(unittest.TestCase):
    def test_fail1(self):
        self.assertEqual(Temperature(celsius = 12).kelvin, 20) #Should be fail because the output is incorrect

    def test_success1(self):
        with self.assertRaises(ValueError):
            Temperature()       #Should be success because this will raise a ValueError

    def test_success2(self):
        with self.assertRaises(ValueError):
            Temperature(kelvin=0, celsius=12, farenheit=13)     #Should be success because this will raise a ValueError

    def test_success3(self):
        with self.assertRaises(ValueError):
            Temperature(-1)     #Should be succes because this will raise a ValueError


if __name__ == '__main__':
    unittest.main()