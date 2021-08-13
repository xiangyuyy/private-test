#!/usr/bin/env python
# -*- coding: utf-8 -*-

from log import logger
import re


def APIParamsCall(func):
    func_name = func.__name__
    operate = func_name.split("_", 1)[0]
    key = func_name.split("_", 1)[1]

    def wrapper(self, *args, **kwargs):
        headers = kwargs.pop("headers", None)
        api_version = kwargs.pop("api_version", None)

        def get_path(key, operate, api_version=None):
            if operate in ["show", "update", "delete", "create", "sync", "postsync", "audit", "force", "preoccupy"]:
                action_prefix = self.get_action_prefix(key=key, api_version=api_version)
            elif operate in ["list"]:
                for k, v in self.EXTED_PLURALS.iteritems():
                    if v == key:
                        action_prefix = self.get_action_prefix(key=key, api_version=api_version)
                        break
                else:
                    action_prefix = self.get_action_prefix(key=key[:-1], api_version=api_version)

            if operate in ["show", "update", "delete"]:
                path = action_prefix + getattr(self, key + "_path")
            elif operate in ["create"]:
                path = action_prefix + getattr(self, self.EXTED_PLURALS.get(key, key + "s") + "_path")
            elif operate in ["list"]:
                path = action_prefix + getattr(self, key + "_path")
            elif operate in ["sync", "postsync", "audit"]:
                path = action_prefix + getattr(self, "%s_%s_path" % (key, operate))
            elif operate in ["force"]:
                path = action_prefix + getattr(self, "%s_%s_path" % (key, operate))
            elif operate in ["preoccupy"]:
                path = action_prefix + getattr(self, "%s_path" % operate)

            return path

        path = get_path(api_version=api_version, key=key, operate=operate)

        if self.service_url.find("v3") >= 0 or self.service_url.find("v2/") >= 0:
            if 'loadbalancer_statictis' != key:
                path = path.replace("/lbaas/", "/")
            
        #如果入参在args中, 则先构造一个dict作为path的参数进行format
        if args:
            args_in_path = re.findall('\{(.*?)\}', path)
            path_args = dict(zip(args_in_path, args))
            path = path.format(**path_args)

        args_in_path = re.findall('\{(.*?)\}', path)
        path = path.format(**kwargs)
        for _arg in args_in_path:
            kwargs.pop(_arg)

        no_key_resource = ["lock", "unlock", "prepaid_spec_change", "billing_status", "change_charge_mode", "bypass",
                           "billing_loadbalancer", "billing_authentication", "service_status", "ext_loadbalancer",
                           "upgrade_nginxvms_task", "members_patch", "metadata", "billing_resource_instance"]
        if operate == "create":
            dataset = self.build_dataset(kwargs)
            if key in no_key_resource:
                body = dataset
            elif "waf_" in key:
                body = {
                    key.replace('waf_', ''): dataset
                }
            elif "loadbalancer_upgrade_info" in key:
                body = {
                    'loadbalancer_upgrade_info': dataset
                }
            elif "loadbalancer_" in key:
                body = {
                    'loadbalancer': dataset
                }
            elif "members_patch" in key:
                body = dataset
            else:
                body = {
                    key: dataset
                }
            return self.post(path, body=body, headers=headers)
        elif operate == "delete":
            return self.delete(path, params=kwargs)
        elif operate == "show":
            return self.get(path, params=kwargs)
        elif operate == "update":
            dataset = self.build_dataset(kwargs)
            if key in no_key_resource:
                body = dataset
            # body: {"reset_data": {"host_id": 1, "seq_name": "seq1"}}
            elif "whitelist_upgrade" in key:
                body = {
                    "whitelist": dataset
                }
            elif "ext_full_sync_status" in key:
                body = {
                    "reset_data": dataset
                }
            elif "loadbalancer_upgrade_info" in key:
                body = {
                    'loadbalancer_upgrade_info': dataset
                }
            elif "instance_sync" in key:
                body = dataset
            elif "loadbalancer" in key:
                body = {
                    "loadbalancer": dataset
                }
            else:
                body = {
                    key: dataset
                }
            return self.put(path, body=body)
        elif operate == "list":
            return self.get(path, params=kwargs)
        elif operate in ['sync', 'audit']:
            return self.get(path, params=kwargs)
        elif operate in ['postsync']:
            dataset = self.build_dataset(kwargs)
            if key == "certificate":
                body = {
                    key: dataset
                }
            else:
                body = dataset
            return self.post(path, body=body)
        elif operate in ['force']:
            return self.get(path, params=kwargs)
        elif operate in ['preoccupy']:
            return self.get(path, params=kwargs)

    return wrapper


from threading import Thread
import functools

def func_timeout(timeout):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = [Exception('%s timeout: %s sec' % (func.__name__, timeout))]
            def new_func():
                try:
                    res[0] = func(*args, **kwargs)
                except Exception, e:
                    res[0] = e
            t = Thread(target=new_func)
            t.daemon = True
            try:
                t.start()
                t.join(timeout)
            except Exception as e:
                logger.warning(str(e))
                raise e
            ret = res[0]
            if isinstance(ret, BaseException):
                logger.warning(str(ret))
                raise ret
            return ret
        return wrapper
    return deco
