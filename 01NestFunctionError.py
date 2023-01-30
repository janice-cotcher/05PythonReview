# prints ABAC on separate lines through a series of function calls


def C():
    """Calls functions b & A and then prints the letter C"""
    def A():
        """prints the letter A"""
        print("A")


    def B():
        """prints the letter B then calls function A"""
        print("B")
        A()
    A()
    B()
    print("C")


C()
A()
B()