class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binary_sum = int(a) + int(b)
        binary_array = []
        binary_string = ""

        for char in str(binary_sum):
            binary_array.append(int(char))

        while 2 in binary_array:
            x = binary_array.index(2)
            binary_array[x] = 0
            if x - 1 == -1:
                binary_array.insert(0,1)
            else:
                binary_array[x-1] += 1

        for i in binary_array:
            binary_string += str(i)

        return binary_string
