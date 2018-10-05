import math

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def getLength(p1,p2):
    length = math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)
    return length


def getArea(p1,p2,p3):
    p1_p2 = getLength(p1,p2)
    p2_p3 = getLength(p2,p3)
    p3_p1 = getLength(p3,p1)
    s = (p1_p2 + p2_p3 +p3_p1)/2
    area = math.sqrt(s*(s-p1_p2)*(s-p2_p3)*(s-p3_p1))
    return area


def main():
    points = []

    for i in range(3):
        x = float(input("x" + str(i+1) + ": "))
        y = float(input("y" + str(i+1) + ": "))
        points.append(Point(x,y))
    
    
    p1 = points[0]
    p2 = points[1]
    p3 = points[2]

    area = getArea(p1,p2,p3)
    print(area)

if __name__ == '__main__':
    main()
