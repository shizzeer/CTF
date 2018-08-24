#!/usr/bin/python3

key = [0x18, 0xD6, 0x15, 0xCA, 0xFA, 0x77]
decryption_flag = [0x50, 0xB3, 0x67, 0xAF, 0xA5, 0x0E, 0x77, 0xA3, 0x4A, 0xA2, 0x9B, 0x01, 0x7D, 0x89, 0x61, 0xA5, 0xA5, 0x02, 0x76, 0xB2, 0x70, 0xB8, 0x89, 0x03, 0x79, 0xB8, 0x71, 0x95, 0x9B, 0x28, 0x74, 0xBF, 0x61, 0xBE, 0x96, 0x12, 0x47, 0x95, 0x3E, 0xE1, 0xA5, 0x04, 0x6C, 0xA3, 0x73, 0xAC, 0x89]

print(''.join(map(chr, [decryption_flag[i] ^ key[i % len(key)] for i in range(len(decryption_flag))])))
