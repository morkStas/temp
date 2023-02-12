def recursion(num):

    if num != 1:
        return (recursion(num - 1) + ", " + num)
    else:
        return num

N = int(input("N = "))
print(f"-> {recursion(N)}")
