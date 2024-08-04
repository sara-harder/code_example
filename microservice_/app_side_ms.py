# author: Michael Hrenko

import zmq

def send_recv_req( arr_from_app ):

    #  Connect to socket
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:7170")

    # send_string applies encoding
    socket.send_string(arr_from_app)

    # Reply from MS
    arr_in_str = socket.recv_string()

    return arr_in_str