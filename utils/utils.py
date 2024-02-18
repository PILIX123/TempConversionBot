import re


def findTempAndDegree(message: str) -> list[tuple[float, str]] | None:
    v = re.findall(
        r'(-?\d+|\d*[.,]\d+|\d+.\d*)\s*°? ?(C|F)\b', message, re.IGNORECASE)
    if v == []:
        return None
    return [(float(va[0]), va[1]) for va in v]


def findMentionMilage(message: str) -> list[tuple[float, str]] | None:
    v = re.findall(
        r'(\d+|\d*[.,]\d+|\d+.\d*) ?(MPG|L\/100KM)\b', message, re.IGNORECASE)
    if v == []:
        return None
    return [(float(va[0]), va[1]) for va in v]


def findMentionLength(message: str) -> list[tuple[float, str]] | None:
    v = re.findall(
        r'(?<!\/)(?<!1)(?<!0)(?<!0)(-?\d+|\d*[.,]\d+|\d+.\d*) ?(kms?|miles?|kilo(?:meter)?s?|mi|in|inch(?:es)?|cm|centimeters?|ft|foot|feet|meters?|m|yards?|yds?)', message, re.IGNORECASE)
    if v == []:
        return None
    return [(float(va[0]), va[1]) for va in v]
