
class Settings:

    # Auth 加密配置
    SECRET_KEY = "123dc95d0fdccadae1369029a393d7dfe30d4f0bfa304e8010bd777938bc1808"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_SECONDS = 24 * 3600


def get_settings():
    return Settings()


settings = get_settings()

__all__ = ["settings"]
