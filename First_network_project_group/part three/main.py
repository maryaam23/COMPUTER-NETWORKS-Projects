from socket import *
import urllib.request

serverPort = 9977
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("192.168.1.109", serverPort))
serverSocket.listen(1)
print("The web server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print("Received sentence:", sentence)
    ip = addr[0]
    port = addr[1]
    sentence_parts = sentence.split()
    if len(sentence_parts) >= 2:
        object = sentence_parts[1]
        print("Requested object:", object)

        if object == '/' or object == '/index.html' or object == '/main_en.html' or object == '/en':
            connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
            connectionSocket.send("Content-Type: text/html \r\n".encode())
            connectionSocket.send("\r\n".encode())
            file1 = open("main_en.html", "rb")
            connectionSocket.send(file1.read())

        elif object == '/ar':
            connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
            connectionSocket.send("Content-Type: text/html \r\n".encode())
            connectionSocket.send("\r\n".encode())
            file2 = open("main_ar.html", "rb")
            connectionSocket.send(file2.read())

        elif object.endswith('.html'):
            connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
            connectionSocket.send("Content-Type: text/html \r\n".encode())
            connectionSocket.send("\r\n".encode())
            file3 = open("Link.html", "rb")
            connectionSocket.send(file3.read())

        elif object.endswith('.css'):
            connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
            connectionSocket.send("Content-Type: text/css \r\n".encode())
            connectionSocket.send("\r\n".encode())
            file4 = open("cssFile.css", "rb")
            connectionSocket.send(file4.read())



        elif object.endswith('.png'):
            url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ2ZE3oq8SzGWmH6wIEIDFiMtTI9zTLxxLHXA&usqp=CAU.png"
            connectionSocket.send("HTTP/1.1 200 OK \r\n".encode())
            connectionSocket.send("Content-Type: image/png \r\n".encode())
            connectionSocket.send("\r\n".encode())
            # Download the image from the URL and save it locally
            urllib.request.urlretrieve(url, "image.png")
            # Open the local image file and send its content
            file5 = open("image.png", "rb")
            connectionSocket.send(file5.read())


        elif object.endswith(".jpg"):

            url = "https://i.imgur.com/fvrP7rn.jpg"
            connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
            connectionSocket.send("Content-Type: image/jpg \r\n".encode())
            connectionSocket.send("\r\n".encode())
            # Download the image from the URL and save it locally
            urllib.request.urlretrieve(url, "image.jpg")
            # Open the local image file and send its content
            file5 = open("image.jpg", "rb")
            connectionSocket.send(file5.read())




        elif object == '/yt':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
            connectionSocket.send("Content-Type: text/html \r\n".encode())
            connectionSocket.send("Location: https://www.youtube.com/ \r\n".encode())
            connectionSocket.send("\r\n".encode())

        elif object == '/so':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
            connectionSocket.send("Content-Type: text/html \r\n".encode())
            connectionSocket.send("Location: https://stackoverflow.com \r\n".encode())
            connectionSocket.send("\r\n".encode())

        elif object == '/rt':
            connectionSocket.send("HTTP/1.1 307 Temporary Redirect \r\n".encode())
            connectionSocket.send("Content-Type: text/html \r\n".encode())
            connectionSocket.send("Location: https://ritaj.birzeit.edu// \r\n".encode())
            connectionSocket.send("\r\n".encode())





        else:
            error_message = f'''HTTP/1.1 404 Not Found <html> <head> <title>Error 404</title> <style>
                            body {{  
                            background-repeat: no-repeat;
                            background-attachment: fixed;
                            background-size: 100% 100%;  }}
                            h1 {{ margin-top: 80px; color: red; font-weight: bold; text-align: center; }}
                            h2 {{background-color: #4682B4; 
                            border-radius: 20px;
                            color: white;
                            font-weight: bold;
                            text-align: center;
                            font-family: "Roboto", Arial, sans-serif;
                            font-size: 18px;
                            padding: 20px;
                            margin: 25px auto;
                            max-width: 450px;
                            letter-spacing: 1px;}} 
                            </style> </head> <body> <h1>The file is not found</h1>
                            <h2>Mariam Hamad - 1200837</h2>
                            <h2>Leena Affouri - 1200335</h2>
                            <h2>Nirmeen Al-sheikh - 1200200</h2>
                            <h2><b>Client IP: {ip}</b></p>
                            <h2><b>Client Port: {port}</b></p> </body> </html> '''.encode('utf-8')
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
            connectionSocket.send("Content-Type: text/html\r\n".encode())
            connectionSocket.send("\r\n".encode())
            connectionSocket.send(error_message)
            connectionSocket.close()
    else:
            print("Invalid request format:", sentence)
            # Add appropriate error handling or send a 400 Bad Request response