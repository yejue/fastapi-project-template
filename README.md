<div align="center"> 
<h1 align="center">
⚡UPing - FastAPI Project Template
</h1>
</div>



## 🐣Introduction

U-Ping 是一个笔记分享和供你评论的 Web 服务，目前它仅仅是用于 FastAPI 的项目结构展示。这个项目结构基本参照了这个项目  [fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices)，之所以做这些改动是源于我在 Django 中的文件目录习惯。

使用的有：Alembic、SQLAlchemy、Celery 等。

这个项目一直会在保持简单清晰的前提下进行更新扩展。


## ✨Features

 - 简单清晰的 FastAPI 项目结构
 - 身份验证和简便的权限认证
 - 对象级别校验（这个方案可扩展性很强）
 - request.user 访问当前用户
 - 优雅的 celery 引入


## 🚀QuickStart

1. Fork or star this project, 要找到这个项目可能不容易
2. `git clone project-url`，克隆这个项目
3. `cd your-project`，进入到项目主目录
4. `pip install -r requirements`，下载好 pip 依赖包
5. 初始化 alembic，在终端输入 `alembic init alembic`，在项目中已经含有 alembic 文件夹，你可以参考其中的 env.py， 随后可以删除这个文件夹
6. python main.py


## 📔TODOs

- [ ] db 提交整合以及异步
- [ ] 统一全局响应
- [ ] 精简 Schema
- [ ] 将 permission 相关类移动到更合理的位置
- [ ] 引入持久部署方案
- [x] 引入数据表迁移方案


## 📂Project Structure

```text
- alembic
- apps
    - note
        - dependencies.py
        - models.py
        - permissions.py
        - router.py
        - schemas.py
        - service.py
- logs
- middleware
- scripts
- tests
- utils
alembic.ini
config.py
database.py
exceptions
main.py
pagination.py
```

**alembic**：这个文件夹和 alembic.ini 都是 alembic 的迁移相关的文件夹，在本项目中，推荐使用 alembic 对数据库进行迁移管理。 
一般不需要对这些文件做任何的改动。https://alembic.sqlalchemy.org/en/latest/tutorial.html 。
本项目中的 alembic 主要用于参照，在实际使用中你可以随时删掉它。

**apps**：顾名思义，里面的下一级文件都是一个 ”app“，这些 ”app“ 是整个项目的不同板块、模块，或者说是类别，总之就是用来区分功能大块用的。
在一个 app 内通常会有 dependencies.py, models.py, router.py, schemas.py, service.py

**note**：这是其中一个的 app，在这个项目中用于笔记相关功能接口。你可以在 router.py 中看到该 app 内的所有接口，在 mvc 中被称为 c。
也有点类似于 Django 的 views，不过这个 views 就还包含了 urls。在 router.py 中调用 service.py 来完成业务逻辑的操作，在 dependencies 中
来存储依赖项。models.py 是当前 app 的所有数据表模型，而 schemas 中是 pydantic 的模型，schemas 内的模型也可以被称为序列化器，类似于
drf 的 serializers。

**logs**：没什么好说的，准备了一个地方存放运行日志，这个文件夹需要在 conf 中进行配置。

**middleware**：全局的中间件。在使用它之前，你应该了解一个请求的生命周期。

**scripts**：一些脚本的存放位置，如：启动脚本、一些触发脚本

**tests**：一些自动化测试的东西，如：接口自动化测试

**alembic.ini**：上面讲了，是 alembic 生成的东西。


**utils**：一些工具函数，这些工具函数往往和业务逻辑有所区分，可以在好多地方通用的地方调用。

**config.py**：全局的配置文件。

**database.py**：关于数据库连接的文件，可以在这里描述数据库的链接、引擎、会话，以及模型等。
它也可以被理解为是工具函数，只是它专门用于数据库。

**exceptions.py**：一些全局的错误类型，比如说自定义的 404 错误、自定义的 500 错误等。

**main.py**：在不使用托管程序的时候，它是程序的入口

**pagination.py**：分页相关的类.

## ⭐Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yejue/fastapi-project-template&type=Date)](https://star-history.com/#yejue/fastapi-project-template&Date)