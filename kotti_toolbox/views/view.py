# -*- coding: utf-8 -*-

"""
Created on 2017-01-03
:author: Oshane Bailey (b4.oshany@gmail.com)
"""

from pyramid.view import view_config
from pyramid.view import view_defaults

from kotti_toolbox import _
from kotti_toolbox.resources import CustomContent
from kotti_toolbox.fanstatic import css_and_js
from kotti_toolbox.views import BaseView


@view_defaults(context=CustomContent, permission='view')
class CustomContentViews(BaseView):
    """ Views for :class:`kotti_toolbox.resources.CustomContent` """

    @view_config(name='view', permission='view',
                 renderer='kotti_toolbox:templates/custom-content-default.pt')
    def default_view(self):
        """ Default view for :class:`kotti_toolbox.resources.CustomContent`

        :result: Dictionary needed to render the template.
        :rtype: dict
        """

        return {
            'foo': _(u'bar'),
        }

    @view_config(name='alternative-view', permission='view',
                 renderer='kotti_toolbox:templates/custom-content-alternative.pt')
    def alternative_view(self):
        """ Alternative view for :class:`kotti_toolbox.resources.CustomContent`.
        This view requires the JS / CSS resources defined in
        :mod:`kotti_toolbox.fanstatic`.

        :result: Dictionary needed to render the template.
        :rtype: dict
        """

        css_and_js.need()

        return {
            'foo': _(u'bar'),
        }
