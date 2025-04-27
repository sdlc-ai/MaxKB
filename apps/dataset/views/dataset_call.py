from drf_yasg.utils import swagger_auto_schema
from poetry.json import ValidationError
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.views import Request

from common.auth import TokenAuth, has_permissions, FixedTokenAuthentication
from common.response import result
from common.log.log import log
from common.swagger_api.common_api import CommonApi
from dataset.serializers.dataset_serializers import DataSetSerializers
from dataset.views.common import get_dataset_operation_object
from django.utils.translation import gettext_lazy as _


class DatasetCall(APIView):
    authentication_classes = [FixedTokenAuthentication]

    class Retrieval(APIView):
        authentication_classes = [FixedTokenAuthentication]

        @action(methods="POST", detail=False)
        @swagger_auto_schema(operation_summary=_('Retrieval hit list'), operation_id=_('Hit test list'),
                             manual_parameters=CommonApi.HitTestApi.get_request_params_api(),
                             responses=result.get_api_array_response(CommonApi.HitTestApi.get_response_body_api()),
                             tags=[_('Knowledge Base')])
        @log(menu='Knowledge Base', operate="Retrieval hit the knowledge from external",
             get_operation_object=lambda r, keywords: get_dataset_operation_object(keywords.get('dataset_id')))
        def post(self, request: Request):
            try:
                data = request.data

                self.validate_request(data)

                # 获取请求参数
                knowledge_id = data['knowledge_id']
                query = data['query']
                retrieval_setting = data['retrieval_setting']

                # 返回结果
                return result.success(
                    DataSetSerializers.HitTest(data={'id': knowledge_id, 'user_id': request.user.id,
                                                     "query_text": query,
                                                     "top_number": retrieval_setting['top_k'],
                                                     'similarity': retrieval_setting['score_threshold'],
                                                     'search_mode': "embedding"}).hit_test(
                    ))

            except ValidationError as e:
                return result.error(message=str(e), code=1003)
            except Exception as e:
                return result.error(message=str(e), code=2002)

        def validate_request(self, data):
            required_fields = ['knowledge_id', 'query', 'retrieval_setting']
            for field in required_fields:
                if field not in data:
                    raise ValidationError(f"Missing required field: {field}")

            required_retrieval_fields = ['top_k', 'score_threshold']
            for field in required_retrieval_fields:
                if field not in data['retrieval_setting']:
                    raise ValidationError(f"Missing required field in retrieval_setting: {field}")

            # if 'metadata_condition' in data:
            #     if 'conditions' not in data['metadata_condition']:
            #         raise ValidationError("Missing required field 'conditions' in metadata_condition")
            #     for condition in data['metadata_condition']['conditions']:
            #         required_condition_fields = ['name', 'comparison_operator']
            #         for field in required_condition_fields:
            #             if field not in condition:
            #                 raise ValidationError(f"Missing required field in metadata_condition conditions: {field}")
