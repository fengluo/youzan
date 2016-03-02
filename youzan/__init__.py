#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import datetime
import requests

API_BASE = 'https://open.koudaitong.com/api/entry'


class YouZan(object):
    """docstring for YouZan"""
    def __init__(self, app_id=None, app_secert=None):
        self.app_id = app_id
        self.app_secert = app_secert
        self.format = 'json'
        self.v = '1.0'
        self.sign_method = 'md5'


    def get_sign(self, args_dict):
        arg_str = ''.join(
            ['%s%s' % (key, args_dict[key])
                for key in sorted(args_dict)])
        arg_str = "{}{}{}".format(self.app_secert, arg_str, self.app_secert)
        return hashlib.md5(arg_str).hexdigest().lower()

    def __call__(self, method, **args):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        args_dict = {}
        args_dict['app_id'] = self.app_id
        args_dict['format'] = self.format
        args_dict['sign_method'] = self.sign_method
        args_dict['v'] = self.v
        args_dict['method'] = method
        args_dict['timestamp'] = timestamp
        args_dict.update(args)

        payload = args_dict.copy()
        payload['sign'] = self.get_sign(args_dict)

        r = requests.get(API_BASE, params=payload)
        return r.json()
