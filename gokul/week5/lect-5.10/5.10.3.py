# ![alt text](image-2.png)
# - to check if the coordinates form a triangle or not
# - you can use the formula
#     - if the sum of any two sides is greater than the third side then it forms a triangle

# - take 6 inputs from the user as float
#     - x1,y1,x2,y2,x3,y3
# - create a function distance(x1,y1,x2,y2) to calculate the distance between two points

# - formula for distance between two points
#     - sqrt((x2-x1)^2 + (y2-y1)^2)

def trian(x1, y1, x2, y2, x3, y3):
    if x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0:
        print("triangle")
    else:
        print("not a triangle")

t=trian(0,0,0,1,1,0)
# print(t)

def dist (x1, y1, x2, y2):
    distance= ((x2-x1)**2 + (y2-y1)**2)**0.5
    print(distance)

d=dist(1,3,3,2)