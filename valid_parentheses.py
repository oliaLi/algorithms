def validP(s):
    arr = []
    dict = {"]": "[", "}": "{", ")": "("}
    for char in s:
        if char in dict.values():
            arr.append(char)
        elif char in dict.keys():
            print(arr)
            if arr == [] or dict[char] != arr.pop():
                return False
        else:
            return False
    return arr == []