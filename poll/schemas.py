import uuid as uuid
from datetime import datetime
from typing import List

from django.db import models
from pydantic import BaseModel as BaseModel_


class BaseModel(BaseModel_):
    uuid: uuid.UUID
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_orms(cls, queryset: List[models.Model]):
        return [cls.from_orm(obj) for obj in queryset]


class FastBook(BaseModel):
    title: str

    class Config:
        orm_mode = True


class FastBooks(BaseModel_):
    items: List[FastBook]

    @classmethod
    def from_queryset(cls, qs):
        return cls(items=FastBook.from_orms(qs))
