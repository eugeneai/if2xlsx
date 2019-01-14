import re


FUNCS = [
    "ABS",
    "ACCRINT",
    "ACCRINTM",
    "ACOS",
    "ACOSH",
    "ACOT",
    "ACOTH",
    "AGGREGATE",
    "ADDRESS",
    "AMORDEGRC",
    "AMORLINC",
    "AND",
    "ARABIC",
    "AREAS",
    "ASC",
    "ASIN",
    "ASINH",
    "ATAN",
    "ATAN2",
    "ATANH",
    "AVEDEV",
    "AVERAGE",
    "AVERAGEA",
    "AVERAGEIF",
    "AVERAGEIFS",
    "BAHTTEXT",
    "BASE",
    "BESSELI",
    "BESSELJ",
    "BESSELK",
    "BESSELY",
    "BETADIST",
    "BETAINV",
    "BIN2DEC",
    "BIN2HEX",
    "BIN2OCT",
    "BINOMDIST",
    "BINOM.DIST.RANGE",
    "BINOM.INV",
    "BITAND",
    "BITLSHIFT",
    "BITOR",
    "BITRSHIFT",
    "BITXOR",
    "CALL",
    "CEILING",
    "CEILING.MATH",
    "CEILING.PRECISE",
    "CELL",
    "CHAR",
    "CHIDIST",
    "CHISQ.DIST.RT",
    "CHISQ.INV",
    "CHISQ.INV.RT",
    "CHISQ.TEST",
    "CHOOSE",
    "CLEAN",
    "CODE",
    "COLUMN",
    "COLUMNS",
    "COMBIN",
    "COMBINA",
    "COMPLEX",
    "CONCAT",
    "CONCATENATE",
    "CONFIDENCE",
    "CONFIDENCE.T",
    "CONVERT",
    "CORREL",
    "COS",
    "COSH",
    "COT",
    "COTH",
    "COUNT",
    "COUNTA",
    "COUNTBLANK",
    "COUNTIF",
    "COUNTIFS",
    "COUPDAYBS",
    "COUPDAYS",
    "COUPDAYSNC",
    "COUPNCD",
    "COUPNUM",
    "COUPPCD",
    "COVAR",
    "COVARIANCE.S",
    "CRITBINOM",
    "CSCH",
    "CUBEKPIMEMBER",
    "CUBEMEMBER",
    "CUBEMEMBERPROPERTY",
    "CUBERANKEDMEMBER",
    "CUBESET",
    "CUBESETCOUNT",
    "CUBEVALUE",
    "CUMIPMT",
    "CUMPRINC",
    "DATE",
    "DATEDIF",
    "DATEVALUE",
    "DAVERAGE",
    "DAY",
    "DAYS",
    "DAYS360",
    "DB",
    "DBCS",
    "DCOUNT",
    "DCOUNTA",
    "DDB",
    "DEC2BIN",
    "DEC2HEX",
    "DEC2OCT",
    "DECIMAL",
    "DEGREES",
    "DELTA",
    "DEVSQ",
    "DGET",
    "DISC",
    "DMAX",
    "DMIN",
    "DOLLAR",
    "DOLLARDE",
    "DOLLARFR",
    "DPRODUCT",
    "DSTDEV",
    "DSTDEVP",
    "DSUM",
    "DURATION",
    "DVAR",
    "DVARP",
    "EDATE",
    "EFFECT",
    "ENCODEURL",
    "EOMONTH",
    "ERF",
    "ERF.PRECISE",
    "ERFC",
    "ERFC.PRECISE",
    "ERROR.TYPE",
    "EUROCONVERT",
    "EVEN",
    "EXACT",
    "EXP",
    "EXPON.DIST",
    "EXPONDIST",
    "FACTDOUBLE",
    "FALSE",
    "F.DIST",
    "FDIST",
    "FILTER",
    "FILTERXML",
    "FIND",
    "F.INV",
    "F.INV.RT",
    "FINV",
    "FISHER",
    "FISHERINV",
    "FIXED",
    "FLOOR",
    "FLOOR.PRECISE",
    "FORECAST",
    "FORECAST.ETS.SEASONALITY",
    "FORECAST.ETS.STAT",
    "FORECAST.LINEAR",
    "FORMULATEXT",
    "FREQUENCY",
    "F.TEST",
    "FTEST",
    "FVSCHEDULE",
    "GAMMA",
    "GAMMA.DIST",
    "GAMMADIST",
    "GAMMAINV",
    "GAMMALN.PRECISE",
    "GAUSS",
    "GCD",
    "GEOMEAN",
    "GESTEP",
    "GETPIVOTDATA",
    "GROWTH",
    "HARMEAN",
    "HEX2BIN",
    "HEX2DEC",
    "HEX2OCT",
    "HLOOKUP",
    "HOUR",
    "HYPERLINK",
    "HYPGEOM.DIST",
    "HYPGEOMDIST",
    "IFERROR",
    "IFNA",
    "IFS",
    "IMABS",
    "IMAGINARY",
    "IMARGUMENT",
    "IMCONJUGATE",
    "IMCOS",
    "IMCOSH",
    "IMCOT",
    "IMCSC",
    "IMCSCH",
    "IMDIV",
    "IMEXP",
    "IMLN",
    "IMLOG10",
    "IMLOG2",
    "IMPOWER",
    "IMPRODUCT",
    "IMREAL",
    "IMSEC",
    "IMSECH",
    "IMSIN",
    "IMSINH",
    "IMSQRT",
    "IMSUB",
    "IMSUM",
    "IMTAN",
    "INDEX",
    "INDIRECT",
    "INFO",
    "INT",
    "INTERCEPT",
    "INTRATE",
    "IPMT",
    "IRR",
    "ISBLANK",
    "ISERR",
    "ISERROR",
    "ISEVEN",
    "ISFORMULA",
    "ISLOGICAL",
    "ISNA",
    "ISNONTEXT",
    "ISNUMBER",
    "ISODD",
    "ISREF",
    "ISTEXT",
    "ISO.CEILING",
    "ISOWEEKNUM",
    "ISPMT",
    "JIS",
    "KURT",
    "LARGE",
    "LCM",
    "LEFT",
    "LEN",
    "LINEST",
    "LN",
    "LOG",
    "LOG10",
    "LOGEST",
    "LOGINV",
    "LOGNORM.DIST",
    "LOGNORMDIST",
    "LOGNORM.INV",
    "LOOKUP",
    "LOWER",
    "MATCH",
    "MAX",
    "MAXA",
    "MAXIFS",
    "MDETERM",
    "MDURATION",
    "MEDIAN",
    "MID",
    "MIN",
    "MINIFS",
    "MINA",
    "MINUTE",
    "MINVERSE",
    "MIRR",
    "MMULT",
    "MOD",
    "MODE",
    "MODE.SNGL",
    "MONTH",
    "MROUND",
    "MULTINOMIAL",
    "MUNIT",
    "NA",
    "NEGBINOM.DIST",
    "NEGBINOMDIST",
    "NETWORKDAYS.INTL",
    "NOMINAL",
    "NORM.DIST",
    "NORMDIST",
    "NORM.INV",
    "NORMSDIST",
    "NORMSINV",
    "NOW",
    "NPER",
    "NPV",
    "NUMBERVALUE",
    "OCT2BIN",
    "OCT2DEC",
    "OCT2HEX",
    "ODD",
    "ODDFPRICE",
    "ODDFYIELD",
    "ODDLPRICE",
    "ODDLYIELD",
    "OFFSET",
    "OR",
    "PDURATION",
    "PEARSON",
    "PERCENTILE.EXC",
    "PERCENTILE.INC",
    "PERCENTILE",
    "PERCENTRANK",
    "PERMUTATIONA",
    "PHI",
    "PHONETIC",
    "PI",
    "PMT",
    "POISSON.DIST",
    "POISSON",
    "PPMT",
    "PRICE",
    "PRICEDISC",
    "PRICEMAT",
    "PROB",
    "PRODUCT",
    "PROPER",
    "PV",
    "QUARTILE",
    "QUOTIENT",
    "RADIANS",
    "RAND",
    "RANDARRAY",
    "RANDBETWEEN",
    "RANK.AVG",
    "RANK.EQ",
    "RANK",
    "RECEIVED",
    "REGISTER.ID",
    "REPLACE",
    "REPT",
    "RIGHT",
    "ROMAN",
    "ROUND",
    "ROUNDDOWN",
    "ROUNDUP",
    "ROW",
    "ROWS",
    "RRI",
    "RSQ",
    "RTD",
    "SEARCH",
    "SEC",
    "SECH",
    "SECOND",
    "SEQUENCE",
    "SERIESSUM",
    "SHEET",
    "SHEETS",
    "SIGN",
    "SIN",
    "SINGLE",
    "SINH",
    "SKEW",
    "SKEW.P",
    "SLN",
    "SLOPE",
    "SMALL",
    "SORT",
    "SORTBY",
    "SQRT",
    "SQRTPI",
    "STANDARDIZE",
    "STDEV",
    "STDEV.P",
    "STDEV.S",
    "STDEVA",
    "STDEVP",
    "STEYX",
    "SUBSTITUTE",
    "SUBTOTAL",
    "SUM",
    "SUMIF",
    "SUMIFS",
    "SUMPRODUCT",
    "SUMSQ",
    "SUMX2MY2",
    "SUMX2PY2",
    "SUMXMY2",
    "SWITCH",
    "SYD",
    "T",
    "TAN",
    "TANH",
    "TBILLEQ",
    "TBILLPRICE",
    "TBILLYIELD",
    "T.DIST",
    "T.DIST.2T",
    "T.DIST.RT",
    "TDIST",
    "TEXT",
    "TEXTJOIN",
    "TIME",
    "TIMEVALUE",
    "T.INV",
    "T.INV.2T",
    "TINV",
    "TODAY",
    "TRANSPOSE",
    "TREND",
    "TRIM",
    "TRIMMEAN",
    "TRUE",
    "TRUNC",
    "T.TEST",
    "TTEST",
    "UNICHAR",
    "UNICODE",
    "UNIQUE",
    "UPPER",
    "VALUE",
    "VAR",
    "VAR.S",
    "VARA",
    "VARP",
    "VDB",
    "VLOOKUP",
    "WEBSERVICE",
    "WEEKDAY",
    "WEEKNUM",
    "WEIBULL",
    "WORKDAY",
    "WORKDAY.INTL",
    "XIRR",
    "XNPV",
    "XOR",
    "YEAR",
    "YEARFRAC",
    "YIELD",
    "YIELDDISC",
    "YIELDMAT",
    "Z.TEST",
    "ZTEST"
]

FUNCS = set(FUNCS)


def check_func_name(text: str) -> bool:
    rc = text in FUNCS
#    print("FN: '{}'->{}".format(text, rc))
    if rc:
        pass
        #        import pudb
        #        pu.db

    return rc


RE_A = re.compile(r"[$]?[A-Z]+[$]?[0-9]+")


def check_a_selector(text):
    if defined_name(text):
        return False

    if RE_A.match(text):
     #       print("SEL:", text)
        return True
    return False


RE_RC = re.compile(r'[Rr][\[][0-9]+[\]][Cc][\[][0-9]+[\]]')


def check_rc_selector(text):
    if defined_name(text):
        return False

    if RE_RC.match(text):
        #        print("SEL:", text)
        return True
    return False


def defined_name(text):
    return False
