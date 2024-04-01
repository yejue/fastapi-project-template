from pydantic import BaseModel, Field


class NoteBaseSchema(BaseModel):
    """笔记基本 Schema"""
    title: str = Field(description="标题")
    content: str = Field(description="笔记内容")
    is_public: bool = Field(description="是否公开")


class NoteSchema(NoteBaseSchema):
    """笔记 Schema"""
    id: int
    user_id: int = Field(description="用户ID")


class NoteCreateSchema(NoteBaseSchema):
    """笔记创建 Schema"""
    pass


class NoteUpdateSchema(NoteBaseSchema):
    """笔记更新 Schema"""
    title: str = Field(None, description="标题")
    content: str = Field(None, description="笔记内容")
    is_public: bool = Field(None, description="是否公开")
    user_id: int = Field(None, description="用户ID")
