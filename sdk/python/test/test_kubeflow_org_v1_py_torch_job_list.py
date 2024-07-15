# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.8.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

from kubeflow.training.models import *
from kubeflow.training.models.kubeflow_org_v1_py_torch_job_list import KubeflowOrgV1PyTorchJobList  # noqa: E501
from kubeflow.training.rest import ApiException

class TestKubeflowOrgV1PyTorchJobList(unittest.TestCase):
    """KubeflowOrgV1PyTorchJobList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KubeflowOrgV1PyTorchJobList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubeflow.training.models.kubeflow_org_v1_py_torch_job_list.KubeflowOrgV1PyTorchJobList()  # noqa: E501
        if include_optional :
            return KubeflowOrgV1PyTorchJobList(
                api_version = '0', 
                items = [
                    kubeflow_org_v1_py_torch_job.KubeflowOrgV1PyTorchJob(
                        api_version = '0', 
                        kind = '0', 
                        metadata = None, 
                        spec = kubeflow_org_v1_py_torch_job_spec.KubeflowOrgV1PyTorchJobSpec(
                            elastic_policy = kubeflow_org_v1_elastic_policy.KubeflowOrgV1ElasticPolicy(
                                max_replicas = 56, 
                                max_restarts = 56, 
                                metrics = [
                                    None
                                    ], 
                                min_replicas = 56, 
                                n_proc_per_node = 56, 
                                rdzv_backend = '0', 
                                rdzv_conf = [
                                    kubeflow_org_v1_rdzv_conf.KubeflowOrgV1RDZVConf(
                                        key = '0', 
                                        value = '0', )
                                    ], 
                                rdzv_host = '0', 
                                rdzv_id = '0', 
                                rdzv_port = 56, 
                                standalone = True, ), 
                            nproc_per_node = '0', 
                            pytorch_replica_specs = {
                                'key' : kubeflow_org_v1_replica_spec.KubeflowOrgV1ReplicaSpec(
                                    replicas = 56, 
                                    restart_policy = '0', 
                                    template = None, )
                                }, 
                            run_policy = kubeflow_org_v1_run_policy.KubeflowOrgV1RunPolicy(
                                active_deadline_seconds = 56, 
                                backoff_limit = 56, 
                                clean_pod_policy = '0', 
                                scheduling_policy = kubeflow_org_v1_scheduling_policy.KubeflowOrgV1SchedulingPolicy(
                                    min_available = 56, 
                                    min_resources = {
                                        'key' : None
                                        }, 
                                    priority_class = '0', 
                                    queue = '0', 
                                    schedule_timeout_seconds = 56, ), 
                                suspend = True, 
                                ttl_seconds_after_finished = 56, ), ), 
                        status = kubeflow_org_v1_job_status.KubeflowOrgV1JobStatus(
                            completion_time = None, 
                            conditions = [
                                kubeflow_org_v1_job_condition.KubeflowOrgV1JobCondition(
                                    last_transition_time = None, 
                                    last_update_time = None, 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            last_reconcile_time = None, 
                            replica_statuses = {
                                'key' : kubeflow_org_v1_replica_status.KubeflowOrgV1ReplicaStatus(
                                    active = 56, 
                                    failed = 56, 
                                    label_selector = None, 
                                    selector = '0', 
                                    succeeded = 56, )
                                }, 
                            start_time = None, ), )
                    ], 
                kind = '0', 
                metadata = None
            )
        else :
            return KubeflowOrgV1PyTorchJobList(
                items = [
                    kubeflow_org_v1_py_torch_job.KubeflowOrgV1PyTorchJob(
                        api_version = '0', 
                        kind = '0', 
                        metadata = None, 
                        spec = kubeflow_org_v1_py_torch_job_spec.KubeflowOrgV1PyTorchJobSpec(
                            elastic_policy = kubeflow_org_v1_elastic_policy.KubeflowOrgV1ElasticPolicy(
                                max_replicas = 56, 
                                max_restarts = 56, 
                                metrics = [
                                    None
                                    ], 
                                min_replicas = 56, 
                                n_proc_per_node = 56, 
                                rdzv_backend = '0', 
                                rdzv_conf = [
                                    kubeflow_org_v1_rdzv_conf.KubeflowOrgV1RDZVConf(
                                        key = '0', 
                                        value = '0', )
                                    ], 
                                rdzv_host = '0', 
                                rdzv_id = '0', 
                                rdzv_port = 56, 
                                standalone = True, ), 
                            nproc_per_node = '0', 
                            pytorch_replica_specs = {
                                'key' : kubeflow_org_v1_replica_spec.KubeflowOrgV1ReplicaSpec(
                                    replicas = 56, 
                                    restart_policy = '0', 
                                    template = None, )
                                }, 
                            run_policy = kubeflow_org_v1_run_policy.KubeflowOrgV1RunPolicy(
                                active_deadline_seconds = 56, 
                                backoff_limit = 56, 
                                clean_pod_policy = '0', 
                                scheduling_policy = kubeflow_org_v1_scheduling_policy.KubeflowOrgV1SchedulingPolicy(
                                    min_available = 56, 
                                    min_resources = {
                                        'key' : None
                                        }, 
                                    priority_class = '0', 
                                    queue = '0', 
                                    schedule_timeout_seconds = 56, ), 
                                suspend = True, 
                                ttl_seconds_after_finished = 56, ), ), 
                        status = kubeflow_org_v1_job_status.KubeflowOrgV1JobStatus(
                            completion_time = None, 
                            conditions = [
                                kubeflow_org_v1_job_condition.KubeflowOrgV1JobCondition(
                                    last_transition_time = None, 
                                    last_update_time = None, 
                                    message = '0', 
                                    reason = '0', 
                                    status = '0', 
                                    type = '0', )
                                ], 
                            last_reconcile_time = None, 
                            replica_statuses = {
                                'key' : kubeflow_org_v1_replica_status.KubeflowOrgV1ReplicaStatus(
                                    active = 56, 
                                    failed = 56, 
                                    label_selector = None, 
                                    selector = '0', 
                                    succeeded = 56, )
                                }, 
                            start_time = None, ), )
                    ],
        )

    def testKubeflowOrgV1PyTorchJobList(self):
        """Test KubeflowOrgV1PyTorchJobList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
