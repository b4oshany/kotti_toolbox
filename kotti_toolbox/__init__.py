# -*- coding: utf-8 -*-

"""
Created on 2017-01-03
:author: Oshane Bailey (b4.oshany@gmail.com)
"""

from kotti.resources import File
from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_toolbox')


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                kotti_toolbox.kotti_configure

        to enable the ``kotti_toolbox`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' kotti_toolbox'
    settings['kotti.alembic_dirs'] += ' kotti_toolbox:alembic'
    settings['kotti.available_types'] += ' kotti_toolbox.resources.CustomContent'
    settings['kotti.fanstatic.view_needed'] += ' kotti_toolbox.fanstatic.css_and_js'
    File.type_info.addable_to.append('CustomContent')


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    config.add_translation_dirs('kotti_toolbox:locale')
    config.add_static_view('static-kotti_toolbox', 'kotti_toolbox:static')

    config.scan(__name__)
