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

1. fork this project
2. git clone your-project-url
3. cd your-project
4. pip install -r requirements
5. python main.py


## 📂Project Structure

待更新...（会在项目更加稳定的时候更新这个内容）


## 📔TODOs

- [ ] db 提交整合以及异步
- [ ] 统一全局响应
- [ ] 精简 Schema
- [ ] 将 permission 相关类移动到更合理的位置
- [ ] 引入持久部署方案
- [ ] 引入数据表迁移方案



## ⭐Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yejue/fastapi-project-template&type=Date)](https://star-history.com/#yejue/fastapi-project-template&Date)