import cv2
import zmq
import base64
import time
import datetime

context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.connect('tcp://localhost:5555')
footage_socket.bind('tcp://127.0.0.1:5555')

print("Current libzmq version is %s" % zmq.zmq_version())
print("Current  pyzmq version is %s" % zmq.__version__)

messagedata = str(datetime.datetime.now())
while True:
    try:
        footage_socket.send_string(messagedata)

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        print("\n\nBye bye\n")
        break

    # time.sleep(.1)
    # time.sleep(.25)
    time.sleep(.5)