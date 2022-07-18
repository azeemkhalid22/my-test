import base64

a="Abdur Rehman".encode("utf-8")

encoded= base64.b64encode(a)

print(encoded)

print(base64.b64decode(encoded))