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


def nonRestoringDivision(Q, M, A):

    count = len(M)

    comp_M = compliment(M)

    flag = "successful"

    print("Initial Values: A:", A, " Q:", Q, " M:", M)

    while count:

        print("\nstep:", len(M) - count + 1)

        A = A[1:] + Q[0]
        print("A:", A, " Q:", Q[1:] + "_", " -Left Shift")

        if flag == "successful":
            A = add(A, comp_M)
            print("A:", A, "          -Subtract")
        else:
            A = add(A, M)
            print("A:", A, "          -Addition ")

        print("A:", A, " Q:", Q[1:] + "_", end="")

        if A[0] == "1":

            Q = Q[1:] + "0"
            print("  -Unsuccessful")

            if count == 1:
                A = add(A, M)
                print("A:", A, " Q:", Q, " -Restoration ")
            else:
                flag = "unsuccessful"
                print("A:", A, " Q:", Q, " -Addition in next Step")

        else:

            Q = Q[1:] + "1"
            print("  -Successful")

            flag = "successful"
            print("A:", A, " Q:", Q, " -Subtraction in next step")
        count -= 1
    print("\nQuotient(Q):", Q, " Remainder(A):", A)


# Driver code
if __name__ == "__main__":

    dividend = "0111"
    divisor = "0011"

    accumulator = "0" * len(dividend)

    nonRestoringDivision(dividend, divisor, accumulator)
