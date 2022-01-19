import random
from math import *


def GOBI(PARAM: str, *, RETURN_DECIMAL: bool = False) -> float:
    # Remove whitespace
    PARAM = "".join(PARAM.split())
    # Filter out non-text & set lowercase, then seed random
    string = "".join([I for I in PARAM if ord(I) < 256])
    random.seed(hash(string.lower()) or None)
    DECIMAL = random.random()
    return DECIMAL if RETURN_DECIMAL else round(DECIMAL * 100, 2)


def GOBI_DIFF(PARAM1: str, PARAM2: str) -> float:
    return GOBI(PARAM1) - GOBI(PARAM2)


def GOBI_MEAN(*PARAMS: str) -> float:
    return sum([GOBI(PARAM) for PARAM in PARAMS]) / len(PARAMS)


def GOBI_DEGR(PARAM: str) -> float:
    return GOBI(PARAM, RETURN_DECIMAL=True) * 360


def GOBI_RAD(PARAM: str, *, IN_TERMS_OF_PI: bool = True) -> float:
    return 2 * GOBI(PARAM, RETURN_DECIMAL=True) * (pi if IN_TERMS_OF_PI else 1)


def HERON(s1, s2, s3):
    s = (s1 + s2 + s3) / 2
    return sqrt(s * (s - s1) * (s - s2) * (s - s2))


if __name__ == "__main__":
    PARAM0 = "ARMENIUM"
    PARAM1 = "ERNIE"
    print("PARAM0: %s" % PARAM0)
    print("PARAM1: %s" % PARAM1)
    print("")
    print("GOBI_DIFF:", GOBI_DIFF(PARAM0, PARAM1))
    print("GOBI_MEAN:", GOBI_MEAN(PARAM0, PARAM1))
    FUNCS = GOBI, GOBI_DEGR, GOBI_RAD
    for FUNC in FUNCS:
        print("%s:" % FUNC.__name__, FUNC(PARAM0))
