import re


def findTempAndDegree(message: str) -> tuple[int, str] | None:
    v = re.search(r'-?(\d+|\d*[.,]\d+|\d+.\d*)\s*°?\s*(C|F|c|f)\b', message)
    if v == None:
        return None
    return (int(v.groups()[0]), v.groups()[1])
