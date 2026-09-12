# ![alt text](image-3.png)
# - using slope method 
# - create a function slope(x1,y1,x2,y2) to calculate the slope of the line
#     - formula for slope
#         - (y2-y1)/(x2-x1)
#         - if x2-x1 is 0 then the slope is math.inf

# - if slope of any two sides is not equal then it forms a triangle
def trian (x1, y1, x2, y2, x3, y3):
    m1=(y2-y1)/(x2-x1)
    m2=(y3-y2)/(x3-x2)
    if m1 != m2 :
        print("tiangle")
    else :
        print("not triangle")

t=trian(0,0,1,0,0,1)