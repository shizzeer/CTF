#!/usr/bin/python2

from z3 import *
from hashlib import sha512
import sys

def verify(x, chalbox):
    length, gates, check = chalbox              # length --> length of the key, gates --> logical gates, check --> checking gate
    b = [(x >> i) & 1 for i in range(length)]   # reversed key
    for name, args in gates:                    # name --> name of the current gate, args --> values to compute
        if name == 'true':
            b.append(1)
        else:
            u1 = b[args[0][0]] ^ args[0][1]     # calculations of the exact bits of the key
            u2 = b[args[1][0]] ^ args[1][1]
            if name == 'or':
                b.append(u1 | u2)
            elif name == 'xor':
                b.append(u1 ^ u2)
    return b[check[0]] ^ check[1]               # last check using checking gate - this is the target of the z3 Solver
    
def dec(x, w):
    z = int(sha512(str(int(x))).hexdigest(), 16)
    return '{:x}'.format(w ^ z).decode('hex')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'Usage: ' + sys.argv[0] + ' <key> <map.txt>'
        print 'Example: Try Running ' + sys.argv[0] + ' 11443513758266689915 map1.txt'
        exit(1)
    with open(sys.argv[2], 'r') as f:
        cipher, chalbox = eval(f.read())
    
    key = int(sys.argv[1]) % (1 << chalbox[0])

    # This code is added
    s = Solver()
    solvers_key = BitVec('solvers_key', int(chalbox[0]))    # chalbox[0] is the length of the key
    s.add(verify(solvers_key, chalbox) == True)             # constraint to get the correct key
    if s.check() == sat:                                    # if problem is satisfiable then print the correct key
        print s.model()


    if verify(key, chalbox):
        print 'Congrats the flag for ' + sys.argv[2] + ' is:', dec(key, cipher)
    else:
        print 'Wrong key for ' + sys.argv[2] + '.'
