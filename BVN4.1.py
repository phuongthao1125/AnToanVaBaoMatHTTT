def caesar_encrypt(plaintext, k):
    result=""
    for i in range(len(plaintext)):
        char=plaintext[i]
        if char.isupper():
            result+=chr((ord(char)+k-65)%26+65)
        else:
            result+=chr((ord(char)+k-97)%26+97)
    return result
plaintext="NguyenThiPhuongThao"
k=24
print("Plaintext: "+plaintext)
print("Shift: "+str(k))
print ("Cipher: "+caesar_encrypt(plaintext,k))