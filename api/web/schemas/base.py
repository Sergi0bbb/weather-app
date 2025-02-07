from pydantic import BaseModel, ConfigDict


class BaseModelSchema(BaseModel):
    """Base model for all schemas"""
    model_config = ConfigDict(
        extra="ignore",
        from_attributes=True,
    )
