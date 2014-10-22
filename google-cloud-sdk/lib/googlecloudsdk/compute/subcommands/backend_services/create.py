# Copyright 2014 Google Inc. All Rights Reserved.
"""Command for creating backend services."""

from googlecloudsdk.compute.lib import backend_services_utils
from googlecloudsdk.compute.lib import base_classes


class Create(base_classes.BaseAsyncCreator):
  """Create a backend service."""

  @staticmethod
  def Args(parser):
    backend_services_utils.AddUpdatableArgs(
        parser, http_health_check_required=True)

    parser.add_argument(
        'name',
        help='The name of the backend service.')

  @property
  def service(self):
    return self.compute.backendServices

  @property
  def method(self):
    return 'Insert'

  @property
  def resource_type(self):
    return 'backendServices'

  def CreateRequests(self, args):
    health_checks = [self.CreateGlobalReference(
        args.http_health_check, resource_type='httpHealthChecks').SelfLink()]

    backend_services_ref = self.CreateGlobalReference(args.name)

    request = self.messages.ComputeBackendServicesInsertRequest(
        backendService=self.messages.BackendService(
            description=args.description,
            healthChecks=health_checks,
            name=backend_services_ref.Name(),
            port=args.port,
            portName=args.port_name,
            timeoutSec=args.timeout),
        project=self.project)

    return [request]


Create.detailed_help = {
    'brief': 'Create a backend service',
    'DESCRIPTION': """
        *{command}* is used to create backend services. Backend
        services define groups of backends that can receive
        traffic. Each backend group has parameters that define the
        group's capacity (e.g., max CPU utilization, max queries per
        second, ...). URL maps define which requests are sent to which
        backend services.

        Backend services created through this command will start out
        without any backend groups. To add backend groups, use 'gcloud
        compute backend-services add-backend' or 'gcloud compute
        backend-services edit'.
        """,
}
