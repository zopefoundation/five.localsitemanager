from Acquisition import aq_parent, aq_inner
from zope import interface
from zope.component.globalregistry import base
from zope.traversing.interfaces import IContainmentRoot
from zope.app.component.interfaces import ISite
from five.localsitemanager.registry import PersistentComponents
from five.localsitemanager import interfaces
from Products.Five.component.interfaces import IObjectManagerSite
from Products.Five.component import enableSite, disableSite

def make_site(obj, iface=ISite):
    """Give the specified object required qualities to identify it as a proper
    ISite.
    """
    
    # we intentionally test for ISite and not iface
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

def make_objectmanager_site(obj):
    """Just a bit of sugar coating to make an unnofficial objectmanager
    based site.
    """
    
    make_site(obj, IObjectManagerSite)

def get_parent(obj):
    """Returns the container the object was traversed via.  This
    is a version of zope.traversing.api.getParent that is designed to
    handle acquisition as well.

    Returns None if the object is a containment root.
    Raises TypeError if the object doesn't have enough context to get the
    parent.
    """
    
    if IContainmentRoot.providedBy(obj):
        return None
    
    parent = getattr(obj, '__parent__', None)
    if parent is not None:
        return parent

    parent = aq_parent(aq_inner(obj))
    if parent is not None:
        return parent

    raise TypeError("Not enough context information to get parent", obj)


def find_next_sitemanager(site):
    """Find the closest sitemanager that is not the specified site's
    sitemanager.
    """
    
    container = site
    sm = None
    while sm is None:
        if IContainmentRoot.providedBy(container):
            # we're the root site, return None
            return None

        try:
            container = get_parent(container)
            if container is None:
                return None
        except TypeError:
            # there was not enough context; probably run from a test
            return None

        if ISite.providedBy(container):
            sm = container.getSiteManager()
    return sm

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

def update_sitemanager_bases_handler(site, event):
    update_sitemanager_bases(site)
