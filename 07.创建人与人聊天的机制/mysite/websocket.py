import urllib


CONNECTIONS = {}

async def websocket_application(scope, receive, send):
    while True:
        event = await receive()
        print('[event] ', event)

        # 收到建立WebSocket连接的消息
        if event['type'] == 'websocket.connect':
            await send({'type': 'websocket.accept'})

            # 得到auth
            query_string = scope.get('query_string', b'').decode()
            qs = urllib.parse.parse_qs(query_string)
            auth = qs.get('auth', [''])[0]

            # 记录send对象
            CONNECTIONS[auth] = send

        # 收到中断WebSocket连接的消息
        elif event['type'] == 'websocket.disconnect':
            break

        # 其他情况,正常的WebSocket消息
        elif event['type'] == 'websocket.receive':
            if event['text'] == 'ping':
                await send({
                    'type': 'websocket.send',
                    'text': 'pong!'
                })
        else:
            pass

    print('[disconnect]')
    