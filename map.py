#!/usr/bin/python

import re
import string

coded_message = r"g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def trans(m):
    c = m.group(0)
    alphabet = string.ascii_lowercase
    position = alphabet.find(c)
    
    if position != -1:
        return alphabet[(position + 2) % len(alphabet)]
    else:
        return c
    
print re.sub(r'\w', trans, coded_message)
