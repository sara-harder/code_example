# author: Michael Hrenko

import zmq
import json
import color_conversion

#  Connect to socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:7170")

# Listen for incoming requests
while True:

    # recv_string applies decoding
    arr_in_str = socket.recv_string()
    # print("Received array: %s" % arr_in_str)
   
    arr_in_full = eval(arr_in_str)
    
    # Array with the RGB or HSV values, not the last r or u.
    arr_in = arr_in_full[:3]

    # Convert RGB to HSV
    if arr_in_full[3] == 'r':
        arr_out = color_conversion.RGB_to_HSV(arr_in)

    # Convert HSV to RGB
    elif arr_in_full[3] == 'u':
        arr_out = color_conversion.HSV_to_RGB(arr_in)
    
    # json.dumps is akin to json.stringify in JS
    arr_out_str = json.dumps(arr_out)
    
    # Send to app-side MS
    socket.send_string(arr_out_str)