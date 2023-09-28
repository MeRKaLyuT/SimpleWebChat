from django.test import TestCase
import websocket
import time


# def on_message(ws, message):
#    print(f"Received message: {message}")
#
# def on_error(ws, error):
#    print(f"Error occurred: {error}")
#
# def on_close(ws, close_status_code, close_msg):
#    print("WebSocket connection closed")
#
# websocket.enableTrace(True)  # Для отладки
# ws = websocket.WebSocketApp("ws://localhost:8000/chat/1/",  # Замените <chat_id> на конкретный chat_id
#                            on_message=on_message,
#                            on_error=on_error,
#                            on_close=on_close)
#
# ws.run_forever()

array = [2, 11, 7, 15]
target = 9
output = []
index = []


def Solution(array, target):
    for i in array:
        for b in array:
            if i + b == target:
                output.append(i)
                for d in output:
                    index = [num for num in enumerate(array) if num == i]

    print(output)
    print(index)


Solution(array, target)