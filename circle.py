class circle:
    def findCircum(self, rad):
        return 2 * 3.14 * rad

print("Enter Radius of Circle: ", end="")
r = float(input())

ob = circle()
c = ob.findCircum(r)
print("\nCircumference = {:.2f}".format(c))