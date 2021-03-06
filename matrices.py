import numpy as np

def sigmoid(x):
    '''sigmoid function
    '''
    return 1.0/(1+ np.exp(-x))

def sigmoid_derivative(x):
    '''sigmoid_derivative
    '''
    return x * (1.0 - x)

def crossover(a, b, crossover_rate):
    '''crossover function
    '''
    if np.random.randint(1,100)<crossover_rate:
        return a #child value
    else:
        return b #parent value

def randomize(rows, cols):
    '''Generating random matrix. Values ranges from -1 to 1
    '''
    return 2*np.random.rand(rows, cols+1)-1

def random_mutation():
    '''Function simulating how much is mutation
    Rigth now it gives values ranged from -2 to +2
    '''
    return (4*np.random.rand()-2)

def mutate(mutation_rate, value):
    '''Mutate function    
    '''
    if np.random.randint(1,100)<mutation_rate:
        value += random_mutation()
    if value > 1 or value <-1:
    	return int(value)
    else:
    	return value

def add_bias(array):
    '''Adds 1 to the bottom of array
    '''
    return np.append(array, 1)

#Vectorize section.
#With this method we can applied aboved function on every value
#of matrix
sigmoid = np.vectorize(sigmoid)
sigmoid_derivative = np.vectorize(sigmoid_derivative)
crossover = np.vectorize(crossover)
mutate = np.vectorize(mutate)