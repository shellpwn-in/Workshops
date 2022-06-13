string = "q{vpln'bH_varHuebcrqxetrHOXEj"
for no in range(257): #ascii have 256 different ascii characters
    encrypted = ''.join([chr(ord(x) ^ no) for x in string])
    #print(encrypted)
    if encrypted.startswith("flag"):
        flag = encrypted
        print(no)
print(flag)