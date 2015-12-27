import random

magnification = 100
sensor_width, sensor_height = 128, 128
line_width = 500
line_period = 1000
number_of_points = 2000

image_width = sensor_width*magnification
image_height = sensor_height*magnification

# create ranges

ranges = []
a = 0
for i in range(sensor_width*magnification/line_period):
    ranges.append((a, a + line_width))
    a += line_period

points = []

for i in range(number_of_points):
    xvalue = 0
    yvalue = 0

    while any(lower <= xvalue <= upper for (lower, upper) in ranges):
        xvalue = random.uniform(0, image_width)
    while any(lower <= yvalue <= lower for (lower, upper) in ranges):
        yvalue = random.uniform(0, image_height)

    points.append([xvalue, yvalue])

f = open("points.txt", 'w')

for point in points:
    f.write(str(point[0]) + ", " + str(point[1]) + ', 0' + '\n')
