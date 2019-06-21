from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response


class RequestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print('process_request middlewares')
        if request.POST:
            request.data = request.POST
        # if request.method == 'POST' and request.content_type == 'application/x-www-form-urlencoded':
        #     request.data = request.POST


