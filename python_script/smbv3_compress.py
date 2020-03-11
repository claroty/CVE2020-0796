import struct
import socket
import sys

if len(sys.argv) != 2:
	print("Usage: %s IP" % (sys.argv[0]))
	exit()

	
smb_payload ="000000b2fe534d4240000100000000000000210010000000000000000000000000000000fffe00000000000000000000000000000000000000000000000000000000000024000500010000007f000000aa9952d87063ea118a76005056b886b0700000000200000002021002000302031103000001002600000000000100200001006c6110bcde71a04e50810ffac0769c32c4c011cf86e26deb2ba923cd79cbbf7c0000"
# Adding comperssion negotiation context
smb_payload += "0300" + \
			  "0a00" +\
			  "00000000" + \
			  "0100" + \
			  "0000" + \
			  "00000000" + \
			  "0100" # Compression type

s = socket.socket(2,1)
s.connect((sys.argv[1],445))
s.send(bytes.fromhex(smb_payload))
buff_res = s.recv(4096)

smb_version = struct.unpack("<H", buff_res[72:74])[0]
print("SMB Version: " + hex(smb_version))
if buff_res.endswith(b"\x00"*4 + b"\x00"*2 + b"\x01\x00"):
	print("SMBv3: Compression (LZNT1) supported.")
s.close()