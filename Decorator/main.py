
# we have a class with a transform function. In some cases we want to apply a pre-transform function to the elements of the list to be transform.
# Exploring the solution using a decorator.

def class_method_decorator(cls):
    def augment(self, f_trans):       
        print("this is the decorator applied")
        cls.original_transform(f_trans)
        return

    cls.original_transform = cls.transform
    cls.transform = augment
    return cls

@class_method_decorator
class A:

    data = list[str]

    def __init__(self, list = []):
        self.data = list

    @classmethod
    def transform(self, transform_function):
        for el in self.data:
            transform_function(el)


def main():
    n = A(["home", "llibre", "casa"])
    def f_trans(x = list[str]) : print(x)
    n.transform(f_trans)
    

if __name__=="__main__": 
    main() 

