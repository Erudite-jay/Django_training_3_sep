from channels.consumer import SyncConsumer

class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self,event):
        self.send({
            'type': 'websocket.accept',   
        })
    
    def websocket_receive(self, event):
        print('Received message from client ', event)
        self.send({
            'type': 'websocket.send',
            'text': 'Hello from ws side!'
        })

    def websocket_disconnect(self, event):
        self.send({
            'type': 'websocket.close',
            'reason': 'Client disconnected'
        })
        print('Client disconnected')