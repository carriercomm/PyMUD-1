'''
Created on Dec 23, 2013

@author: jusmith
'''

class Room:
  
  def __init__(self, name, **kwargs):
    
    self.coords = (0,0,0)
    self.name = name
    self.description = "! This room is not described !"
    self.contents = set()
    self.exits = {}
  
  def addObj(self, obj):
    
    self.contents.add(obj)
  
  def removeObj(self, obj):
    
    self.contents.discard(obj)
  
  def getDisplay(self):
    
    output = []
    output.append(self.name)
    
    return "\n".join(output)
