__author__ = 'Francesco'
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from cmsplugin_rawhtml.models import RawHTMLModel

class RawHTMLPlugin(CMSPluginBase):
    model = RawHTMLModel
    name = _('Raw HTML')
    render_template = 'cmsplugin_rawhtml/raw_html_plugin.html'
    text_enabled = True

    def render(self, context, instance, placeholder):
        context['self'] = instance
        return context

plugin_pool.register_plugin(RawHTMLPlugin)