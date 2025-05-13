from common.auth.handle.auth_base_handle import AuthBaseHandle
from common.constants.authentication_type import AuthenticationType
from common.constants.permission_constants import Permission, Group, Operate, RoleConstants, Auth
from django.contrib.auth.models import AnonymousUser
from django.utils.translation import gettext_lazy as _


logger = logging.getLogger(__name__)


class FixedToken(AuthBaseHandle):
    def support(self, request, token: str, get_token_details):
        logger.debug(f"正在检查 FixedToken 支持: token={token}")
        result = token == 'passwordfordify'
        logger.debug(f"{'支持该 token' if result else ' 不支持该 token'}")
        return result

    def handle(self, request, token: str, get_token_details):
        logger.debug(" 调用 FixedToken handle 方法")

        permission_list = [
            Permission(group=Group.SYSTEM, operate=Operate.USE),
            Permission(group=Group.APPLICATION, operate=Operate.USE),
        ]

        auth_obj = Auth(
            role_list=[RoleConstants.FIXED_TOKEN],
            permission_list=permission_list,
            client_id='fixed_token',
            client_type=AuthenticationType.FIXED_TOKEN.value,
            current_role=RoleConstants.FIXED_TOKEN
        )

        logger.info("返回匿名用户 + 固定权限")
        return (AnonymousUser(), auth_obj)