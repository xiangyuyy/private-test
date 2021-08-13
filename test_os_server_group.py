# !/usr/bin/env python
# -*- coding: utf-8 -*-
from testcases.test_elb_controller.test_elbv3.common.constants import *
import time

class Test_osServerGroup(object):
    @classmethod
    def setup_class(cls):
        cls.elb_internal = ELBInternalClient(
            api_info=GATEWAY_API_INFO, user_id='admin',
            service_url='elb_internal', service_type='elb_internal',
            **{"is_catch_error_status": False})
        cls.elb_om = ELBInternalClient(
            api_info=GATEWAY_API_INFO, user_id='admin',
            service_url='elb_om', service_type='elb_om',
            **{"is_catch_error_status": False})
        cls.test = Controller_Basic()
        cls.create_resources()

    @classmethod
    def create_resources(cls):
        now_time = str(time.time())
        nginxvm_version = {
            "name": "CI_OSSERVERGROUP" + now_time,
            "image_name": "eular_osServerGroup" + now_time,
            "nginx_package_name": "nginx_osServerGroup" + now_time
        }
        resp, cls.nginxvm_version = cls.elb_om.create_nginxvm_version(**nginxvm_version)
        assert cls.nginxvm_version['nginxvm_version']
        cls.nginxvm_version_id = cls.nginxvm_version['nginxvm_version']['id']

        cls.nginxvm_count = 100
        os_server_group = {
            "id": cls.nginxvm_version_id,
            "ecs_flavor": "elb1.medium",
            "availability_zone": "AZ1",
            "nginxvm_version_id": cls.nginxvm_version_id,
            "nginxvm_count": cls.nginxvm_count
        }
        resp, cls.os_server_group = cls.elb_internal.create_os_server_group(**os_server_group)
        assert cls.os_server_group['os_server_group']
        cls.os_server_group_id = cls.os_server_group['os_server_group']['id']

    @classmethod
    def teardown_class(cls):
        if cls.os_server_group_id:
            resp, body = cls.elb_internal \
                .delete_os_server_group_delete(cls.os_server_group_id)
            assert resp.status_code == 204

            if cls.nginxvm_version_id:
                resp, body = cls.elb_om \
                    .delete_nginxvm_version_delete(cls.nginxvm_version_id)
                assert resp.status_code == 204

    def test_update_nginxvmosg(self):
        update = {
            "nginxvm_count": 200,
        }
        resp, body = self.elb_internal \
            .update_os_server_group(self.os_server_group_id, **update)
        assert resp.status_code == 200

    def test_01_list_nginxvmosgs(self):
        resp, body = self.elb_internal.list_os_server_group_with_filter("?id=" + self.os_server_group_id)
        assert resp.status_code == 200

    def test_01_show_nginxvmosg(self):
        resp, body = self.elb_internal \
            .show_os_server_group(self.os_server_group_id)
        assert resp.status_code == 200
