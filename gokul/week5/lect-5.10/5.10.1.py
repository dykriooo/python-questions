# ![alt text](image.png)

# sentence="Functions could have no paarameters
# op: 1 29 34 5




def circle(radius):
    area = 3.14 * radius * radius
    perimeter = 2 * 3.14 * radius
    return area, perimeter


def rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


radius = float(input("Enter radius of circle: "))
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))


circle_area, circle_perimeter = circle(radius)
rectangle_area, rectangle_perimeter = rectangle(length, width)


print("Circle Area =", circle_area)
print("Circle Perimeter =", circle_perimeter)

print("Rectangle Area =", rectangle_area)
print("Rectangle Perimeter =", rectangle_perimeter)


