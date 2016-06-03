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

sector_num = len(names)
sector = math.pi * 2 / sector_num
delta = sector / 2


def borders(ecliptic_longtitude_radian):

    sector_index = int(ecliptic_longtitude_radian / sector)
    sector_delta = ecliptic_longtitude_radian - sector_index * sector

    if sector_delta == delta:
        return [names[sector_index]]

    s1 = sector_index
    s2 = s1 + 1

    if sector_delta < delta:
        s2 = sector_index
        s1 = s2 - 1

    if s1 < 0:
        s1 = sector_num - 1

    if s1 == sector_num:
        s1 = 0

    if s2 < 0:
        s2 = sector_num - 1

    if s2 == sector_num:
        s2 = 0

    return [names[s1], names[s2]]


def borders_degrees(ecliptic_longtitude_degrees):
    """
    >>> int(round(math.degrees(sector)))
    30
    >>> int(round(math.degrees(delta)))
    15
    >>> borders_degrees(10)
    ['Pisces', 'Aries']
    >>> borders_degrees(20)
    ['Aries', 'Taurus']
    >>> borders_degrees(181)
    ['Virgo', 'Libra']
    >>> borders_degrees(359)
    ['Pisces', 'Aries']
    """
    return borders(math.radians(ecliptic_longtitude_degrees))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
