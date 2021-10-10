import abc

class Shape(metaclass=abc.ABCMeta):
   @abc.abstractmethod
   def area(self):
      pass
  
class Rectangle(Shape):
   def __init__(self, x,y):
      self.l = x
      self.b=y
   def area(self):
      return self.l*self.b
      
class RoundedRectangle(Shape):
   def __init__(self, x,y):
      self.l = x
      self.b=y
   def area(self):
      return "modifed version of area"
      
      
class AbstractShapeFactory(metaclass=abc.ABCMeta):
   @abc.abstractmethod
   def createShape(self, shapeName):
      pass
      
class NormalShapeFactory(AbstractShapeFactory):
   def createShape(self, shapeName):
       if shapeName == 'RECTANGLE':
          return Rectangle(10, 20)
          
class RoundedShapeFactory(AbstractShapeFactory):
   def createShape(self, shapeName):
       if shapeName == 'RECTANGLE':
          return RoundedRectangle(10, 20)

class FactoryProvider:
    @staticmethod
    def getFactory(factoryType):
         if factoryType == 'SHAPE':
          return NormalShapeFactory()
         if factoryType == 'ROUNDED_SHAPE':
          return RoundedShapeFactory()
       

shapeFactory = FactoryProvider.getFactory("SHAPE")
roundedShapeFactory = FactoryProvider.getFactory("ROUNDED_SHAPE")

rectangle = shapeFactory.createShape('RECTANGLE')
roundedRectangle = roundedShapeFactory.createShape('RECTANGLE')

print ('area: ',rectangle.area())
print ('area: ',roundedRectangle.area())