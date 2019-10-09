import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class TimeItMiddleware(MiddlewareMixin):
    """旧版"""
    # 1 请求来到middleware中时进入的第一个方法
    def process_request(self,request):
        self.start_time = time.time()
        return

    # 2 该方法在process_request后执行
    def process_view(self,request,func,*args,**kwargs):
        if request.path !=reverse('index'):
            return None
        start = time.time()
        response = func(request)
        costed = time.time() - start
        print('process view:{:.2f}s'.format(costed))
        return response

    def procss_exception(self,request,exception):
        pass
    # 3
    def process_template_response(self,request,response):
        return response
    # 4
    def process_response(self,request,response):
        costed = time.time() - self.start_time
        print('request to response cose:{:.2f}s'.format(costed))
        return response

# class TimeItMiddleware(MiddlewareMixin):
#     # """新版"""
#     def __init__(self,get_response=None):
#         self.get_response = get_response
#         super(MiddlewareMixin,self).__init__()
#
#     def __call__(self, request):
#         response = None
#         self.start_time = time.time()
#         if hasattr(self, 'process_request'):
#             response = self.process_request(request)
#         response = response or self.get_response(request)
#         if hasattr(self, 'process_response'):
#             response = self.process_response(request, response)
#         costed = time.time() - self.start_time
#         print('request to response cose:{:.2f}s'.format(costed))
#         return response
