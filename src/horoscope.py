from skyfield.api import load
from planets import earth, Planet, get as get_planet


mars = get_planet(Planet.MARS)
ts = load.timescale()
t = ts.now()

boston = earth.topos('42.3583 N', '71.0603 W')
position = earth.at(t).observe(mars).apparent()

ra, dec, distance = position.radec()
lat, lon, distance = position.ecliptic_latlon()

print(ra)
print(dec)
print(distance)
