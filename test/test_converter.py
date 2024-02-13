import pytest
from converters import converter


@pytest.mark.parametrize("degreesC, expected_result", [
    (3.0, 37.4),
    (0.5, 32.9),
    (-40.0, -40.0),
    (-40.0, -40.0),
])
def test_celciusToFahrenheit(degreesC, expected_result):
    assert converter.celciusToFahrenheit(degreesC) == expected_result
