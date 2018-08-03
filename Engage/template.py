from math import pi
def sphere_data():
    '''
    a function that takes the radius of a sphere (a floating-point number) as
    input and outputs the sphere’s diameter, circumference, surface area, and volume.
    '''
    radius = float(input("Enter radius of the sphere."))
    print("Diameter of the sphere is      {}.".format(radius * 2))
    print("Circumference of the sphere is {}.".format(2 * pi * radius))
    print("Surface area of the sphere is {}.".format(4*pi*radius))
    print("volume of the sphere is {}.".format((4/3) * pi * radius))




if __name__ == "__main__":
    sphere_data()




