from zope.component.globalregistry import base
from zope.app.component.interfaces import ISite
from zope.component.persistentregistry import PersistentComponents
from Products.Five.component.interfaces import IObjectManagerSite
from Products.Five.component import enableSite

def make_site(obj, iface=ISite):
    """Give the specified object required qualities to identify it as a proper
    ISite.
    """
    
    # we intentionally test for ISite and not iface
    if ISite.providedBy(obj):
        raise ValueError('This is already a site')
    
    enableSite(obj, iface=iface)
    
    components = PersistentComponents(name='five', bases=(base,))
    obj.setSiteManager(components)

def make_objectmanager_site(obj):
    make_site(obj, IObjectManagerSite)
