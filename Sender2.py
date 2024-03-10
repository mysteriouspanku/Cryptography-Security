import socket
#USING TRANSPOSITION CIPHER METHOD
key = input("Enter the Transposition Cipher key: ")
n = len(key)
print("Enter your message: ")
s = input()
print("Message:", s)
x = len(s) // n
if len(s) % n != 0:
    x += 1
    t = True
print(x)
message = ""

for i in range(x):
    for j in range(n):
        if int(key[j]) - 1 + (n)  * i >= len(s):
            continue
        message += s[int(key[j]) - 1 + (n) * i]

print("ENCRYPTED MESSAGE:", message)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 4288))

s.listen(5)

while True:

    clt, adr = s.accept() #returns object using which msg can be send and address
    
    clt.send(bytes(message,"utf-8"))