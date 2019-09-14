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


def cmp_dict(src_data, dst_data, path='', diff=dict()):
    assert type(src_data) == type(dst_data), "type: '{}' != '{}'".format(type(src_data), type(dst_data))
    if isinstance(src_data, dict):
        for key in src_data:
            newpath = path + '.' + key
            if key in dst_data:
                diff = cmp_dict(src_data[key], dst_data[key], newpath, diff)
            else:
                diff[newpath] = [src_data.get(key), 'not exist is key']
    elif isinstance(src_data, list):
        for k, v in enumerate(zip(src_data, dst_data)):
            cmp_dict(v[0], v[1], path + '.' + str(k))
    else:
        if src_data != dst_data:
            diff[path] = [src_data, dst_data]

    return diff


if __name__ == "__main__":
    xx = {"a":"b", "version":"1.0","status":10,"errorMsg":"全部成功","elapsed":3,"data":{"groups":[{"name":"全部","id":-1,"dispOrd":11},{"name":"面部护肤","id":1142,"dispOrd":1}],"firstCategoryList":[{"name":"美妆个护","id":1041,"dispOrd":12},{"name":"食品生鲜","id":1004,"dispOrd":13}]}}
    yy = {"version":"1.0","status":0,"errorMsg":"全部成功","elapsed":3,"data":{"groups":[{"name":"全部","id":-1,"dispOrd":1},{"name":"面部护肤","id":1042,"dispOrd":1}],"firstCategoryList":[{"name":"美妆个护","id":1041,"dispOrd":12},{"name":"食品生鲜","id":1004,"dispOrd":13}]}}
    diff = cmp_dict(xx, yy)
    for k, v in diff.items():
        print('key is {} -> value is {}'.format(k, v))
