"""
FelipedelosH

Need to grap a prime numbers
"""

from tkinter import *
import math

class Software:
    def __init__(self):
        self.screem = Tk()
        self.canvas = Canvas(self.screem, width=1280, height=720, bg="black")
        self.center = [int(self.canvas['width'])/2, int(self.canvas['height'])/2]
        self.prime = [] # Colection of primes
        self.primes(6666) # Put a primes into array
        self.scale = self.center[0] / len(self.prime) # distance bwwtwen point to point

        self.showScreem()

    def showScreem(self):
        """
        Configure a screem resolution, put elements and show
        """
        self.screem.geometry("1280x720")
        self.screem.title("Prime by felipe")

        self.canvas.place(x=0, y=0)

        # Paint axis
        self.canvas.create_line(0, 360, 1280, 360, fill="red")
        self.canvas.create_line(640, 0, 640, 720, fill="red")

        # Paint primes
        for i in self.prime:
            self.putPointInPlaneXY(i, i)

        self.screem.mainloop()

    def putPointInPlaneXY(self, x, y):
        """
        draw xy pont, (r, o) r e prime N o e rad
        """
        # Calculate a R
        r = self.scale * x
        x = self.center[0] + (r*math.cos(y))
        y = self.center[1] - (r*math.sin(y))
        self.canvas.create_oval(x, y, x+3, y+3, fill="yellow")

    def primes(self, n):
        """
        Return a colection with n primes
        """
        cont = 1
        while len(self.prime) < n:
            if self.isPrime(cont):
                self.prime.append(cont)
            cont = cont + 1


    def isPrime(self, x):
        cont = 0

        if x < 0:
            return False
        elif x == 1 or x == 2:
            return True
        else:
            for i in range(2, x+1):
                if x%i == 0:
                    cont = cont + 1
                    if cont > 1:
                        return False

            if cont == 1:
                return True

s = Software()