# function which return the sum of first n natural numbers

def addInt(n: int) -> int:
    if n <= 0:
        return 0
    else:
        return addInt(n - 1) + n  # -> 1 + 2 + 3 + ... + (n-2) + (n-1) + n


print(addInt(7))

# Proof of correctness: (Proof by induction)
# Claim 1 (Base case): addInt returns the right answer of 0
# Claim 2 (Recursive Assumption + Self Work):
#          If addInt returns the right answer for n - 1, (Recursive Assumption)
#          it can correctly calculate the answer for n. (Self work)
# Claim 3: Thus it can correctly calculate the answer for every n.

# Base Case: In base case, you hard code the solution for the smallest input
# Recursive Assumption: You assume that the function works for a subproblem
# Self work: You get the answer for bigger problem from the subproblem
