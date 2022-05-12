def rotation_string(str1, str2):
    s1 = len(str1)
    s2 = len(str2)
    temp = ""

    if s1 != s2:
        return 0
    else:
        temp = str1 + str2

        if str2 in temp:
            return True
        else:
            return False

str1 = input("Enter First String")
str2 = input("Enter Second String")

if rotation_string(str1, str2):
    print("Strings are rotations of each other.")
else:
    print("Strings are not rotations of each other.")
