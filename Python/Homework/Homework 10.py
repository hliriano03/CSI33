def recFib(n):

    print("Computing recFib(" + str(n) + ")\n")

    #returns 1 if n is less than 3
    if n < 3:
        print("Leaving recFib(" + str(n) + ") returning 1")
        return 1

    #returns the sum of recFib(n-1) and recFib(n-2)
    else:
        m = recFib(n-1) + recFib(n-2)
        print("Leaving recFib(" + str(n) + ") returning " + str(m))
        return m

print(recFib(3))
