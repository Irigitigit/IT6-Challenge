import socket

HOST = '192.168.1.10'
PORT = 8888

pin = 132

# Create the request
pin_str = f"{pin:03d}"
body = f"magicNumber={pin_str}"
headers = (
    "POST /verify HTTP/1.1\r\n"
    f"Host: {HOST}:{PORT}\r\n"
    "Content-Type: application/x-www-form-urlencoded\r\n"
    f"Content-Length: {len(body)}\r\n"
    "Connection: close\r\n"
    "\r\n"
)
request = headers + body

# Send the request
sock = socket.create_connection((HOST, PORT))
sock.sendall(request.encode())

# Receive the response
response = b""
while True:
    chunk = sock.recv(4096)
    if not chunk:
        break
    response += chunk
sock.close()

# Decode and print the server response
print(response.decode(errors="ignore"))
