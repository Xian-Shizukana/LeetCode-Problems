def uniqueMorseCodeRepresentations(words:list[str]) -> int:
    morse_arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    morse_set = set()

    for word in words:
        word_morse = []
        for char in word:
            char_val = ord(char) - 97
            word_morse.append(morse_arr[char_val])
        morse_set.add("".join(word_morse))
     
    return len(morse_set)

print(uniqueMorseCodeRepresentations(["gin","zen","gig","msg"]))
        
