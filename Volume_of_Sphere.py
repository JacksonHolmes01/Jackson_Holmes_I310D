# this file is going to calculate the volume of a sphere
def compute_volume_of_sphere(radius):
    pi = 3.14
    volume = 4/3 * pi * radius * radius
    return volume

radius1 = 40
volume1 = compute_volume_of_sphere(radius1)
print(f"The volume of sphere with radius {radius1} is: {volume1}")

radius2 = 50
volume2 = compute_volume_of_sphere(radius2)
print(f"The volume of sphere with radius {radius2} is: {volume2}")
