from rsa_algorithm import ascToNum, encrypt, decrypt, numToAsc
from keygen import generateKeys

while True:
    print("Welcome to RSA Encryption and Decryption Program")
    print("---")
    print("Menu:")
    print("1. Generate Public and Private Key")
    print("2. Encrypt a Message")
    print("3. Decrypt a Message")
    print("4. Encrypt and Decrypt a Message")
    print("5. Exit")
    choice = int(input("Choose Menu: "))

    if (choice == 1):
        e, d, N = generateKeys()
        print(f"e = {e} \nd = {d}\nN = {N}")
    elif (choice == 2):
        print(
            """ 
                Keys:
                1. I have my own keys
                2. Generate new keys
            """)
        choice = int(input("Enter your choice: "))
        if (choice == 1):
            e = int(input("Enter public key: "))
            N = int(input("Enter n value: "))
        else:
            e, d, N = generateKeys()
        msg = input("Enter message: ")
        encrypted = encrypt(e, N, msg)
        # cipher = numToAsc(encrypted)
        print(f"Encrypted message: {encrypted}")
    elif (choice == 3):
        d = int(input("Enter private key: "))
        N = int(input("Enter n value: "))
        cipher = input("Enter encrypted cipher text: ")
        # converted = ascToNum(cipher)
        decrypted = decrypt(d, N, cipher)
        print(f"Decrypted message: {decrypted}")
    elif (choice == 4):
        print(
            """ 
                Keys:
                1. I have my own keys
                2. Generate new keys
            """)
        choice = int(input("Enter your choice: "))
        if (choice == 1):
            e = int(input("Enter public key: "))
            N = int(input("Enter n value: "))
        else:
            e, d, N = generateKeys()
        msg = input("Enter message: ")
        encrypted = encrypt(e, N, msg)
        # cipher = numToAsc(encrypted)
        print(f"Encrypted message: {encrypted}")
        # converted = ascToNum(cipher)
        decrypted = decrypt(d, N, encrypted)
        print(f"Decrypted message: {decrypted}")
    elif (choice == 5):
        print("Thank You for using this program. See you!!")
        break
