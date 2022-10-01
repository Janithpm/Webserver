# Python modules
# Python socket module for handling web sockets
from socket import socket, AF_INET, SOCK_STREAM

# Python os module for handling file paths
import os

# Python mimetypes module for handling mime types
import mimetypes

# IP address of localhost
LOCALHOST = "127.0.0.1"
# Port number to listen on
PORT = 2728


# Function to extract method, path, parameters from the client request
def extract(header):
    # Split the header into lines and then into words
    req_header = header.split("\r\n")
    req = req_header[0].split(" ")
    method = req[0]  # The first word is the method
    url = req[1]  # The second word is the url

    path_and_params = url.split("?")  # Split the url into path and parameters
    path = path_and_params[0]  # The first part is the path

    # create a dictionary for the parameters
    params = path_and_params[1] if len(path_and_params) > 1 else ""
    params = params.split("&") if len(params) > 0 else []
    paramsObject = {}
    if params:
        paramsObject = {param.split("=")[0]: param.split("=")[1] for param in params}
    
    # return the method, path, and parameters
    return method, path, paramsObject


# Function to resolve the path of a file coresponding to request path
def resolve_path(path):
    # If the path is empty, set it to index.html
    if path == "/":
        return os.path.join(os.getcwd(), "htdocs", "index.html")

    # separate the path into segments and remove first empty segment
    segments = path.split("/")
    # remove first segment
    segments.pop(0)

    # if last segment is empty, remove it
    if segments[-1] == "":
        segments.pop(-1)

    # add .html extension to the end of the path to get the file name
    if "." not in segments[-1]:
        segments[-1] = segments[-1] + ".html"

    # join the segments to get the absolute file path
    return os.path.join(os.getcwd(), "htdocs", *segments)


# Function for genarate the response header
def response(status=404, content="", content_type="text/html"):

    # check weather type is image or not
    if "image" in content_type:
        #if image, set Accept Range to bytes and remove content length
        content_length = ""
        accept_ranges = "Accept-Ranges: bytes\r\n"
    else:
        #if not image, set content length and remove Accept Range
        content_length = f"Content-Length: {len(content)}\r\n"
        accept_ranges = ""

    # successfull responces
    if 200 <= status < 300:
        return f'HTTP/1.1 {status} OK\r\n{content_length}content-type: {content_type}\r\n{accept_ranges}\r\n'
    # client error responces
    if 400 <= status < 500:
        return f"HTTP/1.1 {status} Not Found\r\nContent-Length: {len(content)}\r\n\r\n"
    # server error responces
    if 500 <= status < 600:
        return f"HTTP/1.1 {status} Server Error\r\nContent-Length: {len(content)}\r\n\r\n"


# Handling the request
with socket(AF_INET, SOCK_STREAM) as server:

    # Bind the server to the localhost and port
    server.bind((LOCALHOST, PORT))

    # Listen for connections
    server.listen()
    print("Listening on port", PORT)

    while True:
        # Accept the client request
        client, _ = server.accept()

        recv_header = client.recv(1024).decode()

        try:
            method, path, _ = extract(recv_header)

            # Handle GET Method
            if method == 'GET':
                try:
                    file_path = resolve_path(path)
                    print("sent: ", file_path)
                    file_type = mimetypes.guess_type(file_path)[0]

                    # check weather file is a image or not
                    if "image" in file_type:
                        
                        # open file as read bytes mode
                        with open(file_path, 'rb') as f:
                            file = f.read()
                            # send the response header
                            client.send(response(status=200, content_type=file_type).encode())
                            # send the file
                            client.send(file)
                    else:
                        # get content of the file
                        with open(file_path, "r") as f:
                            content = f.read()

                        # send the response header
                        client.send(response(status=200, content=content, content_type=file_type).encode())
                        # send the content
                        client.send(content.encode())

                except FileNotFoundError:
                    # send 404 error if file not found
                    client.send(response(404).encode())
              
        except IndexError:
            # send 400 error if request is not valid
            client.send(response(400).encode())
