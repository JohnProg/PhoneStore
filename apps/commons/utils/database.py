from django.db import models


class AuditableMixin(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    modified = models.DateTimeField(
        editable=False,
        auto_now=True
    )

    class Meta:
        abstract = True


class SoftDeleteQuerySet(models.QuerySet):
    def not_deleted(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)


SoftDeleteManager = SoftDeleteQuerySet.as_manager()


class SoftDeleteMixin(models.Model):
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager

    class Meta:
        abstract = True
