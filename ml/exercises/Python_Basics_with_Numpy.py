"""
Python Basics with Numpy (optional assignment)

This exercise gives you a brief introduction to Python and NumPy functionality
needed for deep learning.

Instructions:
- You will be using Python 3.
- Avoid using for-loops and while-loops, unless you are explicitly told to do so.
"""

import math
import numpy as np
import time

def basic_sigmoid(x):
    """
    Compute sigmoid of x.

    Arguments:
    x -- A scalar

    Return:
    s -- sigmoid(x)
    """
    s = 1 / (1 + math.exp(-x))
    return s

def sigmoid(x):
    """
    Compute the sigmoid of x

    Arguments:
    x -- A scalar or numpy array of any size

    Return:
    s -- sigmoid(x)
    """
    s = 1 / (1 + np.exp(-x))
    return s

def sigmoid_derivative(x):
    """
    Compute the gradient (also called the slope or derivative) of the sigmoid function with respect to its input x.
    You can store the output of the sigmoid function into variables and then use it to calculate the gradient.
    
    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """
    s = sigmoid(x)
    ds = s * (1 - s)
    return ds

def image2vector(image):
    """
    Argument:
    image -- a numpy array of shape (length, height, depth)
    
    Returns:
    v -- a vector of shape (length*height*depth, 1)
    """
    v = image.reshape(-1, 1)
    return v

def normalize_rows(x):
    """
    Implement a function that normalizes each row of the matrix x (to have unit length).
    
    Argument:
    x -- A numpy matrix of shape (n, m)
    
    Returns:
    x -- The normalized (by row) numpy matrix. You are allowed to modify x.
    """
    x_norm = np.linalg.norm(x, ord=2, axis=1, keepdims=True)
    x = x / x_norm
    return x

def softmax(x):
    """Calculates the softmax for each row of the input x.

    Your code should work for a row vector and also for matrices of shape (m,n).

    Argument:
    x -- A numpy matrix of shape (m,n)

    Returns:
    s -- A numpy matrix equal to the softmax of x, of shape (m,n)
    """
    x_exp = np.exp(x)
    x_sum = np.sum(x_exp, axis=1, keepdims=True)
    s = x_exp / x_sum
    return s

def L1(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L1 loss function defined above
    """
    loss = np.sum(np.abs(yhat - y))
    return loss

def L2(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    
    Returns:
    loss -- the value of the L2 loss function defined above
    """
    loss = np.sum((yhat - y)**2)
    return loss

def demo_vectorization():
    """Demonstrate the performance benefits of vectorization."""
    x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]
    x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]
    W = np.random.rand(3, len(x1))  # Random 3*len(x1) numpy array

    # Non-vectorized implementations
    print("Non-vectorized implementations:")
    
    # Classic dot product
    tic = time.process_time()
    dot = 0
    for i in range(len(x1)):
        dot += x1[i] * x2[i]
    toc = time.process_time()
    print("dot = " + str(dot) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")

    # Classic outer product
    tic = time.process_time()
    outer = np.zeros((len(x1), len(x2)))
    for i in range(len(x1)):
        for j in range(len(x2)):
            outer[i, j] = x1[i] * x2[j]
    toc = time.process_time()
    print("outer = " + str(outer) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")

    # Classic elementwise multiplication
    tic = time.process_time()
    mul = np.zeros(len(x1))
    for i in range(len(x1)):
        mul[i] = x1[i] * x2[i]
    toc = time.process_time()
    print("elementwise multiplication = " + str(mul) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")

    # Classic general dot product
    tic = time.process_time()
    gdot = np.zeros(W.shape[0])
    for i in range(W.shape[0]):
        for j in range(len(x1)):
            gdot[i] += W[i, j] * x1[j]
    toc = time.process_time()
    print("gdot = " + str(gdot) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")

    # Vectorized implementations
    print("\nVectorized implementations:")
    
    # Vectorized dot product
    tic = time.process_time()
    dot = np.dot(x1, x2)
    toc = time.process_time()
    print("dot = " + str(dot) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")

    # Vectorized outer product
    tic = time.process_time()
    outer = np.outer(x1, x2)
    toc = time.process_time()
    print("outer = " + str(outer) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")

    # Vectorized elementwise multiplication
    tic = time.process_time()
    mul = np.multiply(x1, x2)
    toc = time.process_time()
    print("elementwise multiplication = " + str(mul) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")

    # Vectorized general dot product
    tic = time.process_time()
    dot = np.dot(W, x1)
    toc = time.process_time()
    print("gdot = " + str(dot) + "\n ----- Computation time = " + str(1000 * (toc - tic)) + "ms")

def run_tests():    
    print("\nTesting image2vector function:")
    t_image = np.array([[[ 0.67826139,  0.29380381],
                         [ 0.90714982,  0.52835647],
                         [ 0.4215251 ,  0.45017551]],
                        [[ 0.92814219,  0.96677647],
                         [ 0.85304703,  0.52351845],
                         [ 0.19981397,  0.27417313]],
                        [[ 0.60659855,  0.00533165],
                         [ 0.10820313,  0.49978937],
                         [ 0.34144279,  0.94630077]]])
    print("image2vector(image) = " + str(image2vector(t_image)))
    
    print("\nTesting normalize_rows function:")
    x = np.array([[0., 3., 4.],
                  [1., 6., 4.]])
    print("normalizeRows(x) = " + str(normalize_rows(x)))
    
    print("\nTesting softmax function:")
    t_x = np.array([[9, 2, 5, 0, 0],
                    [7, 5, 0, 0 ,0]])
    print("softmax(x) = " + str(softmax(t_x)))
    
    print("\nTesting L1 loss function:")
    yhat = np.array([.9, 0.2, 0.1, .4, .9])
    y = np.array([1, 0, 0, 1, 1])
    print("L1 = " + str(L1(yhat, y)))
    
    print("\nTesting L2 loss function:")
    print("L2 = " + str(L2(yhat, y)))

if __name__ == "__main__":
    print("Python Basics with NumPy")
    print("========================\n")
    
    # Simple test: Set test to "Hello World"
    test = "Hello World"
    print("test: " + test + "\n")
    
    # Run the tests for all implemented functions
    run_tests()
    
    # Demo vectorization performance
    print("\nDemonstrating vectorization performance:")
    demo_vectorization()
    
    print("\nAll tasks completed!")




