import os
import json
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .websocket import check_connection


def home(request):
    path = os.path.join(settings.BASE_DIR, 'static', 'index.html')
    html = ''
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    return HttpResponse(html)
    
def login(request):
    try:
        if request.method != 'POST':
            raise Exception('请求无效')

        # 获取数据
        data = request.body.decode()
        data = json.loads(data)
        # 简单判断
        if not data.get('nickname', ''):
            raise Exception('没有设置昵称')
        # 判断该昵称是否被使用
        nickname = data['nickname']
        if check_connection(nickname):
            raise Exception('该昵称已被使用，无法建立连接')

        # 验证通过
        auth = nickname  # 暂时使用昵称作为标识
        return JsonResponse({'status': 1, 'auth': auth})
    except Exception as e:
        return JsonResponse({'status': 0, 'err': str(e)})
