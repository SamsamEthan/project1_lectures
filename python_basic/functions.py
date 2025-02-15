#defining a function
#this function is called square and this takes 1 argument '(x)'
#if you hand me a number x, i will return that number squared

def square(x):
    return x * x

def main():
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))

    print("enter a number")
    num = input()
    n = int(num)
    print("enter a name")
    name = input()

    print("{}'s number is {}, this number squared is {}".format(name, num, square(n)))
        

#in other words, if I am running this particular file then run the main
if __name__ == "__main__":
    main()
