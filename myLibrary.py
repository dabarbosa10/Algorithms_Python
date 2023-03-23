#We are defining some libraries here
# Addition of two numbers
def add(x,y):
    return x+y
#Subtraction of two numbers
def sub(x,y):
    return x-y
#Greeting
def hello():
    print("Hello World")

##Sometimes it is useful to declare a main function main
def main():
    hello()
    print(add(10,20))
    print(sub(10,20))
    print("TEST")


#For example this can be used if we want to test the library
#but this is not used
if __name__ == 'main':
    main()

