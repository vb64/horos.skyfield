from skyfield.api import load

class Planet:

    EARTH = "earth"
    SUN = "sun"
    MOON = "moon"

    SATURN = "saturn BARYCENTER"
    JUPITER = "jupiter BARYCENTER"
    MARS = "mars"
    VENUS = "venus"
    MERCURY = "mercury"

    URANUS = "uranus BARYCENTER"
    NEPTUNE = "neptune BARYCENTER"
    PLUTO = "pluto BARYCENTER"


data = load('de422.bsp')
earth = data[Planet.EARTH]


def name(skyfield_planet):
    """
    >>> name(Planet.JUPITER)
    'jupiter'
    >>> name(Planet.EARTH)
    'earth'
    """
    return skyfield_planet.split()[0]


def get(skyfield_planet):
    """
    >>> get(Planet.VENUS)
    <Body 299 'VENUS' from kernel 'de422.bsp'>
    """
    return data[skyfield_planet]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
