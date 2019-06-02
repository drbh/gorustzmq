import zmq

loc = 'tcp://127.0.0.1:5555'

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt_string(zmq.SUBSCRIBE, '')
socket.connect(loc)
print(loc, "is live:", (not socket.closed))

while True:
    message = socket.recv()
    print(message)