from Acquisition import aq_acquire
import plone.api as api
from plone.app.layout.viewlets.common import LogoViewlet
from plone.app.layout.navigation.root import getNavigationRoot
from borg.localrole.interfaces import IFactoryTempFolder
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.interfaces._content import IContentish

from collective.subsitebehaviors.behaviors import ISubSite


class SubsiteLogoViewlet(LogoViewlet):
    index = ViewPageTemplateFile('subsitelogoviewlet.pt')

    def __init__(self, context, request, view, manager=None):
        super(SubsiteLogoViewlet, self).__init__(context, request, view, manager)
        self.scaler = None
        self.subsitelogo = False
        self.scaled = False

    def update(self):

        nav_root = api.portal.get_navigation_root(context=self.context)
        self.logo = getattr(self.context, 'logoImage', None)

        if ISubSite.providedBy(nav_root) and self.logo:
            self.subsitelogo = True
            scaler = api.content.get_view("images", self.context, self.request)
            if "logo" in scaler.getAvailableSizes():
               self.scaled = True
            else:
               self.scaled = False
        else:
           self.subsitelogo = False
           super(SubsiteLogoViewlet, self).update()

