import uuid as uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import (
    CreationDateTimeField,
    ModificationDateTimeField,
)

from poll.schemas import _BookSchema


class BaseModelMixin(models.Model):
    uuid = models.UUIDField(
        unique=True, db_index=True, default=uuid.uuid4, editable=False
    )
    created_at = CreationDateTimeField(
        _('Created at'),
    )
    updated_at = ModificationDateTimeField(_('Updated at'))

    class Meta:
        abstract = True


class Book(BaseModelMixin, models.Model):
    title = models.CharField(max_length=200, unique=True)

    @classmethod
    def from_api(cls, book: _BookSchema):
        return cls(title=book.title)
