def longestCommonPrefix(strs:list[str]) -> str:
    
    prefix = ""
    try: # If the array is only an empty string, return ""
        next_prefix = strs[0][0]
    except:
        return ""

    counter = 1

    arr_index = 0
    arr_range = len(strs)

    while counter != len(strs[0]) + 1:
        # If all the strings passed the comparison, raise the counter up
        if arr_index == arr_range:
            arr_index = 0
            counter += 1

            # The 'next_prefix' was presented in every string, so from now on, return 'prefix'
            # 'next_prefix' will now have one more letter
            prefix = next_prefix
            next_prefix = strs[0][:counter]
            print("Next prefix")

        # If the 'next_prefix' is present in the string, go to the next string
        if next_prefix == strs[arr_index][:counter]:
            arr_index += 1
        else:
            # Returns the previous working prefix
            print("Returned prefix")
            return prefix
    return prefix


    

print(longestCommonPrefix(["ab", "a"]))
