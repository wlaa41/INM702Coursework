import numpy as np 

class gridgen():
    def __init__(self,size=(3,3)):
        
        self.width ,self.length= size
        self.grid = self.fillgrid()

    def fillgrid(self, min=0, max=10):

        """ Generate random grid

        Args:
            max (int): maximuim number Execlusive
            min (int): min inclusive

        Returns:
            numpy.array: N*M 2D array
        """
            
        return np.random.randint(min,max, (self.width, self.length))

    def fillnaughty(self):
              
        s = [  [0, 0, 0, 0, 0 ]
              ,[1, 1, 1, 1, 0 ]
              ,[1, 1, 1, 1, 0 ]
              ,[1, 1, 1, 1, 0 ]
              ,[1, 1, 1, 1, 0 ]
        ]
        self.grid = np.array(s)

    def fillreallynaughtyUP(self):
              
        s = [[1 ,9 , 1, 0, 0]
            ,[1 ,9 , 1, 9, 0]
            ,[1 ,1 , 1, 9, 0]
            ,[9 ,9 , 9, 9, 0]
            ,[9 ,9 , 9, 9, 0]
        ]
        self.grid = np.array(s)
    def fillreallynaughtyLEFTUP(self):
              
        s = [ [0, 0 , 0, 0,  0]
             ,[1 ,1 , 9, 1,  0]
             ,[0, 0 , 0, 0,  0]
             ,[0, 1 , 9, 1,  1]
             ,[0, 0,  0, 0,  0]
        ]
        self.grid = np.array(s)

if __name__ == "__main__":
    d = gridgen()
    print(d.grid)

    
    
