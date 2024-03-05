from constructs import Construct

from hmd_lib_cdktf_factories.service_base import ServiceCdkTfStack


class CdkTfStack(ServiceCdkTfStack):
    def __init__(
        self,
        scope: Construct,
        ns: str,
        instance_name: str,
        repo_name: str,
        deployment_id: str,
        environment: str,
        region: str,
        customer_code,
        repo_version: str,
        account_number: str,
        profile: str,
        config: dict,
    ):
        super().__init__(
            scope,
            ns,
            instance_name,
            repo_name,
            deployment_id,
            environment,
            region,
            customer_code,
            repo_version,
            account_number,
            profile,
            config,
        )
