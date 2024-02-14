import re


def findTempAndDegree(message: str) -> list[tuple[float, str]] | None:
    v = re.findall(r'(-?\d+|\d*[.,]\d+|\d+.\d*)\s*°?\s*(C|F|c|f)\b', message)
    if v == []:
        return None
    t = [(float(va[0]), va[1]) for va in v]
    return [(float(va[0]), va[1]) for va in v]
