import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        # TODO - your code here
        det=0
        if self.w==2 and self.h==2:
            det = (self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0])
        if self.w==1 and self.h==1:
            det = self.g[0][0]
        return det
        
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        tr=0
        for i in range(self.h):
            tr+=self.g[i][i]
        return tr

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        inverse=[]
        if self.w==1 and self.h==1:
            row=[]
            row.append((1.0/self.g[0][0]))
            inverse.append(row)
        if self.w==2 and self.h==2:
            det = self.determinant()
            tr = self.trace()
            I = identity(self.h)
            for i in range(self.h):
                row=[]
                for j in range(self.w):
                    row.append((1.0/det)*(tr*I[i][j]-self.g[i][j]))
                inverse.append(row)
        return Matrix(inverse)
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transpose=[]
        if self.w==1 and self.h==1:
            row=[]
            row.append(self.g[0][0])
            transpose.append(row)
        if self.w>=2 and self.h>=2:
            for i in range(self.w):
                row=[]
                for j in range(self.h):
                    row.append(self.g[j][i])
                transpose.append(row)
        return Matrix(transpose)
            
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        Z=zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                Z.g[i][j]=self.g[i][j]+other.g[i][j]
        return Z

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        Z=zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                Z.g[i][j]+=(-1*self.g[i][j])
        return Z

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same")
        Z=zeroes(self.h, self.w)
        for i in range(self.h):
            for j in range(self.w):
                Z.g[i][j]=self.g[i][j]-other.g[i][j]
        return Z

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        def dotProduct(A,B):
            res=0
            for i in range(len(A)):
                res+=A[i]*B[i]
            return res
        
        if self.w != other.h:
            raise(ValueError, "Matrices can only be multiplied if the width of matrix A and height of matrix B are the same")
        
        product = []
        # Take the transpose of matrixB and store the result
        tp = other.T()

        for r1 in range(self.h):
            new_row = []
            for r2 in range(tp.h):
                dp = dotProduct(self.g[r1], tp.g[r2])
                new_row.append(dp)
            # Store the results in the product variable
            product.append(new_row)
        return Matrix(product)
    
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        Z=zeroes(self.h, self.w)
        if isinstance(other, numbers.Number):
            #   
            # TODO - your code here
            #
            for i in range(self.h):
                for j in range(self.w):
                    Z.g[i][j]=other*self.g[i][j]
        return Z
            
            