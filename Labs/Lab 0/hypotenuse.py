import math

def calchypotenuse(a, b):
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    return hypotenuse

def main():
    a = int(input("Enter first number: "))
    print(a)
    b = int(input("Enter second number: "))
    print(b)

    h = calchypotenuse(a,b)
    print("the hypotenuse is: " + str(h))

if __name__ == '__main__':
    main()