def add(A, M):
    carry = 0
    Sum = ""

    for i in range(len(A) - 1, -1, -1):

        temp = int(A[i]) + int(M[i]) + carry

        if temp > 1:
            Sum += str(temp % 2)
            carry = 1
        else:
            Sum += str(temp)
            carry = 0

    return Sum[::-1]


def compliment(m):
    M = ""

    for i in range(0, len(m)):

        M += str((int(m[i]) + 1) % 2)

    M = add(M, "0001")
    return M


def restoringDivision(Q, M, A):

    count = len(M)

    print("Initial Values: A:", A, " Q:", Q, " M:", M)

    while count:

        print("\nstep:", len(M) - count + 1)

        A = A[1:] + Q[0]

        comp_M = compliment(M)

        print("A:", A, " Q:", Q[1:] + "_", " -Left Shift")
        A = add(A, comp_M)
        print("A:", A, end=" ")
        print("          -Subtract")
        print("A:", A, " Q:", Q[1:] + "_", end="")

        if A[0] == "1":

            Q = Q[1:] + "0"
            print("  -Unsuccessful")

            A = add(A, M)
            print("A:", A, " Q:", Q, " -Restoration")

        else:

            Q = Q[1:] + "1"
            print("  -Successful")

            print("A:", A, " Q:", Q, " -No Restoration")
        count -= 1

    print("\nQuotient(Q):", Q, " Remainder(A):", A)


# Driver code
if __name__ == "__main__":

    dividend = "0111"
    divisor = "0011"

    accumulator = "0" * len(dividend)

    restoringDivision(dividend, divisor, accumulator)
