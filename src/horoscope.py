import datetime

from skyfield.api import load, utc
from planets import earth, Planet, get as get_planet, name as name_planet
from zodiac import borders, home

# mars - Pisces Aquarius
# saturn - Aquarius Capricorn
# jupiter - Pisces Aries
# venus - Aries Taurus !
# mercury - Aries Taurus *

# 22-26 04 1168

ts = load.timescale()

horo_planets = [
    Planet.SUN,
    Planet.MOON,
    Planet.MARS,
    Planet.SATURN,
    Planet.JUPITER,
    Planet.VENUS,
    Planet.MERCURY,
    Planet.URANUS,
    Planet.NEPTUNE,
    Planet.PLUTO,
]


def at_date(dt, from_location=None):
    """

    >>> p = at_date(datetime.datetime(2016, 6, 4, 11, 16))
 
    >>> p['sun']
    ('Gemini', 'Taurus Gemini')

    >>> p['moon']
    ('Gemini', 'Taurus Gemini')

    >>> p['mercury']
    ('Taurus', 'Taurus Gemini')

    >>> p['venus']
    ('Gemini', 'Taurus Gemini')

    >>> p['mars']
    ('Scorpio', 'Scorpio Sagittarius')

    >>> p['jupiter']
    ('Virgo', 'Leo Virgo')

    >>> p['saturn']
    ('Sagittarius', 'Scorpio Sagittarius')

    >>> p['uranus']
    ('Aries', 'Aries Taurus')

    >>> p['neptune']
    ('Pisces', 'Aquarius Pisces')

    >>> p['pluto']
    ('Capricorn', 'Capricorn Aquarius')



    >>> p = at_date(datetime.datetime(1168, 4, 26))

    >>> p['mars']
    ('Aquarius', 'Aquarius Pisces')

    >>> p['saturn']
    ('Aquarius', 'Aquarius Capricorn')

    >>> p['jupiter']
    ('Aries', 'Pisces Aries')

    >>> p['venus']
    ('Taurus', 'Aries Taurus')

    >>> p['mercury']
    ('Taurus', 'Aries Taurus')

    """

    # boston = earth.topos('42.3583 N', '71.0603 W')
    dt = dt.replace(tzinfo=utc)
    from_point = earth.at(ts.utc(dt))
    result = {}

    for p in horo_planets:
        position = from_point.observe(get_planet(p)).apparent()
        lat, lon, distance = position.ecliptic_latlon()
        # print name_planet(p), lon.radians
        result[name_planet(p)] = (
            home(lon.radians),
            ' '.join(borders(lon.radians))
        )

    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
