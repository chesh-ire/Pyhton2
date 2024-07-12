class Polygon:

    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = []

    def inputSides(self):
        for i in range(self.n):
            side = float(input("Enter the length of a side: "))
            self.sides.append(side)

    def dispSides(self):
        for i in range(self.n):
            print(f"Length of side {i + 1} is {self.sides[i]}")

    def findArea(self):
        pass

    def calculatePerimeter(self):
        return sum(self.sides) / 2


class Triangle(Polygon):

    def __init__(self):
        super().__init__(3)

    def findArea(self):
        s = self.calculatePerimeter()
        a, b, c = self.sides
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


# Example usage:
t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()