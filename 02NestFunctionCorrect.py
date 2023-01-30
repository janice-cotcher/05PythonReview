# prints ABAC on separate lines through a series of function calls


def A():
    """prints the letter A"""
    print("A")


def B():
    """prints the letter B then calls function A"""
    print("B")
    A()

def C():
    """Calls functions B & A and then prints the letter C"""
    A()
    B()
    print("C")

C()