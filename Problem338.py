def countBits(n:int) -> list[int]:
    count_arr = []
    
    for i in range(0, n + 1):
        binary_str = bin(i)
        count_arr.append(binary_str.count("1")) 

    return count_arr

print(countBits(2))
