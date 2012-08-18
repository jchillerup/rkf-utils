#!/usr/bin/python2

from Crypto.Cipher import DES
# from Crypto.Util import strxor

def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    
    return reduce(lambda x,y:x+y, lst)

def strxor(s1, s2):
    return "".join(map(lambda x, y: chr(ord(x) ^ ord(y)), s1, s2))

def rkf_des_mac(plain, key):
    iv = "\x00"*8

    padding_length = (8-(len(plain) % 8))%8
    padding = "\x00" * padding_length;

    plain += padding
    
    des_obj = DES.new(key, DES.MODE_ECB)

    mac = iv
    
    # loop through blocks of 8 chars
    for i in range(0, len(plain), 8):
        curPlain = plain[i:(i+8)]
        mac = des_obj.encrypt(strxor(curPlain, mac))
                
    return mac;


key = "\x01\x23\x45\x67\x89\xab\xcd\xef"
plains = ["7654321 Now is the time for ",
          "\xB2\x3D\x1C\xA6\x57\xE9\xF0\x48",
          "\x0F\x1E\x2D\x3C\x4B\x5A\x69\x78\x87\x96\xA5\xB4\xC3\xD2\xE1\xF0\xB2\x3D\x1C\xA6\x57\xE9\xF0\x48",
          "\xF3\xBE\x22\x3C\xC0\xC5",
          "\xBF\x17\xDD\x8C\x4B\x6A\x6E\x89\x82\x9E\xA5\xB4\xC4\x4D\x31\xF0\xB5\x3A\x9C\xA8\x5F\x43\xD4\xAA\xC2\x20\x19\x2D\x5B\xE9\xF0\x48\xB2\xCD\xF6"
          ]

for plain in plains:
    print "Hashing: \n"+plain+"\n"+toHex(plain)+"\n"
    print toHex(rkf_des_mac(plain, key));
    print "\n----\n"
