


class Encap:                  #Public is an access spicifier. By these spicifiers only we can acheive encapsulation.
    def fan(self):            #public is the bydefault access specifier.
        print("hello")
c1=Encap()
c1.fan()


#Private




class ac:                        #private is an access specifier. The methods and functions can be used by this class only.
    __a=10;
    def __cold(self):
        print(self.__a)
        print(self.__cold)
       






