# Gravitational force is the attractive force that exists between two masses. It can be calculated by using the following formula: GMm/r^2
# where G is the gravitational constant, M and m are the two masses, and r is the distance between them.

# You must implement this equation in Python to calculate the gravitational force between Earth and the moon.

# My solution

G = 6.67 * (10 ** -11)
M = 6.0 * (10 ** 24)  # Mass of Earth
m = 7.34 * (10 ** 22)  # Mass of the moon
r = 3.84 * (10 ** 8)

grav_force = (G * M * m) / (r ** 2)

# Educative solution was exactly the same

