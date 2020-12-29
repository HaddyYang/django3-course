import json
import urllib


# 全部的websocket sender
CONNECTIONS = {}

# 判断用户是否已经连接
def check_connection(key):
    return key in CONNECTIONS

# 发送消息结构体
def message(sender, msg_type, msg):
    text = json.dumps({
        'sender': sender,
        'contentType': msg_type,
        'content': msg,
    })
    return {
        'type': 'websocket.send',
        'text': text
    }

async def websocket_application(scope, receive, send):
    while True:
        event = await receive()
        #print('[event] ', event)
        query_string = scope.get('query_string', b'').decode()
        qs = urllib.parse.parse_qs(query_string)
        auth = qs.get('auth', [''])[0]

        # 收到建立WebSocket连接的消息
        if event['type'] == 'websocket.connect':
            # 昵称验证
            if not auth:
                break
            if auth in CONNECTIONS:
                break

            await send({'type': 'websocket.accept'})

            # 发送好友列表
            friends_list = list(CONNECTIONS.keys())
            await send(message('system', 'friendsList', friends_list))

            # 向其他人群发消息, 有人登录了
            for other in CONNECTIONS.values():
                await other(message('system', 'addFriend', auth))
            
            # 记录
            CONNECTIONS[auth] = send

        # 收到中断WebSocket连接的消息
        elif event['type'] == 'websocket.disconnect':
            # 移除记录
            if auth in CONNECTIONS:
                CONNECTIONS.pop(auth)

            # 向其他人群发消息, 有人离线了
            for other in CONNECTIONS.values():
                await other(message('system', 'removeFriend', auth))

        # 其他情况,正常的WebSocket消息
        elif event['type'] == 'websocket.receive':
            if event['text'] == 'ping':
                await send(message('system', 'text', 'pong!'))
            else:
                receive_msg = json.loads(event['text'])
                send_to = receive_msg.get('sendTo', '')
                if send_to in CONNECTIONS:
                    content_type = receive_msg.get('contentType', 'text')
                    content = receive_msg.get('content', '')
                    msg = message(auth, content_type, content)
                    await CONNECTIONS[send_to](msg)
                else:
                    msg = message('system', 'text', '对方已下线或不存在')
                    await send(msg)
        else:
            pass

    print('[disconnect]')
    