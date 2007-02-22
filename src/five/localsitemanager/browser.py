from five.localsitemanager.components import FivePersistentComponents
from zope.component.globalregistry import base

from Products.Five.component.browser import ObjectManagerSiteView
from Products.Five.component.interfaces import IObjectManagerSite
from Products.Five.component import enableSite

class ObjectManagerSiteView(ObjectManagerSiteView):
    """Configure the site setup for an ObjectManager.
    """

    def makeSite(self):
        if IObjectManagerSite.providedBy(self.context):
            raise ValueError('This is already a site')

        enableSite(self.context, iface=IObjectManagerSite)

        #TODO in the future we'll have to walk up to other site
        # managers and put them in the bases
        components = FivePersistentComponents()
        components.__bases__ = (base,)
        self.context.setSiteManager(components)
