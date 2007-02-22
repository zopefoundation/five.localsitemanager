import zope.component.persistentregistry
import OFS.ObjectManager

class PersistentComponents \
          (zope.component.persistentregistry.PersistentComponents,
           OFS.ObjectManager.ObjectManager):
    """An implementation of a component registry that can be persisted
    and looks like a standard ObjectManager.
    """
