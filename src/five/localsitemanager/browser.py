from five.localsitemanager import make_objectmanager_site
from Products.Five.component.browser import ObjectManagerSiteView

class ObjectManagerSiteView(ObjectManagerSiteView):
    """Configure the site setup for an ObjectManager.
    """

    def makeSite(self):
        make_objectmanager_site(self.context)
