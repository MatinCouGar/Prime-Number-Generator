def avval(a):
    if a == 2:
        return "avval hast"
    elif a == 1:
        return "avval nist"
    if a%2 == 0:
        return "avval nist"
    else:
        runner = a//2 + 1
        while runner != 2:
            runner = runner -1
            if a%runner == 0:
                return "avvan nist"
                break
            else:
                if runner == 2:
                    return "avval hast"
                    break
adad = int(input("adad ro vared kon: "))
print(avval(adad))