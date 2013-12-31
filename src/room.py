'''
Created on Dec 23, 2013

@author: jusmith
'''

class Room:
  
  def __init__(self, **kwargs):
    
    self.contents = set()
    self.exits = {}
    self.buildSelf(kwargs)

  def buildSelf(self, kwargs):

    coords = kwargs.get("coords")
    name = kwargs.get("name")
    description = kwargs.get("description")
    self.coords = coords if coords else (0, 0, 0)
    self.name = name if name else "! Not Named !"
    self.description = description if description else "! This room is not described !"

  def getStringCoords(self):
    
    return str(self.coords)

  def addObj(self, obj):
    
    self.contents.add(obj)
  
  def removeObj(self, obj):
    
    self.contents.discard(obj)
  
  def getDisplay(self):
    
    output = []
    output.append(self.name)
    
    return "\n".join(output)
