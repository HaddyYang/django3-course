import os
import json
from django.http import HttpResponse, JsonResponse
from django.conf import settings


def login(request):
    try:
        if request.method != 'POST':
            raise Exception('无效的请求方式')

        # 获取数据
        data = request.body.decode()
        data = json.loads(data)

        # 验证数据
        nickname = data.get('nickname', '')
        if nickname == '':
            raise Exception('缺少必要的参数')

        # 数据验证，返回auth
        auth = nickname
        return JsonResponse({'status': 1, 'auth': auth})
    except Exception as e:
        return JsonResponse({'status': 0, 'message': str(e)})
