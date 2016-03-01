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
        self._arg_dict = {}

    def get_arg_dict(self):
        self._arg_dict['app_id'] = self.app_id
        self._arg_dict['format'] = self.format
        self._arg_dict['sign_method'] = self.sign_method
        self._arg_dict['v'] = self.v
        return self._arg_dict

    def set_arg_dict(self, key, value):
        self._arg_dict[key] = value

    def merge_arg_dict(self, args):
        self._arg_dict = dict(self._arg_dict, **args)

    def get_sign(self):
        arg_str = ''.join(
            ['%s%s' % (key, self.get_arg_dict()[key])
                for key in sorted(self.get_arg_dict())])
        arg_str = "{}{}{}".format(self.app_secert, arg_str, self.app_secert)
        return hashlib.md5(arg_str).hexdigest().lower()

    def __call__(self, method, **args):
        self._arg_dict = {}
        self.method = method
        self.args = args
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.set_arg_dict('method', method)
        self.set_arg_dict('timestamp', self.timestamp)
        self.merge_arg_dict(args)

        payload = self.get_arg_dict()
        payload['sign'] = self.get_sign()
        r = requests.get(API_BASE, params=payload)
        return r.json()
