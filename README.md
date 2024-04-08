## Introduction

U-Ping 是一个笔记分享和供你评论的 Web 服务，目前它仅仅是用于 FastAPI 的项目结构展示。
这个项目结构基本参照了这个项目 [fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices)，之所以做这些改动是源于我在 Django 中的文件目录习惯。

本项目的局限是 FastAPI 全部的组件还需要一段时间的使用，以及像是 Alembic 的使用和 SQlAlchemy 2.0 的查询以及异步这些等等事项，我会在实际使用后
对项目进行一些优化。

这个项目一直会在保持简单清晰的前提下进行更新扩展。


## Features

 - 简单清晰的 FastAPI 项目结构
 - 身份验证和简便的权限认证
 - 对象级别校验（这个方案可扩展性很强）
 - 中间件


## QuickStart
1. fork this project
2. git clone your-project-url
3. cd your-project
4. pip install -r requirements
5. python main.py


## Project Structure

待更新...（会在项目更加稳定的时候更新这个内容）


## TODOs

- [ ] db 提交整合
- [ ] 统一全局响应
- [ ] 精简 Schema
- [ ] 将 permission 相关类移动到更合理的位置
- [ ] 引入持久部署方案
- [ ] 引入数据表迁移方案
