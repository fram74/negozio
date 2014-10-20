from django.db import models

# Create your models here.

from django.db import models
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField


class Novita(models.Model):
    titolo = models.CharField(max_length=70)
    sottotitolo = models.CharField(max_length=250)
    testo = HTMLField()
    immagine = FilerImageField(null=True, blank=True)

    def __unicode__(self):
        return u'%s (%s)' % (self.titolo, self.sottotitolo)