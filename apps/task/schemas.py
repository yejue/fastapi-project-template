from pydantic import BaseModel, Field


class AddTwoNumSchema(BaseModel):
    """两数相加"""
    num1: int = Field(description="数字 1")
    num2: int = Field(description="数字 2")
