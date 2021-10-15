import keygen

def encrypt(e, N, msg):
    cipher = ""

    for i in msg:
        cipher += str(pow(ord(i), e, N)) + " "

    return cipher


def decrypt(d, N, cipher):
    msg = ""

    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, N))

    return msg


def numToAsc(num):
    parts = num.split()
    converted = ""

    for i in (parts):
        for j in (i):
            j = int(j) + 65
            converted += chr(j)
        converted += " "

    return converted


def ascToNum(asc):
    parts = asc.split()
    converted = ""

    for i in (parts):
        for j in (i):
            temp = ord(j)
            temp -= 65
            converted += str(temp)
        converted += " "
        
    return converted

