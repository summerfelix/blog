import re
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from backweb.models import Admin


class LoginStatusMiddle(MiddlewareMixin):

    def process_request(self, request):
        # 不需要做登录校验的地址
        if re.match('/web/.*', request.path):
            return None
        if re.match('/media/.*', request.path):
            return None
        # if re.match('/api/.*', request.path):
        #     return None
        if request.path in ['/backweb/login/']:
            return None

        admin_id = request.session.get('admin_id')

        if admin_id:
            admin = Admin.objects.filter(pk=admin_id)
            request.admin = admin
            return None
        else:
            return HttpResponseRedirect('/backweb/login/')
