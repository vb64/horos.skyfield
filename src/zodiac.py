import math


names = [
    "Aries",
    "Taurus",
    "Gemini",
    "Cancer",
    "Leo",
    "Virgo",
    "Libra",
    "Scorpio",
    "Sagittarius",
    "Capricorn",
    "Aquarius",
    "Pisces",
]


def borders(ecliptic_longtitude_radian):
    return []


def borders_degrees(ecliptic_longtitude_degrees):
    """
    >>> borders_degrees(10)
    ["Pisces", "Aries"]
    >>> borders_degrees(20)
    ["Aries", "Taurus"]
    """
    return borders(math.radians(ecliptic_longtitude_degrees))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
