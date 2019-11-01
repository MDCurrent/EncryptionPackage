from cryptography.fernet import Fernet

file = open('na.key', 'r')
key = file.read()
file.close()

file = open('your-file-name-here.ext', 'rb')
message = file.read()

f = Fernet(key)
encrypted = f.encrypt(message)

encryped_file = open('that-good-good.txt', 'wb')
encryped_file.write(encrypted)
encryped_file.close()
