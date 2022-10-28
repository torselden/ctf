#!/bin/env python3

from pwn import remote
from pprint import pprint as pp


HOST = '161.35.33.243'
PORT = 32470

def main ():

    there_is_data = True

    conn = remote(HOST, PORT)

    while True:
        data = conn.recvuntil([b"meeting?",b"}"])
        if b"HTB" in data:
            pp(data.split(b'\n'))
            conn.close()
            exit(0)

        conn.sendline(b"sup3r_s3cr3t_p455w0rd_f0r_u\!")
        data = conn.recvuntil([b"}"])
        pp(data.split(b'\n'))
        


if __name__ == '__main__':
    main()