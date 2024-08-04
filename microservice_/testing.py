# author: Michael Hrenko

import json
import app_side_ms
import time

arr_out_list = [
    [129, 88, 47, 'r'], 
    [100, 255, 255, 'r'],
    [36, 45, 170, 'r'],
    [30, 0.636, 0.506, 'u'],
    [180, 0.608, 1.00, 'u'],
    [236, 0.788, 0.667, 'u'],
    [180, 0.61, 1.00, 'u']
]

arr_in_expd_list = [
    [30, 0.636, 0.506],
    [180, 0.608, 1.00],
    [236, 0.788, 0.667],
    [129, 88, 47], 
    [100, 255, 255],
    [36, 45, 170],
    [99, 255, 255]
]

for i in range(len(arr_out_list)):

    print("test: %s" % (i+1))
    arr_out_str = json.dumps(arr_out_list[i])
    print("Sending array: %s" % arr_out_str)
    arr_recv = app_side_ms.send_recv_req(arr_out_str)
    print("Received array: %s" % arr_recv)
    print("Expected array: %s" % arr_in_expd_list[i])
    print("-----------------------\n")
    time.sleep(500/1000)
