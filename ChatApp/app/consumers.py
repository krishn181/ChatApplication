from channels.consumer import SyncConsumer
from .models import Chat, Group
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json

class MySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print("Connection form server....", event)
        self.send({
            'type':'websocket.accept'
        })
        self.group = self.scope['url_route']['kwargs']['group_name']
        async_to_sync(self.channel_layer.group_add)(self.group, self.channel_name)
        print("Channel Layer.....", self.channel_layer)
        print("Group name.....", self.group)
        print("Channel Name.....", self.channel_name)

    def websocket_receive(self, event):
        print("Websocket receiver.....", event)
        print("text",event['text'])
        data = json.loads(event['text'])
        message = data['msg']
        print("this is message.....", message)
        self.group = self.scope['url_route']['kwargs']['group_name']
        try:
            group = Group.objects.get(name = self.group)
        except Group.DoesNotExist:
            return
        username = self.scope['user'].username
        if self.scope['user'].is_authenticated:
            chat = Chat(content=message, group=group, user = self.scope['user'])
            chat.save()
            
            async_to_sync(self.channel_layer.group_send)(self.group,
                {
                    'type':'chat.message',
                    'message':message,
                    'username':username,
                }
            )

        else:
            self.send({
                    'type':'websocket.send',
                    'text':json.dumps({'msg':'Login required'})
                    }
                )

    def chat_message(self, event):
        message = event['message']
        username = event['username']
        self.send({ 
                    'type':'websocket.send',
                    'text':json.dumps({'msg':message, 'username':username}),                    
                    }
                )    

    def websocket_disconnect(self, event):
        self.group = self.scope['url_route']['kwargs']['group_name']
        async_to_sync(self.channel_layer.group_discard)(self.group, self.channel_name)        
        raise StopConsumer