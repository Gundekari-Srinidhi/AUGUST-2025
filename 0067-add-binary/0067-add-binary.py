class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert both binary strings to decimal integers
        s = int(a, 2)
        p = int(b, 2)

        # Add them
        n = s + p

        # Convert back to binary (strip '0b' prefix)
        return bin(n)[2:]
