import math
import random

"""
This is a basic implementation of the RSA algorithm. It is not cryptographically
secure, but demonstrates the basic understanding of the algorithm. I referenced functions
from this blog to help in generating large prime numbers: 
https://incolumitas.com/2018/08/12/finding-large-prime-numbers-and-rsa-miller-rabin-test/
"""

#this is the extended euclian algorithm plulled from wikibooks
#https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
#I ended up not using this but out of spite i'm keeping it here
def eea(a,b):
    print("doing eea \n")
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        print("while a!=0 \n")
        (q, a), b = divmod(b, a), a
        print(a)
        print(type(a))
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    print("done with eea")
    return b, x0, y0

#This function is used to check the prime numbers we generate from generatePrimes()
def millerRabinPrimeTest(p, s):
    #print("preforming miller rabin's prime test \n")
    if p == 2:
        #print("p is prime \n")
        return True
    if not (p & 1):
        #print("p is not prime \n")
        return False

    p1 = p - 1
    u = 0
    r = p1

    while r % 2 == 0:
        #print("In while loop \n")
        #print(f"r= ", r, "\n")
        #print(f"u= ", u, "\n")
        r >>= 1
        u += 1

    #print("Out of while loop\n")
    for j in range(s):
        a = random.randint(2,p-2)
        #print("confirming prime check\n")
        if checkNotPrime(a, r, p, u, p1):
            #print("not prime\n")
            return False

    #print("prime\n")
    return True

def checkNotPrime(a, r, p, u, p1):
    z = pow(a,r,p)
    if z == 1:
        return False

    for i in range(u):
        z = pow(a, 2**i * r, p)
        if z == p1:
            return False
    return True
def generatePrime():
    #print("generating primes\n")
    x = random.getrandbits(16)

    while True:
        #print("in while loop...\n")
        if millerRabinPrimeTest(x, 7):
            break
        x += 1
    #print("done with generating primes\n")
    return x

def generateKeys():
    p = generatePrime()
    q = generatePrime()

    n = p * q
    phi_n = (p - 1) * (q - 1)

    #print(f"p = {p} \n")
    #print(f"q = {q} \n")
    #print(f"n = {n} \n")
    #print(f"phi = {phi_n}\n")

    #find e by taking a random number from the range 1-phi_n and then check if the gcd of e and phi_n is 1, if so then you're done
    while True:
        e = random.randrange(1, phi_n)
        #print(f"e = {e} \n")
        if math.gcd(e, phi_n) == 1:
            break

    #d*emod(phi_n) = 1
    #d = 1/ emod(phi_n)
    d = pow(e, -1, phi_n)

    return p, q, n, e, d

def encrypt(M, e, n):
    #print("made it to encryption")
    #create empty list to store encrypted ascii vals
    C = []
    #go through each ascii value
    for val in M:
        #print("in for loop")
        new_val = pow(val, e, n)
        C.append(new_val)
    #print("out of for loop")
    return C

def decrypt(C, d, n):
    #create an empty string to store decyrpted chars
    M=""
    #go through the encrypted list
    for val in C:
        #get the decrypted ascii value
        #print(type(val))
        #print(type(d))
        #print(type(n))
        new_val = pow(val, d, n)
        #convert the ascii value to a char
        letter = chr(new_val)
        #append the char to the return string
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
    #this will generate a list of ascii values for each character in the string
    M_int = [ord(character) for character in M]
    #print(M_int)

    #encrypt the list to get C
    C = encrypt(M_int, e, n)
    #now decrypt that list
    decryptM = decrypt(C, d, n)

    print(f"Encrypted: ", C, "\n")
    print(f"Decrypted: ", decryptM, "\n")

