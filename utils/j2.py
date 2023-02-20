from jinja2 import (
    Environment,
    FileSystemLoader,
    select_autoescape
)

from settings import config
""" from apps.site.utils.i18n import get_translation, _ """


templateLoader = FileSystemLoader(searchpath="templates")
env = Environment(
    loader=templateLoader,
    extensions=['jinja2.ext.i18n'],
    autoescape=select_autoescape(['html']),
)

#Supported locales
""" language_names = {} """
""" for lang in config.SUPPORTED_LOCALES:
    language_names[lang] = _("Language name", locale=lang) """


def render_template(
    template_name: str,
    context: dict = {},
    locale: str = 'en'
):
    context['locale'] = locale
    """ translations = get_translation(locale) """
    """ env.install_gettext_translations(translations) """
    template = env.get_template(template_name)
    return template.render(**context)

def static_url(name):
    return name