from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import ForeignKey
from django.db.models import Model
from django.db.models import SlugField
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from grupo.models import Grupo


class SubGrupo(Model):
    nome = CharField(max_length=100)
    grupo = ForeignKey(Grupo, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)
    slug = SlugField(null=True, blank=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nome)

        super(SubGrupo, self).save(*args, **kwargs)