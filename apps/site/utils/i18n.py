""" from babel.support import Translations, NullTranslations

from apps.payments.settings import config


translations = {
    name: Translations.load(config.L10N_LOCALES_DIR, locales=[name])
    for name in config.SUPPORTED_LOCALES
} or {}


def get_translation(locale: str = None):
    if not locale:
        locale = config.DEFAULT_LOCALE
    tr = translations.get(locale)
    if not tr:
        tr = NullTranslations()
    return tr


def translate_text(text: str, locale: str = None):
    if not locale:
        locale = config.DEFAULT_LOCALE
    return translations[locale].gettext(text)


def translate_plural(
        text_singular: str,
        text_plural: str,
        ncount: int,
        locale: str = None
):
    if not locale:
        locale = config.DEFAULT_LOCALE

    return translations[locale].ngettext(
        text_singular,
        text_plural,
        ncount
    )


_ = translate_text

_n = translate_plural """
