import pytest
from utils import utils


@pytest.mark.parametrize("maybe_valid, expected_result", [
    ("C", None),
    ("F", None),
    (".", None),
    (".F", None),
    (".C", None),
    (",F", None),
    (",C", None),
    (",", None),
    ("i took out 2 carrots", None),
    ("c", None),
    ("f", None),
    (".5C", [(0.5, "C")]),
    ("10.C", [(10.0, "C")]),
    ("1.72C", [(1.72, "C")]),
    ("3C", [(3.0, "C")]),
    ("3 F", [(3.0, "F")]),
    ("30°C", [(30.0, "C")]),
    ("30 °C", [(30.0, "C")]),
    ("30° C", [(30.0, "C")]),
    ("30 ° C", [(30.0, "C")]),
    ("30°F", [(30.0, "F")]),
    ("30°f", [(30.0, "f")]),
    ("30°c", [(30.0, "c")]),
    ("-1 c", [(-1.0, "c")]),
    ("-1 c 3c", [(-1.0, "c"), (3, "c")]),
])
def test_findTempAndDegree(maybe_valid, expected_result):
    assert utils.findTempAndDegree(maybe_valid) == expected_result
