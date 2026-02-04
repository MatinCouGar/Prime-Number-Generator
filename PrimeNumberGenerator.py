def primegen(a):
    if a == 2:
        return True
    elif a == 1:
        return False
    if a%2 == 0:
        return False
    else:
        runner = a//2 + 1
        while runner != 2:
            runner = runner -1
            if a%runner == 0:
                return False
            else:
                if runner == 2:
                    return True
number = int(input("Generate up to what number? "))
counter = 0
while counter < number:
    if primegen(counter) == True:
        print(counter)
        counter = counter + 1
    else:
        counter = counter + 1