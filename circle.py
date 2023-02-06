class circle:
    def findCircum(self, rad):
        return 2 * 3.14 * rad

print("Enter Radius of Circle: ", end="")
r = float(input())

ob = circle()
c = ob.findCircum(r)

print("\nCircumference = {:.2f}".format(c))

class pie:
    def area(self, rad):
        return  3.14 * rad**2

print("Enter Radius of Circle: ", end="")
r = float(input())

ob = pie()
c = ob.area(r)

print("\nCircumference = {:.2f}".format(c))

