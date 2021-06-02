from django.db.models import Model
from django.db.models import CharField
from django.db.models import SlugField
from django.db.models import CASCADE
from django.db.models import ForeignKey
from django.db.models import URLField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Grupo(Model):
    nome = CharField(max_length=100, unique=True)
    user = ForeignKey(User, on_delete=CASCADE)
    slug = SlugField(null=True, blank=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nome)

        super(Grupo, self).save(*args, **kwargs)
