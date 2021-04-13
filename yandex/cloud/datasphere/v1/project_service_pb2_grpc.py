# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.datasphere.v1 import project_pb2 as yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__pb2
from yandex.cloud.datasphere.v1 import project_service_pb2 as yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class ProjectServiceStub(object):
    """A set of methods for managing Project resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/Create',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.CreateProjectRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Update = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/Update',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.UpdateProjectRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Delete = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/Delete',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.DeleteProjectRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Open = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/Open',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.OpenProjectRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.Get = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/Get',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetProjectRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__pb2.Project.FromString,
                )
        self.List = channel.unary_unary(
                '/yandex.cloud.datasphere.v1.ProjectService/List',
                request_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.ListProjectsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.ListProjectsResponse.FromString,
                )


class ProjectServiceServicer(object):
    """A set of methods for managing Project resources.
    """

    def Create(self, request, context):
        """Creates a project in the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates the specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes the specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Open(self, request, context):
        """Opens the specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Returns the specified project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Lists projects for the specified folder.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.CreateProjectRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.UpdateProjectRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.DeleteProjectRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Open': grpc.unary_unary_rpc_method_handler(
                    servicer.Open,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.OpenProjectRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetProjectRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__pb2.Project.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.ListProjectsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.ListProjectsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.datasphere.v1.ProjectService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProjectService(object):
    """A set of methods for managing Project resources.
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
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/Create',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.CreateProjectRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/Update',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.UpdateProjectRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/Delete',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.DeleteProjectRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Open(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/Open',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.OpenProjectRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/Get',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.GetProjectRequest.SerializeToString,
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__pb2.Project.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.datasphere.v1.ProjectService/List',
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.ListProjectsRequest.SerializeToString,
            yandex_dot_cloud_dot_datasphere_dot_v1_dot_project__service__pb2.ListProjectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
