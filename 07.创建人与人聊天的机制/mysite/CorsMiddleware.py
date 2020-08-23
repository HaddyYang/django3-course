from django.utils.deprecation import MiddlewareMixin


# 跨域处理中间件
class Cors(MiddlewareMixin):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        if request.method == 'OPTIONS':
            response["Access-Control-Allow-Headers"] = 'Content-Type'
            response["Access-Control-Allow-Methods"] = 'GET,POST,PUT,PATCH,DELETE'
        return response
