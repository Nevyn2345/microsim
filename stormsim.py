import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.animation as animation
import time

class Simulator(object):

    def __init__(self):
        
        cameraImg = np.random.normal(100, 1, (256, 256))
        mu, sigma = 100, 1
        photons = 1000

        gauss = np.random.normal(mu, sigma, photons)
        gaussy = np.random.normal(mu, sigma, photons)

        bins = np.linspace(mu-10,mu+10,21)
        digitx = np.digitize(gauss, bins)
        digity = np.digitize(gaussy, bins)
        binary  =  np.bincount(digitx)
        binaryy = np.bincount(digity)


        a = []
        for i in range(len(binary)):
            b = []
            for j in range(len(binaryy)):
                b.append(binary[i] * binaryy[j])
            a.append(b)
        print a

        points = []
        f = open('points.txt', 'r').readlines()
        for line in f:
            line = line.strip('\n')
            line = line.split(',')
            points.append([line[0], line[1]])
        
        implot = plt.imshow(cameraImg, interpolation="nearest", cmap=plt.get_cmap('gray'), extent=[0,1,0,1], aspect='auto')
        plt.ion()
        plt.show()
        while True:
            self.mainloop(points, a, cameraImg, implot)

    def mainloop(self, points, a, cameraImg, implot):
        val = random.randint(0, len(points))
        point = points[val]
        cameraImg = self.updateImage(a, cameraImg, point[0], point[1])
        implot = plt.imshow(cameraImg, interpolation="nearest", cmap=plt.get_cmap('gray'))
        plt.draw()
        plt.pause(0.0001)

    def updateImage(self, a, cameraImg, pointsx, pointsy):
        cameraImg = np.random.normal(100, 1, (256, 256))
        for i in range(len(a)):
            for j in range(len(a[i])):
                cameraImg[round(float(pointsx)/100)+i][round(float(pointsy)/100)+j] += a[i][j]
        return cameraImg


a = Simulator()
