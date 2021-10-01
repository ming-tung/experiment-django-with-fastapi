import uuid as uuid
from datetime import datetime
from typing import List

from django.db import models
from pydantic import BaseModel as BaseModel_


class BaseSchema(BaseModel_):
    # The fields from `models.BaseModelMixin`

    uuid: uuid.UUID
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_orms(cls, queryset: List[models.Model]):
        return [cls.from_orm(obj) for obj in queryset]


class _BookSchema(BaseModel_):

    title: str


class BookSchema(_BookSchema, BaseSchema):
    class Config:
        orm_mode = True


class BooksSchema(BaseModel_):
    items: List[BookSchema]

    @classmethod
    def from_queryset(cls, qs):
        return cls(items=BookSchema.from_orms(qs))
