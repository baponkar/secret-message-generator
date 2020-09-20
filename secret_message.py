""" Secret Message Encode and Decode 
Description : This can encode the inputed message in evry time with new key.
And you can decode the encoded message by giving key.
You are not able to decode the message without key file.
License : GNU GPL V-3.0
Version - V-1.0.0
Build Date : 20/09/2020
Last Update : 20/09/2020
Author : Bapon Kar
Downloaded Link : https://github.com/baponkar/secret-message-generator
"""


import random
import os

#Encoder messages

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = alphabet + alphabet.upper()
l = []
for i in alphabet:
    l.append(i)
l.extend([' ','\n','\t','-','_','!','@','#','$','%','^','&','*','.','/','\'','\"',';',':','{','}','(',')','|','[',']',','])
l.extend(['0','1','2','3','4','5','6','7','8','9','+','=','?'])
random.shuffle(l)

#print(l)
key_id = str(random.randint(0,10000))
key_file = open("key"+str(key_id)+".txt",'wt')
#list to string
ls = ""
for i in l:
    ls = ls + str(i)
key_file.write(ls)
key_file.close()

msg = input("Type your message: " )



res = ""
for i in msg:
    idx = l.index(str(i))
    if idx == 0:
        midx = 6
    elif idx == 6:
        midx = 0
    else:
        midx = len(l) - 1 - idx
    res = res + l[midx]

print("Encoded message:",res)
msg_file = open("msg"+str(key_id)+".txt",'wt')
msg_file.write(res)
msg_file.close()

#---------------------------------------------------------------------
#Decode message
res_file = open("msg"+str(key_id)+".txt",'rt')
res = res_file.read()
res_file.close()
key_file = open("key"+str(key_id)+".txt",'rt')
key = str(key_file.read())
#print("key",key)
key_file.close()
#string to list
l = []
for i in key:
    l.append(str(i))
#print(l)

#getting encode_message 
msg_file = open("msg"+str(key_id)+".txt",'rt')
msg = msg_file.read()
msg_file.close()



dec_msg = ""
for i in msg:
    idx = l.index(str(i))
    if idx == 0:
        midx = 6
    elif idx == 6:
        midx = 0
    else:
        midx = len(l) -1 - idx
        dec_msg = dec_msg + l[midx]

print("Decoded message : {}".format(dec_msg))

#removing new files

os.remove("key"+str(key_id)+".txt")
os.remove("msg"+str(key_id)+".txt")



