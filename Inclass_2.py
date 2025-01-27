# Question 1
#(a)
def anti_diag(n):
    # Create an n x n matrix initialized with zeros
    matrix = [[0] * n for _ in range(n)]
    
    # Fill the anti-diagonal with 1s
    for i in range(n):
        matrix[i][n - i - 1] = 1
    
    return matrix
#(b)
import numpy as np

def anti_diag_2(n):
    # Create an n x n identity matrix
    identity_matrix = np.identity(n)
    
    # Flip the identity matrix left to right
    anti_diag_matrix = np.fliplr(identity_matrix)
    
    return anti_diag_matrix



#(c)
import numpy as np

def anti_diag_3(n):
    # Create an n x n identity matrix
    identity_matrix = np.identity(n)
    
    # Rotate the identity matrix 90 degrees counter-clockwise
    anti_diag_matrix = np.rot90(identity_matrix)
    
    return anti_diag_matrix

#(d)
import numpy as np

def anti_diag_4(n):
    # Create an n x n identity matrix
    identity_matrix = np.identity(n)
    
    # Flip the identity matrix up and down
    anti_diag_matrix = np.flipud(identity_matrix)
    
    return anti_diag_matrix

# Question 2
import numpy as np

def border(m, n):
  
    total_elements = 2 * m + 2 * n - 4
    
    # Create a zero matrix of size m x n
    matrix = np.zeros((m, n), dtype=int)
    
    # Generate the border numbers in clockwise order
    border_numbers = list(range(1, total_elements + 1))
    
    # Fill the top row
    matrix[0, :n] = border_numbers[:n]
    
    # Fill the right column
    matrix[1:m, n-1] = border_numbers[n:n + m - 1]
    
    # Fill the bottom row (in reverse order)
    matrix[m-1, n-2::-1] = border_numbers[n + m - 1:n + m - 1 + n - 1]
    
    # Fill the left column (in reverse order)
    matrix[m-2:0:-1, 0] = border_numbers[-(m-2):]
    
    return matrix

# Question 3
#(a)
def transpose(mat):
    # Use list comprehension to create the transpose
    transposed = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    return transposed

#(b)
import numpy as np

def transpose(mat):
    # Convert the input list to a NumPy array
    mat_array = np.array(mat)
    
    # Use NumPy's transpose method
    transposed = mat_array.transpose()
    
    # Convert back to a Python list
    return transposed.tolist()

# Question 4
#(a)
def dot_prod(l1, l2):
    # Use zip to pair elements of l1 and l2, then calculate the sum of their products
    return sum(a * b for a, b in zip(l1, l2))

#(b)
import numpy as np

def dot_prod(l1, l2):
    # Convert lists to NumPy arrays and calculate the dot product
    return np.dot(l1, l2)

# Question 5
#(a)
def is_u_t(mat):
    
    n = len(mat)
    
    for i in range(1, n):
        for j in range(i):
            if mat[i][j] != 0:  # Check if any entry below the main diagonal is non-zero
                return False
    return True
#(b)
import numpy as np

def is_u_t_n(mat):
    # Check if the matrix is equal to its upper triangular version
    return np.array_equal(mat, np.triu(mat))

# Question 6
import numpy as np

def chessboard(n):
    # Create an n x n matrix of zeros
    board = np.zeros((n, n), dtype=int)
    
    # Fill the board with 1s in alternating positions
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                board[i, j] = 1
                
    return board


# Question 7
def is_toeplitz(mat):
    # Get the number of rows and columns
    rows = len(mat)
    cols = len(mat[0])

    # Check each element below and to the right of the diagonal
    for i in range(1, rows):
        for j in range(1, cols):
            if mat[i][j] != mat[i-1][j-1]:
                return False
    return True