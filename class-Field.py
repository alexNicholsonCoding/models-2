# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 12:10:15 2021

@author: Alex
"""

class Location(object):
    """This is a location in two dimensions"""
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
        
    def move(self,deltaX, deltaY):
        """deltaX and deltaY are floats
        delta means the amount you move"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    """getters"""
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def distFrom(self, other):
        """Returns distance from origin
        using Pythagoras' theorem"""
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5
    
class Field(object):
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunkd:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk no in field')
        return self.drunks[drunk]
    