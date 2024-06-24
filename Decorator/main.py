

def class_method_decorator(cls):
    def augment(self):
        print("this is the decorator applied")
    cls.augment = augment
    return cls

@class_method_decorator
class A:

    data = list[str]

    def __init__(self, list = []):
        self.data = list

    def transform(self, transform_function):
        for el in self.data:
            transform_function(el)

def main():
    a = A(["home", "llibre", "casa"])
    def f_trans(x = list[str]) : print(x)
    a.transform(f_trans) 

if __name__=="__main__": 
    main() 