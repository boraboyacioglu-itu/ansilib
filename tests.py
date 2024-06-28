import unittest
from unittest.mock import patch
from AnsiLib import style, available, color, prints, CHARS

class TestYourModule(unittest.TestCase):

    def test_style_valid(self):
        # Test styling function with valid styles
        bold_style = style('bold')
        self.assertEqual(bold_style("text"), '\x1b[1mtext\x1b[0m')

    def test_style_invalid(self):
        # Test styling function with invalid style
        with self.assertRaises(ValueError):
            style('invalid_style')

    def test_style_non_string_code(self):
        # Test styling function with non-string style code
        with self.assertRaises(TypeError):
            style(123)

    def test_available(self):
        # Test available styles function
        self.assertTrue("bold" in available())
        self.assertTrue("underline" in available())

    def test_color_valid(self):
        # Test color function with valid RGB values
        self.assertEqual(color(255, 0, 0), 'CODE38;2;255;0;0')

    def test_color_invalid_type(self):
        # Test color function with invalid type
        with self.assertRaises(ValueError):
            color(255, 0, 0, type='invalid')

    def test_color_invalid_rgb_type(self):
        # Test color function with non-integer RGB values
        with self.assertRaises(TypeError):
            color(255, '0', 0)

    def test_color_invalid_rgb_range(self):
        # Test color function with out of range RGB values
        with self.assertRaises(ValueError):
            color(256, 0, 0)

    def test_prints(self):
        # Test prints function with valid style
        with patch('builtins.print') as mocked_print:
            prints("text", s='s')
            mocked_print.assert_called_once_with('\x1b[1mtext\x1b[0m', sep=' ', end='\n', file=None, flush=False)

    def test_prints_invalid_style(self):
        # Test prints function with invalid style
        with self.assertRaises(TypeError):
            prints("text", s=123)

if __name__ == '__main__':
    unittest.main()
