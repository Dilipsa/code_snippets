"""
The diamond problem typically occurs in multiple inheritance scenarios, particularly when a subclass 
inherits from two separate classes that have a common ancestor. This can lead to ambiguity 
when accessing attributes or methods from the common ancestor.
"""
class A:
    def method(self):
        print("Method from class A")


class B(A):
    def method(self):
        print("Method from class B")


class C(A):
    def method(self):
        print("Method from class C")


class D(B, C):
    pass


# Creating an instance of D
d = D()

# Calling the method
d.method()


"""
In this example, we have four classes: A, B, C, and D. Both B and C inherit from class A, and class D inherits from both B and C. 
This creates a diamond-shaped inheritance structure:
  A
 / \
B   C
 \ /
  D
When we create an instance of class D and call the method, which method should be called? Should it 
be the one from class B or the one from class C? This ambiguity is the diamond problem.

In Python, the method resolution order (MRO) dictates the order in which methods are searched for. 
By default, Python uses C3 linearization to determine the MRO. In the case of class D, 
Python will prioritize the MRO as D, B, C, A. Therefore, the method from class B will be called.
"""