# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.iam.v1 import iam_token_service_pb2 as yandex_dot_cloud_dot_iam_dot_v1_dot_iam__token__service__pb2


class IamTokenServiceStub(object):
    """A set of methods for managing IAM tokens.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/yandex.cloud.iam.v1.IamTokenService/Create',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_iam__token__service__pb2.CreateIamTokenRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_iam__token__service__pb2.CreateIamTokenResponse.FromString,
                )
        self.CreateForServiceAccount = channel.unary_unary(
                '/yandex.cloud.iam.v1.IamTokenService/CreateForServiceAccount',
                request_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_iam__token__service__pb2.CreateIamTokenForServiceAccountRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_iam__token__service__pb2.CreateIamTokenResponse.FromString,
                )


class IamTokenServiceServicer(object):
    """A set of methods for managing IAM tokens.
    """

    def Create(self, request, context):
        """Creates an IAM token for the specified identity.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateForServiceAccount(self, request, context):
        """Create iam token for service account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IamTokenServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_iam__token__service__pb2.CreateIamTokenRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_iam__token__service__pb2.CreateIamTokenResponse.SerializeToString,
            ),
            'CreateForServiceAccount': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateForServiceAccount,
                    request_deserializer=yandex_dot_cloud_dot_iam_dot_v1_dot_iam__token__service__pb2.CreateIamTokenForServiceAccountRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iam_dot_v1_dot_iam__token__service__pb2.CreateIamTokenResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.iam.v1.IamTokenService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IamTokenService(object):
    """A set of methods for managing IAM tokens.
    """

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.iam.v1.IamTokenService/Create',
            yandex_dot_cloud_dot_iam_dot_v1_dot_iam__token__service__pb2.CreateIamTokenRequest.SerializeToString,
            yandex_dot_cloud_dot_iam_dot_v1_dot_iam__token__service__pb2.CreateIamTokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateForServiceAccount(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.iam.v1.IamTokenService/CreateForServiceAccount',
            yandex_dot_cloud_dot_iam_dot_v1_dot_iam__token__service__pb2.CreateIamTokenForServiceAccountRequest.SerializeToString,
            yandex_dot_cloud_dot_iam_dot_v1_dot_iam__token__service__pb2.CreateIamTokenResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
