# basics.py script
#easier if broken down into modular functions
x = input("Input a command: ")
print("You entered {}.".format(x)) #print variable within string
if x == 'add' or x == 'a': #start defining new code block
    print("Add")
    a = 1
    b = 2
    print("a = {}".format(a))
    c = a + b
    print("{} + {} = {}".format(a,b,c))
elif x == "subtract" or x == 's':
    print("subtract")
    a = 1
    b = 2
    c = a - b
    print("{} - {} = {}".format(a,b,c))
else:
    print("{} is not an active command.".format(x))
print("Done")
