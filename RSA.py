# RSA.py by elio27
#coding:utf-8

import random


class KeyPair:
    def __init__(self):
        self.GenKey()
        self.public_key = (self.n, self.e)
        self.private_key = (self.n, self.d)
        
    def GenKey(self):
        self.p = self.GenPrime()
        self.q = self.GenPrime()
        self.n = self.p * self.q
        self.phi = self.lcm(self.p - 1, self.q - 1)
        self.e = self.Find_e()
        self.d = self.Find_d()
        
    def IsPrime(self, num):
        x = 0
        for i in range(2,num):
            if num%i==0:
                x = 1
                break
        if(x==0) and (num!=1):
            return num
        
    def GenPrime(self):
        PrimeNum = 0
        for i in range(0,100):
            randomNum = random.randint(101,5673)
            Prime = self.IsPrime(randomNum)
            if Prime != None:
                PrimeNum = Prime
                return PrimeNum
            
    def gcd(self, a, b):
        if a > b:
            x = a
            y = b
        else:
            x = b
            y = a
        for w in range(10000000):
            z = x - y
            if z == 0:
                return y
            if z > y:
                x = z
                y = y
            else:
                x = y
                y = z
                
    def lcm(self, a, b):
        return int((a*b)/self.gcd(a, b))
    
    def Find_e(self):
        for i in range(1, self.n):
            if (i < self.n) and (self.gcd(i, self.phi) == 1):
                if i > 1:
                    return i
                
    def Find_d(self):
        for i in range(1, self.n):
            if ((self.e * i) % self.phi) == 1:
                return i


def encrypt(text, public_key):

    """
    :param text: String => The message you want to encrypt
    :param public_key: Tuple => The public key of the person you're talking to
    :return: List => The encrypted message
    """

    x = []
    for char in text:
        y = ord(char)
        y = y ** public_key[1]
        y = y % public_key[0]
        x.append(y)
    return x

def decrypt(encrypted, private_key):

    """
    :param encrypted: List => The message you want to decrypt
    :param private_key: Tuple => Your private key
    :return: String => The decrypted message
    """

    z = ""
    for c in encrypted:
        c = c ** private_key[1]
        c = c % private_key[0]
        print(c)
        z = z + chr(c)
    return z

def CreateSignature(private_key):

    """
    :param private_key: Tuple => Your private key
    :return: List => A list to send to your correspondent to prove your authenticity
    """

    signature = encrypt("Fetchez la vache !",private_key)
    return signature


def CheckSignature(signature, public_key):

    """
    :param signature: List => Output of the CreateSignature function
    :param public_key: Tuple => The public key of your correspondent
    :return: Bool => True if the signature is valid.
    """

    return decrypt(signature, public_key) == "Fetchez la vache !"
