# first_module.py

def addition(i,j):
    print("Add")
    k = i + j
    print("{} + {} = {}".format(i,j,k))
    return

def subtraction(i,j):
    print("subtract")
    k = i - j
    print("{} - {} = {}".format(i,j,k))
    return

def addsub(x,y,symbol):
    if symbol == "+":
        c = x + y
    elif symbol == "-":
        c = x-y
    else:
        c = "Unrecognized"
    return c

if __name__ == "__main__":
    x = input("Input a command: ")
    print("You entered {}.".format(x))
    a = int(input("a = "))
    b = int(input("b = "))
    if x == 'add' or x == 'a':
        c = addsub(a,b,"+")
        #addition(int(a),int(b))
    elif x == "subtract" or x == 's':
        c = addsub(a,b,"-")
        #subtraction(int(a),int(b))
    else:
        print("{} is not an active command.".format(x))
    print("c = {}".format(c))
    print("Done")
