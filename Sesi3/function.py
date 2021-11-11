def printme(str = "This is default argument"):
    print(str)
    return


printme("Hello this is from function")
printme("This is the second line from function")


def print_personal_info(name, age):
    print("Hello this is", name, "I'm", age, "years old")


print_personal_info("Rafif", 22)

printme(str = "This is a keyword argument")

printme()

def functionTuple(arg1, *vartuple):
    print("Output is:", arg1)
    for n in vartuple:
        print(n)

functionTuple(10,60,50)