# Usage of Docsting for getting informatoon about  function
def my_function():
    """ Demonstrate docstring and does nothing """
    return None
print ("Using __doc__:")
print(my_function.__doc__)
print("Using help: ")
help(my_function)

#%% # oneline docstring
def power(a,b):
    """ Returns arg1 raised to arg 2."""
    return a**b
print(power.__doc__)

#%% # Multiline Docstring
def my_func(arg1):
    """
    Multiline docstring
    to give info about 
    the this function file
    
    """
    return arg1
print(my_func.__doc__)
#%%
class ComplexNumber:
    """
    This is a class for mathematical operations on complex numbers.
    Attributes:
        real (int): The real part of complex number. 
        imag (int): The imaginary part of complex number.
    """
    def __init__(self,real,imag):
        """
        The constructor of Complexnumber class
        Parameters:
            real(int): the real part of complex numbers.
            imag (int): The imaginary part of complex number.
        """
    def add(self,num):
        """
        The function to add two numbers.
        Parameters: 
            num (ComplexNumber): The complex number to be added. 
        Returns: 
            ComplexNumber: A complex number which contains the sum.
            
        """
        re = self.real + num.real 
        im = self.imag + num.imag 
        return ComplexNumber(re, im)
help(ComplexNumber)  # to access Class docstring 
help(ComplexNumber.add)  # to access method's docstring 