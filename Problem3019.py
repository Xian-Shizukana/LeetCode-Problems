def countKeyChanges(s:str) -> int:
    key_changed = 0
    current_char = s[0].lower()

    for char in s.lower():
        if current_char != char:
            key_changed += 1
            current_char = char
        else:
            continue

    return key_changed

print(countKeyChanges("aAbBcC"))
