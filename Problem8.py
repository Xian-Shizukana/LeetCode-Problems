def myAtoi(s: str) -> int:
    
    value = ""

    for char in s:
        match char:
            case " ":
                if value != "":
                    break
                else:
                    continue
            case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0":
                value += char
            case "-":
                if value != "":
                    break
                else:
                    value += char
            case "+":
                if value != "":
                    break
                else:
                    value += char
            case _:
                break

    if value in ["", "-", "+"]:
        value = "0"

    value = int(value)

    if value > 2**31 - 1:
        value = 2**31 - 1
    if value < -2**31:
        value = -2**31

    return value

print(myAtoi("     -042"))
