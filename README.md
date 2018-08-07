# DIRestPlus [![Build Status](https://travis-ci.org/DataIntegrationAlliance/DIRestPlus.svg?branch=master)](https://travis-ci.org/DataIntegrationAlliance/DIRestPlus)
Data Integration RESTPlus，通过Flask-RESTPlus 构建接口框架，将Wind、iFinD、Choice等进行统一封装

### 外部环境依赖及安装配置

#### ifind 环境配置
```commandline
python "d:\IDE\iFinD\bin\x64\installiFinDPy.py" "D:\IDE\iFinD\bin"
```

#### 测试接口文件安装是否成功
```python
from iFinDPy import *
# 返回 D:\WSPych\RestIFindPy\venv\lib\site-packages\iFinDPy.pth
# 说明安装成功

# 登陆
thsLogin = THS_iFinDLogin("***","***")  # 0

thsDataDataPool  = THS_DataPool('block','2016-11-27;001005260','date:Y,security_name:Y,thscode:Y')
```
-----

#### wind 环境配置
```commandline
python "d:\IDE\Wind\Wind.NET.Client\WindNET\bin\installWindPy.py" "d:\IDE\Wind\Wind.NET.Client\WindNET"
```

#### 测试接口文件安装是否成功
```python
from WindPy import w
w.start()
```
输出内容：
> Welcome to use Wind Quant API for Python (WindPy)!
COPYRIGHT (C) 2017 WIND INFORMATION CO., LTD. ALL RIGHTS RESERVED.
IN NO CIRCUMSTANCE SHALL WIND BE RESPONSIBLE FOR ANY DAMAGES OR LOSSES CAUSED BY USING WIND QUANT API FOR Python.
.ErrorCode=0
.Data=[OK!]