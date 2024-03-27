from passlib.context import CryptContext

# 创建一个 hash 验证工具对象
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    """明文密码 hash 加密"""
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    """明文密码与哈希密码比对"""
    return pwd_context.verify(plain_password, hashed_password)


if __name__ == '__main__':
    passwd = get_password_hash("test")
    print(passwd)
