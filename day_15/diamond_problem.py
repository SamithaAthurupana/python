class A:
    def a_method(self):
        print("A class Method")

class B(A):
    def a_method(self):
        print("A class overridden by B")

    def b_method(self):
        print("from B")

class C(A):
    def a_method(self):
        print("A class overridden by C")

    def c_method(self):
        print("from c")

class D(B,C):
    def d_method(self):
        print("D class method")

    def c_method(self):
        print("C class overridden by D")

d_obj = D()

d_obj.d_method()   # from D
d_obj.a_method()   # check MRO (B vs C vs A)
d_obj.b_method()   # from B
d_obj.c_method()   # from D (overridden)