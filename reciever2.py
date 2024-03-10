import socket

dec_key= input("give the encryption key ")

n= len(dec_key)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 4288))

message = s.recv(1000)

message = message.decode("utf-8")
x=len(message)//n
if len(message) % n != 0:
    x += 1
y = 0

z = [" "] * len(message)
for i in range(x):
    for j in range(n):
        if int(dec_key[j]) - 1 + (n) * i >= len(message):
            continue
        z[ i*(n)  + int(dec_key[j]) - 1] = message[y]
        y += 1

print("DECRYPTED MESSAGE:", "".join(z))
