#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
import datetime
import requests

API_BASE = 'https://open.koudaitong.com/api/entry'


class YouZan(object):
    """docstring for YouZan"""
    def __init__(self, app_id, app_secert):
        self.app_id = app_id
        self.app_secert = app_secert
        self.format = 'json'
        self.v = '1.0'
        self.sign_method = 'md5'
        self.arg_dict = {
            'app_id': self.app_id,
            'format': self.format,
            'sign_method': self.sign_method,
            'v': self.v
        }

    def get_sign(self):
        arg_dict = sorted(self.arg_dict.iteritems(), key=lambda d: d[0])
        arg_str = ''.join(
            [''.join([str(i) for i in item]) for item in arg_dict])
        arg_str = "{}{}{}".format(self.app_secert, arg_str, self.app_secert)
        return hashlib.md5(arg_str).hexdigest()

    def __call__(self, method, **args):
        self.method = method
        self.args = args
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.arg_dict['method'] = method
        self.arg_dict['timestamp'] = self.timestamp
        self.arg_dict = dict(self.arg_dict, **self.args)

        payload = self.arg_dict
        payload['sign'] = self.get_sign()
        r = requests.get(API_BASE, params=payload)
        return r.json()

