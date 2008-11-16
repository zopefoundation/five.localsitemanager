from Acquisition import aq_base
from zope.component.globalregistry import base
from zope.traversing.interfaces import IContainmentRoot
from zope.app.component.interfaces import ISite
from five.localsitemanager.registry import PersistentComponents
from five.localsitemanager.utils import get_parent
from Products.Five.component.interfaces import IObjectManagerSite
from Products.Five.component import enableSite


def make_site(obj, iface=ISite):
    """Give the specified object required qualities to identify it as a proper
    ISite.
    """
    if ISite.providedBy(obj):
        raise ValueError('This is already a site')
    
    next = find_next_sitemanager(obj)
    if next is None:
        next = base

    enableSite(obj, iface=iface)

    name = 'five'
    path = getattr(obj, 'getPhysicalPath', None)
    if path is not None and callable(path):
        name = '/'.join(path())

    components = PersistentComponents(name=name, bases=(next,))
    obj.setSiteManager(components)
    components.__parent__ = aq_base(obj)


def make_objectmanager_site(obj):
    """Just a bit of sugar coating to make an unnofficial objectmanager
    based site.
    """
    make_site(obj, IObjectManagerSite)

# Zope 3 version: zope.app.component.site._findNextSiteManager
def find_next_sitemanager(site):
    """Find the closest sitemanager that is not the specified site's
    sitemanager.
    """
    while True:
        if IContainmentRoot.providedBy(site):
            # we're the root site, return None
            return None

        try:
            site = get_parent(site)
        except TypeError:
            # there was not enough context; probably run from a test
            return None

        if ISite.providedBy(site):
            return site.getSiteManager()

def update_sitemanager_bases(site):
    """Formulate the most appropriate __bases__ value for a site's site manager
    by asking find_next_sitemanager what the next appropriate site manager
    is.  After this call, the __bases__ is guaranteed to have one and only
    one value in the __bases__ list/tuple.
    """
    next = find_next_sitemanager(site)
    if next is None:
        next = base
    sm = site.getSiteManager()
    sm.__bases__ = (next, )

# Zope 3 version: zope.app.component.site.changeSiteConfigurationAfterMove
def update_sitemanager_bases_handler(site, event):
    """After a site is moved, its site manager links have to be updated."""
    if event.newParent is not None:
        update_sitemanager_bases(site)
