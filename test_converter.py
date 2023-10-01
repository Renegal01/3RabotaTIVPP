import pytest
from converter import Converter


class TestConverter:
    def test_convert_same_unit(self):
        converter = Converter()
        result = converter.convert(10, 'inch', 'inch')
        assert result == 10

    def test_convert_valid_units(self):
        converter = Converter()
        result = converter.convert(10, 'inch', 'cm')
        assert result == 25.4

    def test_convert_invalid_units(self):
        converter = Converter()
        result = converter.convert(10, 'inch', 'unknown')
        assert result is None


if __name__ == '__main__':
    pytest.main()
