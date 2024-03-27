from .schemas import HelloUserModel


class UserService:
    """用户相关逻辑类"""

    @staticmethod
    def add_user_to_database(user: HelloUserModel):
        # 模拟将 user 存入数据库
        print(f"{user.name} 存入成功")
