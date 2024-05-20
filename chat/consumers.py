from channels.generic.websocket import WebsocketConsumer
import json


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('connected: %s' % self.scope['user'])
        self.accept()

    def disconnect(self, close_code):
        print('disconnected')

    def receive(self, text_data):
        print('receive: %s' % text_data)

        try:
            # 尝试将接收到的数据转换为整数
            value = int(text_data)
            # 将该值乘以 2
            result = value * 2
            # 将结果转换为字符串并发送回客户端
            self.send(text_data=json.dumps({'result': result}))
        except ValueError:
            # 如果接收到的值不是一个有效的整数，发送错误消息
            self.send(text_data=json.dumps({'error': 'Invalid input. Please send a number.'}))

    def chat_message(self, event):
        pass
