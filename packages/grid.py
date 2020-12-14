import numpy as np 

class gridgen():
    def __init__(self,size=(5,5)):
        
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
    def fillgridMOREZeros(self, min=0, max=10,morezeroby=4):
        """ Generate random grid with more zeros possibility
        Args:
            max (int): maximuim number Execlusive
            min (int): min inclusive
            morezeroby (int): how many times more probibilty of generating zero
        Returns:
            numpy.array: N*M 2D array
        """
        arr = np.random.randint(min-morezeroby,max, (self.width, self.length))
        # print(arr)f
        arr[arr <0] = 0
        
        return arr
    ############ TESTING ARRAYS ###########
    def easytest(self):
              
        s = [    [0, 0, 0 ]
                ,[1, 1, 2 ]
                ,[1, 1, 0 ]
        ]
        self.grid = np.array(s)    
        return self.grid.shape
        
    def test1(self):
                
        s = [ [0, 1, 0]
             ,[0, 1, 0]
             ,[9, 0, 7]
        ]
        self.grid = np.array(s)    
        return self.grid.shape

    def test2(self):

        s = [ [4, 9, 1, 3]
             ,[0, 0, 7, 1]
             ,[2, 0, 7, 9]
             ,[1, 2, 1, 9]]
        self.grid = np.array(s)
        return self.grid.shape

        
    def fillava(self):

        s = [    [5, 5, 5]
                ,[5, 5, 5]
                ,[5, 5, 5]
                ,[5, 5, 5]]
        self.grid = np.array(s)
        return self.grid.shape




    def jiktest(self):
              
        s = [    [0, 9, 9 ]
                ,[1, 1, 2 ]
                ,[1, 9, 2 ]
        ]
        self.grid = np.array(s)
        return self.grid.shape
        
    def fillnaughty(self):
              
        s = [  [0, 0, 0, 0, 0 ]
              ,[1, 1, 0, 1, 0 ]
              ,[1, 1, 0, 1, 0 ]
              ,[1, 1, 1, 1, 0 ]
              ,[1, 1, 1, 1, 0 ]
        ]
        self.grid = np.array(s)
        return self.grid.shape

    def fillreallynaughtyUP(self):
              
        s = [[1 ,9 , 1, 0, 0]
            ,[1 ,9 , 1, 9, 0]
            ,[1 ,1 , 1, 9, 0]
            ,[9 ,9 , 9, 9, 0]
            ,[9 ,9 , 9, 9, 0]
        ]
        self.grid = np.array(s)
        return self.grid.shape
    def fillreallynaughtyLEFTUP(self):
              
        s = [ [2, 0 , 0, 0,  0]
             ,[3 ,3 , 1, 2,  0]
             ,[0, 0 , 0, 0,  0]
             ,[0, 1 , 9, 1,  1]
             ,[0, 0,  0, 0,  0]
        ]
        self.grid = np.array(s)
        return self.grid.shape

    def fillmaddness(self):
                  
        s = [  [ 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]
             , [ 1, 1, 1, 0, 1, 0, 0, 0, 1, 0]
             , [ 0, 0, 0, 0, 1, 0, 1, 1, 1, 0]
             , [ 0, 1, 1, 1, 1, 0, 0, 1, 0, 0]
             , [ 0, 1, 0, 0, 0, 1, 0, 1, 0, 1]
             , [ 0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
             , [ 0, 1, 0, 1, 0, 0, 0, 1, 1, 0]
             , [ 0, 1, 0, 1, 1, 1, 1, 0, 0, 0]
             , [ 0, 1, 0, 0, 0, 0, 1, 0, 1, 1]
             , [ 0, 1, 1, 1, 1, 0, 1, 0, 1, 0]
             , [ 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]
             
      
        ]
        self.grid = np.array(s)
        return self.grid.shape


if __name__ == "__main__":
    d = gridgen()
    print(d.grid)
    print(d.fillreallynaughtyLEFTUP())
    print(d.fillgridMOREZeros())



    
    
