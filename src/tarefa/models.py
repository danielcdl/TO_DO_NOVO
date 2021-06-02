from django.db.models import Model
from django.db.models import ForeignKey
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import TextField
from django.db.models import BooleanField
from django.db.models import DateTimeField
from django.db.models import SlugField
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify

from grupo.models import Grupo
from subgrupo.models import SubGrupo

class Tarefa(Model):
    title = CharField(max_length=100)
    description = TextField(null=True, blank=True)
    complete = BooleanField()
    created = DateTimeField(auto_now_add=True)
    slug = SlugField(null=True, blank=True)
    user = ForeignKey(User, on_delete=CASCADE)
    grupo = ForeignKey(Grupo, on_delete=CASCADE, null=True)
    subgrupo = ForeignKey(SubGrupo, on_delete=CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('subgrupos', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Tarefa, self).save(*args, **kwargs)

    class Meta:
        ordering = ['complete']