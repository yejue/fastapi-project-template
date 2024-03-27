from datetime import datetime, timezone, timedelta

from jose import JWTError, jwt


def create_access_token(
        data: dict,
        secret_key: str,
        expire_seconds: int = 30 * 60,
        algorithm: str = "HS256"
):
    """创建 Token"""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expire_seconds)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt


def decrypt_access_token(token: str, secret_key: str, algorithms=("HS256",)):
    """Token 解密"""
    payload = jwt.decode(token=token, key=secret_key, algorithms=algorithms)
    return payload


if __name__ == '__main__':
    temp_data = {"user_id": "1"}
    key = "123dc95d0fdccadae1369029a393d7dfe30d4f0bfa304e8010bd777938bc1808"
    res = create_access_token(temp_data, key)
    print(res)
    token_data = decrypt_access_token(res, key)
    print(token_data)
