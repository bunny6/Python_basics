

num=[3,4,5,6]
it=iter(num)
print(it.__next__())
print(it.__next__())



class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
            if self.num<=10:
                val=self.num
                self.num+=1
                return val
            else:
                raise StopIteration
            
values=topten()
for i in values:
    print(i)
         







