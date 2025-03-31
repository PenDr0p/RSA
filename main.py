#RSA has three main stages: key generation, encryption, and decryption
import math


def generateKeys():
    p = 349207
    q = 966209

    n = p * q
    e = 69759637427
    d = 19479039995

    return p, q, n, e, d

def encrypt(M, e, n):
    #print("made it to encryption")
    C = []
    for val in M:
        #print("in for loop")
        new_val = pow(val, e, n)
        C.append(new_val)
    #print("out of for loop")
    return C

def decrypt(C, d, n):
    M=""
    for val in C:
        new_val = pow(val, d, n)
        letter = chr(new_val)
        M += letter
    return M


if __name__ == '__main__':
    M = input("Enter text: ")
    p, q, n, e, d = generateKeys()

    print("Keys: \n")
    print(f"p: ", p, "\n")
    print(f"q: ", q, "\n")
    print(f"n: ", n, "\n")
    print(f"e: ", e, "\n")
    print(f"d: ", d, "\n")
    print(f"Message: ", M, "\n")

    #take the message and get ascii values for each character
    M_int = [ord(character) for character in M]
    #print(M_int)
    C = encrypt(M_int, e, n)
    decryptM = decrypt(C, d, n)

    print(f"Encrypted: ", C, "\n")
    print(f"Decrypted: ", decryptM, "\n")

