from django.db import models
from cms.models import CMSPlugin

# Create your models here.
class RawHTMLModel(CMSPlugin):
    html = models.TextField()

    class Meta:
        app_label = 'cmsplugin_rawhtml'
        