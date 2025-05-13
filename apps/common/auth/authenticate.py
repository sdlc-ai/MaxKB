# coding=utf-8
"""
    @project: qabot
    @Author：虎
    @file： authenticate.py
    @date：2023/9/4 11:16
    @desc:  认证类
"""
import traceback
from importlib import import_module

from django.conf import settings
from django.core import cache
from django.core import signing
from rest_framework.authentication import TokenAuthentication

from common.exception.app_exception import AppAuthenticationFailed, AppEmbedIdentityFailed, AppChatNumOutOfBoundsFailed, \
    ChatException, AppApiException
from django.utils.translation import gettext_lazy as _
token_cache = cache.caches['token_cache']


class AnonymousAuthentication(TokenAuthentication):
    def authenticate(self, request):
        return None, None


def new_instance_by_class_path(class_path: str):
    parts = class_path.rpartition('.')
    package_path = parts[0]
    class_name = parts[2]
    module = import_module(package_path)
    HandlerClass = getattr(module, class_name)
    return HandlerClass()


handles = [new_instance_by_class_path(class_path) for class_path in settings.AUTH_HANDLES]


class TokenDetails:
    token_details = None
    is_load = False

    def __init__(self, token: str):
        self.token = token

    def get_token_details(self):
        if self.token_details is None and not self.is_load:
            try:
                self.token_details = signing.loads(self.token)
            except Exception as e:
                self.is_load = True
        return self.token_details


class OpenAIKeyAuth(TokenAuthentication):
    def authenticate(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION')
        auth = auth.replace('Bearer ', '')
        # 未认证
        if auth is None:
            raise AppAuthenticationFailed(1003, _('Not logged in, please log in first'))
        try:
            token_details = TokenDetails(auth)
            for handle in handles:
                if handle.support(request, auth, token_details.get_token_details):
                    return handle.handle(request, auth, token_details.get_token_details)
            raise AppAuthenticationFailed(1002, _('Authentication information is incorrect! illegal user'))
        except Exception as e:
            traceback.format_exc()
            if isinstance(e, AppEmbedIdentityFailed) or isinstance(e, AppChatNumOutOfBoundsFailed) or isinstance(e,
                                                                                                                 AppApiException):
                raise e
            raise AppAuthenticationFailed(1002, _('Authentication information is incorrect! illegal user'))


class TokenAuth(TokenAuthentication):
    # 重新 authenticate 方法，自定义认证规则
    def authenticate(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION')
        # 未认证
        if auth is None:
            raise AppAuthenticationFailed(1003, _('Not logged in, please log in first'))
        try:
            token_details = TokenDetails(auth)
            for handle in handles:
                if handle.support(request, auth, token_details.get_token_details):
                    return handle.handle(request, auth, token_details.get_token_details)
            raise AppAuthenticationFailed(1002, _('Authentication information is incorrect! illegal user'))
        except Exception as e:
            traceback.format_exc()
            if isinstance(e, AppEmbedIdentityFailed) or isinstance(e, AppChatNumOutOfBoundsFailed) or isinstance(e,
                                                                                                                 AppApiException):
                raise e
            raise AppAuthenticationFailed(1002, _('Authentication information is incorrect! illegal user'))


logger = logging.getLogger(__name__)

class FixedTokenAuthentication(TokenAuthentication):
    fixed_token = 'passwordfordify'

    def authenticate(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION')

        logger.debug("开始 FixedTokenAuthentication 认证")

        if auth is None:
            logger.warning("没有提供 Authorization")
            raise AppAuthenticationFailed(403, _('The request is denied because of missing access permissions...'))

        try:
            scheme, token = auth.split()
            if scheme.lower() != 'bearer':
                logger.warning(f"非法 Token 类型: {scheme}")
                raise AppAuthenticationFailed(403, _('Invalid token scheme'))
        except ValueError:
            logger.warning("Token 格式错误")
            raise AppAuthenticationFailed(403, _('Invalid token header'))

        if token != self.fixed_token:
            logger.warning(f"Token 不匹配: {token}")
            return None  # 让其他 handler 处理

        logger.info(" Token 匹配成功，进入 handle 流程")

        from common.auth.handle.impl.fixed_token import FixedToken
        return FixedToken().handle(request, token, lambda: None)

    def authenticate_header(self, request):
        return 'Bearer'