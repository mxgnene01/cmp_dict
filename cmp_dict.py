#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Meng xiangguo <mxgnene01@gmail.com>
#
#        H A P P Y    H A C K I N G !
#              _____               ______
#     ____====  ]OO|_n_n__][.      |    |]
#    [________]_|__|________)<     |MENG|
#     oo    oo  'oo OOOO-| oo\_   ~o~~~o~'
# +--+--+--+--+--+--+--+--+--+--+--+--+--+


def cmp_dict(src_data, dst_data, path='', diff=dict(), sort=False):
    # assert type(src_data) == type(dst_data), "type: '{}' != '{}'".format(type(src_data), type(dst_data))
    # 这个地方为了解决：pytest.mark.parametrize 多case中一个失败，导致后续case也失败的问题
    if path == '':
         diff = dict()

    if isinstance(src_data, dict):
        for key in src_data:
            newpath = path + '.' + key
            if key in dst_data:
                diff = cmp_dict(src_data[key], dst_data[key], newpath, diff)
            else:
                diff[newpath] = [src_data.get(key), 'not exist is key']
    elif isinstance(src_data, list):
        if len(src_data) == len(dst_data):
            if sort:
                tmp = zip(sorted(src_data), sorted(dst_data))
            else:
                tmp = zip(src_data, dst_data)
            for k, v in enumerate(tmp):
                diff = cmp_dict(v[0], v[1], path + '.' + str(k), diff)
        else:
            diff[path] = [src_data, dst_data]
    else:
        if src_data != dst_data:
            diff[path] = [src_data, dst_data]

    return diff


if __name__ == "__main__":
    xx = {'kkk0':'vvv0', 'kkkk1': [{'c': 'd', 'k2': [{'kk2': 'vv2'}, {'kk3': 'vv3'}]}, {'k3': 'v3'}], 'kkkk2': 'vvvv2'}
    yy = {'kkk0':'vvvv0', 'kkkk1': [{'c': 'd', 'k2': [{'kk2': 'diffvv2'}, {'kk3': 'vv3'}]}, {'k3': None}]}
    diff = cmp_dict(xx, yy)
    for k, v in diff.items():
        print('key is {} -> value is {}'.format(k, v))
