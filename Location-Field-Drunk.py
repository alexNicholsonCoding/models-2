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
    
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
    
    
class Field(object):
    """The location of the drunk is an attribute 
    of the Field; NOT an attribute of the Drunk.
    This means two Drunks cannot occupy the same place
    """
   
    """Drunks are keys in a dict
    Therefore the type Drunk will have to be hashable"""
    def __init__(self):
        self.drunks = {}
        
        
    def addDrunk(self, drunk, loc):
        """Checks if the drunk is already in the field.
        """
        if drunk in self.drunks: #Example of 'Defensive Programming'
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk no in field')
        return self.drunks[drunk]
    
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Location to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named ' + self.name
    
    
import random

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.0),(0.0,-1.0),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)
    
class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,0.9),(0.0,-1.1),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)