import socket

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

mp3 = {}
    
for i in range(len(key)):
    mp3[key[i]] = new_key[i]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 4288))

message = s.recv(1000)

message = message.decode("utf-8")

decrypted_msg = ""
for char in message:
    decrypted_msg += mp3[char]
    
print("Decrypted Message:", decrypted_msg)
