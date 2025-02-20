def main():
    num = int(input("Enter a positive integer: "))
    if num<=0:
        print("please enter a positive integer: ")
        return
    for i in range(1, num+1):
        if num%i==0:
            print(f"{i} is a factor of {num}")
if __name__=="__main__":
    main()