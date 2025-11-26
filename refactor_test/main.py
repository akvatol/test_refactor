def main():
    print("Hello, World!")


def divide(x:int, y:int):
    return x / y


def summ(*args):
    if isinstance(args[0], (tuple, list)):
        return sum(args[0])
    else:
        ans = 0
        for i in args:
            ans += i
        return ans

if __name__ == "__main__":
    main()
