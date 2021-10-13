from MATH import *


def TESTGOBI():
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
