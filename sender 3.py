import socket

#USING SUBSTITUTION CIPHER METHOD
key = "ABCDEFGHIJKLMNOPQRSTUVWX abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*)(_+=-}{][|:;><.,?/"
print("Enter the Substitution Cipher Keyword: ", end="")
cipher = input()
mp = {}
new_key = ""
    
for char in cipher:
    if char not in mp:
        new_key += char
        mp[char] = True
    
for char in key:
    if char not in mp:
        new_key += char
        mp[char] = True
    
mp2 = {}
# mp3 = {}
    
for i in range(len(key)):
    mp2[new_key[i]] = key[i]
    # mp3[key[i]] = new_key[i]
    
print("Enter the Message: ", end="")
msg = input()
    
encrypted_msg = ""
for char in msg:
    encrypted_msg += mp2[char]
    
print("Encrypted Message:", encrypted_msg)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 4288))

s.listen(5)

while True:

    clt, adr = s.accept() #returns object using which msg can be send and address
    
    clt.send(bytes(encrypted_msg,"utf-8"))