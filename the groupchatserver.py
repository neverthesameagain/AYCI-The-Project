
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

#This part deals with accepting all incoming connections
def accept_incoming_connections():
    while True:
        client, client_address = SERVER.accept()
        #Tells Everyone this user joined
        print("%s:%s has connected." % client_address)
        #asks the user his name
        client.send(bytes("Greetings from the cave! Now type your name and press enter!", "utf8"))
        addresses[client] = client_address
        #defines functions that can take place on the thread
        Thread(target=receivingandsending, args=(client,)).start()


def receivingandsending(client):  # recieves messages from the users.
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % name
    client.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name
    sendtoallthreads(bytes(msg, "utf8"))
    clients[client] = name

    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            sendtoallthreads(msg, name+": ")
        else:
            client.send(bytes("{quit}", "utf8"))
            client.close()
            del clients[client]
            sendtoallthreads(bytes("%s has left the chat." % name, "utf8"))
            break


def sendtoallthreads(msg, prefix=""):  #  defines how the message is sent to all its users
    for sock in clients:
        sock.send(bytes(prefix, "utf8")+msg)

        
clients = {}
addresses = {}
HOST = "127.0.0.1"
PORT = 3000
BUFSIZ = 1024
ADDR = (HOST, PORT)

SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
