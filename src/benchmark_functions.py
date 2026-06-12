import numpy as np

def sphere(x):
    return np.sum(x**2)

def rastrigin(x):
    d = len(x)
    return 10*d + np.sum(x**2 - 10*np.cos(2*np.pi*x))

def ackley(x):
    d = len(x)
    return -20*np.exp(-0.2*np.sqrt(np.sum(x**2)/d)) - np.exp(np.sum(np.cos(2*np.pi*x))/d) + 20 + np.e

def rosenbrock(x):
    return np.sum(100*(x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

def griewank(x):
    i = np.arange(1, len(x)+1)
    return 1 + np.sum(x**2)/4000 - np.prod(np.cos(x/np.sqrt(i)))

def schwefel(x):
    d = len(x)
    return 418.9829*d - np.sum(x*np.sin(np.sqrt(np.abs(x))))

def levy(x):
    w = 1 + (x - 1)/4
    return (
        np.sin(np.pi*w[0])**2
        + np.sum((w[:-1]-1)**2 * (1 + 10*np.sin(np.pi*w[:-1] + 1)**2))
        + (w[-1]-1)**2 * (1 + np.sin(2*np.pi*w[-1])**2)
    )
