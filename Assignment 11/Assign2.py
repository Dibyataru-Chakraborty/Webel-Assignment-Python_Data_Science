def test(n):
    return int(bin(n)[::-1][:-2], 2)

n = int(input("Enter a Number: "))

print("Reverse the binary representation of the said integer and convert it into an integer:\n",test(n))