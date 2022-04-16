class parent:
    def summ(self):
        print("Hello")
        
class child(parent):
    def subs(self):
        print("Bye")
        
c1=child()
c1.summ()
c1.subs()

#Multilevel
class gparent:
    def display(self):
        print("Gp")
class pparent(gparent):
    def show(self):
        print("PP")
class child(pparent):
    def show1(self):
        print("Cc")
        
c2=child()
c2.display()
c2.show()
c2.show1()


#Hierarchical
class parent:
    def p1(self):
        print("Hello")
class child1(parent):
    def c1(self):
        print("hello1")
class child2(parent):
    def c2(self):
        print("hello2")
        
c3=child1()
c4=child2()
c3.c1()
c3.p1()
c4.c2()
c4.p1()

#Multiple 
class Father:
    def f1(self):
        print("Father")
        
class Mother:
    def f2(self):
        print("Mother")
class child(Father,Mother):
    def f3(self):
        print("child")
        
c1=child()
c1.f3()
c1.f2()
c1.f1()







