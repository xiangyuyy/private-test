#!/usr/bin/env python
# -*- coding: utf-8 -*-

from httpclient import HTTPClient
from decorator import APIParamsCall
import time
import re


class ELBInternalClient(HTTPClient):
    nginxvms_path = "nginxvms"
    nginxvm_path = "nginxvms/{nginxvm_id}"
    nginxvm_with_filter_path = "nginxvms{filter_param}"
    nginxvm_delete_path = "nginxvms/{nginxvm_id}"
    nginxvm_release_path = "nginxvms/release"
    nginxvm_vmrelease_path = "nginxvms/vmrelease"
    nginxvm_affinity_path = "nginxvms/affinity/{loadbalancer_id}"
    quota_sync_path = "quotas/synchronize"
    quota_audit_path = "quotas/audit"
    certificate_postsync_path = "certificates/sync"
    internal_loadbalancers_path = "loadbalancers"
    loadbalancer_path = "loadbalancers/{loadbalancer_id}"
    loadbalancer_postsync_path = "loadbalancers/{loadbalancer_id}/sync"
    loadbalancer_update_eip_path = "loadbalancers/{loadbalancer_id}/update_eip"
    loadbalancer_assign_capacitys_path = "loadbalancers/{loadbalancer_id}/assign-capacity"
    loadbalancer_check_publicip_path = "loadbalancer/publicipcheck/{loadbalancer_id}"
    loadbalancer_instance_check_path = "{loadbalancer_id}/publicips/instance-check"
    loadbalancer_instance_sync_path = "{loadbalancer_id}/publicips/instance-sync"
    loadbalancer_statictis_path = "lbaas/count"
    listener_path = "listeners/{listener_id}"
    listeners_path = "listeners"
    nginxvm_versions_path = "nginxvms/versions"
    nginxvm_version_path = "nginxvms/versions/{version_id}"
    nginxvm_version_with_filter_path = "nginxvms/versions{filter_param}"
    nginxvm_version_delete_path = "nginxvms/versions/{version_id}"
    nginxvm_tenant_versions_path = "nginxvms/tenant-versions"
    nginxvm_tenant_version_path = "nginxvms/tenant-versions/{nginxvm_tenant_version_id}"
    nginxvm_tenant_version_global_path = "nginxvms/tenant-versions/{cluster_id}/global"
    nginxvm_tenant_version_with_filter_path = "nginxvms/tenant-versions{filter_param}"
    upgrade_nginxvms_task_path = "loadbalancers/{loadbalancer_id}/upgrade-nginxvms"
    upgrade_nginxvms_tasks_path = "loadbalancers/{loadbalancer_id}/upgrade-nginxvms"
    upgrade_nginxvms_task_status_path = "loadbalancers/{loadbalancer_id}/upgrade-nginxvms"
    os_server_groups_path = "os-server-groups"
    os_server_group_path = "os-server-groups/{os_server_group_id}"
    os_server_group_with_filter_path = "os-server-groups{filter_param}"
    os_server_group_delete_path = "os-server-groups/{os_server_group_id}"
    loadbalancer_upgrade_infos_path = "loadbalancers/{loadbalancer_id}/upgrade-nginxvms"
    loadbalancer_upgrade_info_path = "loadbalancers/{loadbalancer_id}/upgrade-nginxvms"
    loadbalancer_upgrade_info_with_filter_path = "loadbalancers/upgrade-nginxvms{filter_param}"
    loadbalancer_upgrade_info_delete_path = "loadbalancers/{loadbalancer_id}/upgrade-nginxvms"

    elbagents_path = "agents"
    elbagent_path = "agents/{agent_id}"
    clusters_path = "clusters"
    cluster_path = "clusters/{cluster_id}"
    l7policies_path = "l7policies"
    l7policy_path = "l7policies/{l7policy_id}"
    member_path = "pools/members/{member_id}"
    service_statuss_path = "elb/billing/status"
    billing_authentications_path = "cloud/elb/billing/authentication"
    billing_resource_instances_path = "cloud/elb/billing/resource-instances"
    billing_instances_path = "elb/billing/instances"
    metadata_path = "cloud/elb/billing/metadata"
    flavors_path = "flavors"
    flavor_path = "flavors/{flavor_id}"
    prewarmsegrules_path = "prewarmsegrules"
    prewarmsegrule_path = "prewarmsegrules/{prewarmsegrule_id}"
    # Vrouter访问db切换API
    HTTP_METHOD_GET = 'GET'
    HTTP_METHOD_PUT = 'PUT'
    ext_lblisteners_path = "extlblisteners"
    ext_lblistener_path = "extlblisteners/{extlblistener_id}/host/{host_id}"
    ext_lbmembers_path = "extlbmembers"
    ext_lbmember_path = "extlbmembers/{extlbmember_id}"
    ext_lbmember_batch_path = "extlbmembers"
    ext_nats_path = "extnats"
    ext_nat_path = "extnats/{public_ip_address}"
    # 全量同步接口
    ext_full_sync_status_path = "reset-full-sync-status"
    bypasss_path = "loadbalancers/{loadbalancer_id}/bypass-enable"
    bypass_migrates_path = "loadbalancers/{loadbalancer_id}/bypass-migrate/{dst_cluster_id}"

    # 全量同步优化接口
    reset_extlblisteners = "reset-extlblisteners/{seq_name}"
    reset_extlbmembers = "reset-extlbmembers/{seq_name}"
    reset_extnats = "reset-extnats/{seq_name}"

    # 查询vrouter接口
    vrouter_opertions = "vrouter-operations"

    locks_path = "elb/billing/lock"
    unlocks_path = "elb/billing/unlock"
    billing_statuss_path = "elb/billing/status"

    EXTED_PLURALS = {
    }

    def __init__(self,
                 api_info,
                 user_id,
                 service_url=None,
                 service_type=None,
                 timeout=30,
                 **kwargs):
        HTTPClient.__init__(self,
                            api_info=api_info,
                            user_id=user_id,
                            service_url=service_url,
                            service_type=service_type,
                            timeout=timeout,
                            **kwargs
                            )

    def get_action_prefix(self, api_version=None, key=None):
        if self.api_type == "openstack":
            return "/v2.0/"

        if re.search(r"\/v(\d+(\.\d+)?)\/?", self.service_url):
            return "/"
        else:
            return "/v2.0/"

    @APIParamsCall
    def show_loadbalancer(self, **kwargs):
        pass

    @APIParamsCall
    def postsync_loadbalancer(self, **kwargs):
        pass

    @APIParamsCall
    def update_loadbalancer_update_eip(self, loadbalancer_id, **kwargs):
        pass

    @APIParamsCall
    def create_loadbalancer_assign_capacity(self, loadbalancer_id, **kwargs):
        pass

    @APIParamsCall
    def show_loadbalancer_check_publicip(self, loadbalancer_id):
        pass

    @APIParamsCall
    def show_loadbalancer_instance_check(self, loadbalancer_id, **kwargs):
        pass

    @APIParamsCall
    def update_loadbalancer_instance_sync(self, loadbalancer_id, **kwargs):
        pass

    @APIParamsCall
    def list_internal_loadbalancers(self, **kwargs):
        pass

    @APIParamsCall
    def list_loadbalancer_statictis(self, **kwargs):
        pass

    @APIParamsCall
    def update_loadbalancer(self, loadbalancer_id, **kwargs):
        pass

    @APIParamsCall
    def show_listener(self, listener_id, **kwargs):
        pass

    @APIParamsCall
    def list_listeners(self, **kwargs):
        pass

    @APIParamsCall
    def show_nginxvm_affinity(self, loadbalancer_id, **kwargs):
        pass

    @APIParamsCall
    def create_nginxvm(self, **kwargs):
        pass

    @APIParamsCall
    def show_nginxvms(self, **kwargs):
        pass

    @APIParamsCall
    def update_nginxvm(self, nginxvm_id, **kwargs):
        pass

    @APIParamsCall
    def list_nginxvm_with_filter(self, filter_param, **kwargs):
        pass

    @APIParamsCall
    def show_nginxvm(self, nginxvm_id):
        pass

    @APIParamsCall
    def delete_nginxvm_delete(self, nginxvm_id, **kwargs):
        pass

    @APIParamsCall
    def postsync_certificate(self, **kwargs):
        pass

    @APIParamsCall
    def sync_quota(self, **kwargs):
        pass

    @APIParamsCall
    def audit_quota(self, **kwargs):
        pass

    @APIParamsCall
    def create_nginxvm_version(self, **kwargs):
        pass

    @APIParamsCall
    def list_nginxvm_version_with_filter(self, filter_param, **kwargs):
        pass

    @APIParamsCall
    def show_nginxvm_version(self, version_id):
        pass

    @APIParamsCall
    def delete_nginxvm_version_delete(self, version_id, **kwargs):
        pass

    @APIParamsCall
    def create_os_server_group(self, **kwargs):
        pass

    @APIParamsCall
    def update_os_server_group(self, os_server_group_id, **kwargs):
        pass

    @APIParamsCall
    def list_os_server_group_with_filter(self, filter_param, **kwargs):
        pass

    @APIParamsCall
    def show_os_server_group(self, os_server_group_id):
        pass

    @APIParamsCall
    def delete_os_server_group_delete(self, os_server_group_id, **kwargs):
        pass

    @APIParamsCall
    def create_loadbalancer_upgrade_info(self, loadbalancer_id, **kwargs):
        pass

    @APIParamsCall
    def update_loadbalancer_upgrade_info(self, loadbalancer_id, **kwargs):
        pass

    @APIParamsCall
    def list_loadbalancer_upgrade_info_with_filter(self, filter_param, **kwargs):
        pass

    @APIParamsCall
    def show_loadbalancer_upgrade_info(self, loadbalancer_id):
        pass

    @APIParamsCall
    def delete_loadbalancer_upgrade_info_delete(self, loadbalancer_id, **kwargs):
        pass

    @APIParamsCall
    def create_nginxvm_tenant_version(self, **kwargs):
        pass

    @APIParamsCall
    def update_nginxvm_tenant_version(self, nginxvm_tenant_version_id, **kwargs):
        pass

    @APIParamsCall
    def delete_nginxvm_tenant_version(self, nginxvm_tenant_version_id, **kwargs):
        pass

    @APIParamsCall
    def show_nginxvm_tenant_version(self, nginxvm_tenant_version_id):
        pass

    @APIParamsCall
    def show_nginxvm_tenant_version_global(self, cluster_id):
        pass

    @APIParamsCall
    def list_nginxvm_tenant_version_with_filter(self, filter_param, **kwargs):
        pass

    @APIParamsCall
    def create_upgrade_nginxvms_task(self, loadbalancer_id, **kwargs):
        pass

    @APIParamsCall
    def update_upgrade_nginxvms_task_status(self, loadbalancer_id, **kwargs):
        pass

    @APIParamsCall
    def list_upgrade_nginxvms_task(self, loadbalancer_id, **kwargs):
        pass

    @APIParamsCall
    def create_elbagent(self, **kwargs):
        pass

    @APIParamsCall
    def update_elbagent(self, agent_id, **kwargs):
        pass

    @APIParamsCall
    def show_elbagent(self, agent_id):
        pass

    @APIParamsCall
    def delete_elbagent(self, agent_id):
        pass

    @APIParamsCall
    def list_elbagents(self, **kwargs):
        pass

    @APIParamsCall
    def create_cluster(self, **kwargs):
        pass

    @APIParamsCall
    def update_cluster(self, agent_id, **kwargs):
        pass

    @APIParamsCall
    def delete_cluster(self, cluster_id):
        pass

    @APIParamsCall
    def show_cluster(self, cluster_id):
        pass

    @APIParamsCall
    def list_clusters(self, filter_param, **kwargs):
        pass

    @APIParamsCall
    def show_l7policy(self, l7policy_id):
        pass

    @APIParamsCall
    def list_l7policies(self, filter_param, **kwargs):
        pass

    @APIParamsCall
    def show_member(self, member_id):
        pass

    @APIParamsCall
    def create_service_status(self, **kwargs):
        pass

    @APIParamsCall
    def create_billing_authentication(self, **kwargs):
        pass

    @APIParamsCall
    def update_metadata(self, **kwargs):
        pass

    @APIParamsCall
    def create_flavor(self, **kwargs):
        pass

    @APIParamsCall
    def delete_flavor(self, **kwargs):
        pass

    @APIParamsCall
    def create_prewarmsegrule(self, **kwargs):
        pass

    @APIParamsCall
    def update_prewarmsegrule(self, segrule_id, **kwargs):
        pass

    @APIParamsCall
    def delete_prewarmsegrule(self, segrule_id):
        pass

    @APIParamsCall
    def show_prewarmsegrule(self, segrule_id):
        pass

    @APIParamsCall
    def list_prewarmsegrules(self, **kwargs):
        pass

    @APIParamsCall
    def list_members(self, **kwargs):
        pass

    @APIParamsCall
    def show_ext_lblisteners(self, id, host_id, seq, fields, limit=10):
        pass

    @APIParamsCall
    def list_billing_instances(self, **kwargs):
        pass

    @APIParamsCall
    def create_billing_resource_instance(self, **kwargs):
        pass

    def update_ext_lblistener(self, extlblistener_id, host_id, body):
        path = self.ext_lblistener_path
        body = {"extlblistener": body}
        url = path.format(extlblistener_id=extlblistener_id, host_id=host_id)
        return self.put(url, body=body)

    def show_ext_lblisteners_with_filters(self, **kwargs):
        path = self.ext_lblisteners_path
        args = ['fields=id', 'fields=vip',
                'fields=vip_port_id', 'fields=vip_vni',
                'fields=vip_subnet_id', 'fields=listener_mark',
                'fields=front_port', 'fields=front_protocol',
                'fields=region_vip', 'fields=host_id',
                'fields=admin_state_up', 'fields=status',
                'fields=connection_limit',
                'fields=default_tls_container_id',
                'fields=sni_containers', 'fields=router_gw_ip',
                'fields=vport_mac_address', 'fields=dataplane_mark',
                'fields=lb_id', 'fields=pool_id',
                'fields=lb_algorithm', 'fields=pool_admin_state_up',
                'fields=session_persistence', 'fields=back_protocol',
                'fields=heal_monitor_id', 'fields=type',
                'fields=delay', 'fields=timeout',
                'fields=max_retries', 'fields=http_method',
                'fields=url_path', 'fields=expected_codes',
                'fields=provisioning_status', 'fields=hm_admin_state_up',
                'fields=option', 'fields=tenant_id',
                'fields=seq0']

        for (k, v) in kwargs.items():
            args.append("%s=%s" % (k, v))

        filters = '&'.join(args)
        url = path + "?%s" % filters
        return self.get(url)

    @APIParamsCall
    def show_ext_lbmembers(self, limit=10, **kwargs):
        pass

    def update_ext_lbmember(self, extlbmember_id, body):
        path = self.ext_lbmember_path
        body = {"extlbmember": body}
        url = path.format(extlbmember_id=extlbmember_id)
        return self.put(url, body=body)

    def update_ext_lbmembers(self, body):
        path = self.ext_lbmembers_path
        body = {"extlbmembers": body}
        return self.put(path, body=body)

    def show_ext_lbmembers_with_filters(self, **kwargs):
        path = self.ext_lbmembers_path
        # fields and args
        args = ['fields=public_ip_address', 'fields=private_ip_address',
                'fields=fixed_port_id', 'fields=host_id',
                'fields=status', 'fields=vni',
                'fields=vtep_ip', 'fields=mac_address',
                'fields=subnet_id', 'fields=router_port_mac',
                'fields=id', 'fields=back_port',
                'fields=back_protocol', 'fields=weight',
                'fields=lb_id', 'fields=listener_id',
                'fields=pool_id', 'fields=admin_state_up',
                'fields=provisioning_status', 'fields=option',
                'fields=tenant_id', 'fields=seq0']

        for (k, v) in kwargs.items():
            args.append("%s=%s" % (k, v))

        filters = '&'.join(args)
        url = path + "?%s" % filters
        return self.get(url)

    @APIParamsCall
    def show_ext_nats(self, id, host_id, seq, fields, limit=10):
        pass

    def update_ext_nat(self, public_ip_address, body):
        path = self.ext_nat_path
        body = {"extnat": body}
        url = path.format(public_ip_address=public_ip_address)
        return self.put(url, body=body)

    def show_ext_nats_with_fliters(self, **kwargs):
        path = self.ext_nats_path
        args = ['fields=public_ip_address', 'fields=private_ip_address',
                'fields=router_id', 'fields=fixed_port_id',
                'fields=agent_host_id', 'fields=status',
                'fields=vni', 'fields=vtep_ip',
                'fields=mac_address', 'fields=subnet_id',
                'fields=router_port_mac', 'fields=router_gw_ip',
                'fields=option', 'fields=seq0', ]
        # add requestParams
        for (k, v) in kwargs.items():
            args.append("%s=%s" % (k, v))
        filters = '&'.join(args)
        url = path + "?%s" % filters
        return self.get(url)

    def get_reset_ext_nats(self, seq_name):
        path = self.reset_extnats
        url = path.format(seq_name=seq_name)
        return self.get(url)

    def get_reset_ext_lblisteners(self, seq_name):
        path = self.reset_extlblisteners
        url = path.format(seq_name=seq_name)
        return self.get(url)

    def get_reset_ext_lbmembers(self, seq_name):
        path = self.reset_extlbmembers
        url = path.format(seq_name=seq_name)
        return self.get(url)

    def reset_extnats_with_seq(self, seq_name, body):
        path = self.reset_extnats
        url = path.format(seq_name=seq_name)
        body = {"reset_data": body}
        return self.put(url, body)

    def reset_extlisteners_with_seq(self, seq_name, body):
        path = self.reset_extlblisteners
        url = path.format(seq_name=seq_name)
        body = {"reset_data": body}
        return self.put(url, body)

    def reset_extmembers_with_seq(self, seq_name, body):
        path = self.reset_extlbmembers
        url = path.format(seq_name=seq_name)
        body = {"reset_data": body}
        return self.put(url, body)

    def fetch_operation(self):
        path = self.vrouter_opertions
        url = path.format()
        return self.get(url)

    def fetch_operation_with_marker(self, marker):
        path = self.vrouter_opertions + "?" + "marker=%s" % marker
        url = path.format()
        return self.get(url)

    def reset_nginxvm_release(self, body):
        path = self.nginxvm_release_path
        return self.post(path, body=body)

    def reset_nginxvm_vmrelease(self, body):
        path = self.nginxvm_vmrelease_path
        return self.post(path, body=body)

    @APIParamsCall
    def create_lock(self, **kwargs):
        pass

    @APIParamsCall
    def create_unlock(self, **kwargs):
        pass

    @APIParamsCall
    def create_billing_status(self, **kwargs):
        pass

    @APIParamsCall
    def create_bypass(self, lb_id, **kwargs):
        pass

    @APIParamsCall
    def create_bypass_migrate(self, dst_cluster_id):
        pass

    def list_pool_members(self, pool_id, **kwargs):
        args = []
        for (k, v) in kwargs.items():
            args.append("%s=%s" % (k, v))
        filters = '&'.join(args)
        path = "pools/" + pool_id + "/members" + "?%s" % filters
        url = path.format()
        return self.get(url)

    def show_pool_members(self, pool_id, member_id):
        path = "pools/" + pool_id + "/members/" + member_id
        url = path.format()
        return self.get(url)

    def update_pool_members(self, body):
        url = "members/refresh"
        body = {"members": body}
        return self.put(url, body)

    def list_om_all_members(self, **kwargs):
        path = "members"
        args = []
        for (k, v) in kwargs.items():
            args.append("%s=%s" % (k, v))
        filters = '&'.join(args)
        path = path + "?%s" % filters
        url = path.format()
        url = path.format()
        return self.get(url)

    def list_om_pool_exmembers(self, pool_id, **kwargs):
        path = "pools/" + pool_id + "/exmembers"
        args = []
        for (k, v) in kwargs.items():
            args.append("%s=%s" % (k, v))
        filters = '&'.join(args)
        path = path + "?%s" % filters
        url = path.format()
        return self.get(url)

    def list_om_pool_members(self, pool_id, **kwargs):
        path = "pools/" + pool_id + "/members"
        args = []
        for (k, v) in kwargs.items():
            args.append("%s=%s" % (k, v))
        filters = '&'.join(args)
        path = path + "?%s" % filters
        url = path.format()
        return self.get(url)

    def show_om_pool_members(self, pool_id, member_id):
        path = "ops/em/pools/" + pool_id + "/members/" + member_id
        url = path.format()
        return self.get(url)

    def list_all_members(self, **kwargs):
        path = "members"
        args = []
        for (k, v) in kwargs.items():
            args.append("%s=%s" % (k, v))
        filters = '&'.join(args)
        path = path + "?%s" % filters
        url = path.format()
        return self.get(url)

    def list_vm_member(self, **kwargs):
        path = "vm"
        args = []
        for (k, v) in kwargs.items():
            args.append("%s=%s" % (k, v))
        filters = '&'.join(args)
        path = path + "?%s" % filters
        url = path.format()
        return self.get(url)


if __name__ == "__main__":
    pass
