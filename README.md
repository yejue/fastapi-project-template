## 一、项目结构解读

```
├─alembic  # 数据库迁移文件相关
├─apps  # 子应用划分
│  │  __init__.py
│  └─hello
│          constants.py     # 单个应用中的常量
│          dependencies.py  # 依赖注入
│          exceptions.py    # 本应用内的异常捕获
│          models.py   		# 与数据表相对的模型类
│          router.py   		# 本应用的路由，是每个 app 的入口
│          schemas.py  		# 数据校验或序列化器
│          service.py  		# 封装的业务逻辑等
│          utils.py    		# 归属于本应用的一些工具，非业务逻辑
│          __init__.py		# 认为每个 app 同时作为一个模块，可能其中的某些 module 会被别的 app 复用
│
├─logs
├─scripts
├─tests  # 项目测试相关，脚本或者一些预定义 http 测试请求
│  └─hello
│
├─utils  # 一些全局工具函数，如果需要的话
│      __init__.py
│
│ config.py  		# 全局配置文件
│ database.py		# 数据库链接文件
│ exceptions.py		# 全局错误捕获
│ main.py			# 项目主入口
│ models.py			# 通用数据模型
│ pagination.py		# 全局分页模块
│ README.md
│ requirements.txt
```


## 二、TODOs
- [ ] db 提交整合
- [ ] 请求响应格式整合
- [ ] 简单 ORBC
- [ ] 精简 Schema
