# Color Conversion Microservice

Convert an RGB color array to HSV, and HSV to RGB

The microservice performs the conversion of values between RGB colors and HSB colors. The microservice will take either an RGB or an HSB color value as the request, and it will send back the corresponding HSB/RGB value as the response.

## Brief summary of send/receive steps for interacting with the microservice (see detailed outline below)
1. Run **ms_side.py**
2. In the React app, send a stringified array to the function **send_recv_req** in the **app_side_ms.py** program. When conversion is complete, **send_recv_req** will return a converted stringified array to the React app.

## How to request data from the microservice (detailed outline)
1. Run **ms_side.py** to load the "server" side of the microservice at port 7170 using the ZeroMQ framework.  
2. The React app should send a stringified array to the function **send_recv_req** in the **app_side_ms.py** program (you don't need to run the app_side_ms.py program)
3. **app_side_ms.py** will initialize the socket connection at the same port in step #1 using the ZeroMQ framework.
4. The function **send_recv_req** will send the stringified array to port 7170.
5. **ms_side.py**, which is listening at port 7170, will ingest this stringified array, transform it to a list, and pass the list to the program **color_conversion.py** to perform the microservice described above. 

Note: the list array [129, 88, 47, 'r'] converts to the stringified array "[129, 88, 47, "r"]" when using json.dumps in python. 

## How to receive data from the microservice (detailed outline)

6. After conversion is complete, **color_conversion.py** returns the converted list array to **ms_side.py**
7. **ms_side.py** will ingest this list array, transform it to a stringified array, and send it to port 7170.
8.  **app_side_ms.py** receives this stringified array, and passes it back to the React app. 

## UML diagram describing the flow

In the example below, we convert the stringified RGB array "[129, 88, 47, 'r']" to the stringified HSV array "[30, 0.636, 0.506]".

![ColorFlow](https://user-images.githubusercontent.com/91226165/236582892-68e4a891-ce13-4d1c-891e-698fbec1ffc1.png)

## Testing results

I used testing.py to act as the React app. Here's the results of my tests. Most of the values are close to the expected.

![Testing](https://user-images.githubusercontent.com/91226165/236566283-de52c168-25ab-4e4e-b0c6-6f5a5cd7ba4f.png)

