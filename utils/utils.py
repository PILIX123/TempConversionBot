import re


def findTempAndDegree(message: str) -> list[tuple[float, str]] | None:
    v = re.findall(
        r'(-?\d+|\d*[.,]\d+|\d+.\d*)\s*°?\s*(C|F)\b', message, re.IGNORECASE)
    if v == []:
        return None
    return [(float(va[0]), va[1]) for va in v]


def findMentionMilage(message: str) -> list[tuple[float, str]] | None:
    v = re.findall(
        r'(\d+|\d*[.,]\d+|\d+.\d*)\s*(MPG|L\/100KM)\b', message, re.IGNORECASE)
    if v == []:
        return None
    return [(float(va[0]), va[1]) for va in v]
