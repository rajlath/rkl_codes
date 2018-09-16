import platform
import cpuinfo
import os
import getpass
import socket
def convert_2_ascii(st):
    rets = ''
    for i in st:
        rets += str(ord(i))
    return rets

def create_key():
    keys = ''
    keys += convert_2_ascii("1FAA")
    keys += convert_2_ascii(platform.version())
    keys += convert_2_ascii(getpass.getuser()[::-1])
    keys += convert_2_ascii(platform.architecture()[1])
    keys += convert_2_ascii(platform.platform())
    keys += convert_2_ascii(str(os.cpu_count()))
    keys += convert_2_ascii(socket.gethostname())
    return keys

print(create_key())