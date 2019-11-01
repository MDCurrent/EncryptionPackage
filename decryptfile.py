from cryptography.fernet import Fernet

file = open('na.key', 'wb')
key = file.read()
file.close()
file = open('that-good-good.txt', 'r')
encrypted = file.read()
file.close()
fernet = Fernet(key)
message = f.decrypt(encrypted)

file = open('that-good-good.mp3', 'wb')
file.write(message)
file.close()
