
# we have a class with a transform function. We could want to decorate the input data, or decorate the transform function depending on the input.
# Exploring the solution using a decorator.

def class_method_decorator(cls):
    
    def augment(self, data_list, f_trans):       
        print("this is the decorator applied")
        decorated_data = [x + "_decorated" for x in data_list]
        #we could change the transform function depending on the input params
        return cls.original_transform(decorated_data, f_trans)

    cls.original_transform = cls.transform
    cls.transform = augment
    return cls

@class_method_decorator
class A:
    @classmethod
    def transform(self, data_list, transform_function):
        for el in data_list:
            transform_function(el)

class B:

    def __init__(self, a :int, b : int, c :int):
        self._a = a
        self._b = b
        self._c = c
    
    @property
    def get_a(self):
        return self._a
    @property
    def get_b(self):
        return self._b
    
    @property
    def get_c(self):
        return self._c

def main():
    a = A()
    def f_trans(x = list[str]) : print(x)
    a.transform(["home", "llibre", "casa"], f_trans)
    
    b = B(2,4,6)
    print(b._a)
    print(b._b)
    print(b._c)

if __name__=="__main__": 
    main() 

