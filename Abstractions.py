#import ABC,abstractmethod from abc.


from abc import ABC,abstractmethod     

#abstraction means hiding the implementation part and showing the declaration part.



class ss(ABC):                           
    @abstractmethod
    def display(self):
        None
    @abstractmethod
    def show(self):
        None
        
class dd(ss):
    def display(self):
        print("hello")
    def show(self):
        print('bye')
obj=dd()
obj.display()
obj.show()






