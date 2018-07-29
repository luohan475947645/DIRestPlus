#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author  : MG
@Time    : 2018/7/29 13:06
@File    : __init__.py.py
@contact : mmmaaaggg@163.com
@desc    : 
"""
from flask import Flask
from flask_restplus import Api
import logging
from datetime import datetime
from direstplus.config import config

logger = logging.getLogger(__name__)
STR_FORMAT_DATE = '%Y-%m-%d'
STR_FORMAT_DATETIME_WIND = '%Y-%m-%d %H:%M:%S'  # 2017-03-06 00:00:00
UN_AVAILABLE_DATETIME = datetime.strptime('1900-01-01', STR_FORMAT_DATE)
UN_AVAILABLE_DATE = UN_AVAILABLE_DATETIME.date()
app = Flask(__name__)
api = Api(app,
          title='Data Integration RestPlus API',
          version='0.0.1',
          description='Wind、iFinD、Choice 接口封装API',
          )

# 加载 iFinD 接口
has_api = True
try:
    import iFinDPy
except ImportError:
    has_api = False

if has_api:
    from direstplus.ifind import *
    logger.info('加载 iFinD 接口')


# 加载 Wind 接口


def start_service():
    ths_login = ifind.THS_iFinDLogin(config.THS_LOGIN_USER_NAME, config.THS_LOGIN_PASSWORD)
    if ths_login == 0 or ths_login == -201:
        logger.info('成功登陆')
        try:
            from direstplus import app
            app.run(host="0.0.0.0", debug=True)
        finally:
            ifind.THS_iFinDLogout()
            logger.info('成功登出')
    else:
        logger.error("登录失败")


if __name__ == '__main__':
    start_service()