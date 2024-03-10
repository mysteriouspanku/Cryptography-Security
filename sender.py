import socket

#USING CEASER CIPHER METHOD
message = input("Please enter yur message ")

key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ$%^&*()_-+=}{][`|:;~`><?/~abcdefghijklmnopqrstuvwxyz.,1234567890 !@#"
val= key[::-1]

encrypter = dict(zip(key, val))

message = "".join([encrypter[words] for words in message])

print(message)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 4288))

s.listen(5)

while True:

    clt, adr = s.accept() #returns object using which msg can be send and address
    
    clt.send(bytes(message,"utf-8"))