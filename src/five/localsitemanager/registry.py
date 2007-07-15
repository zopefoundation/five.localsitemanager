import Acquisition
import ComputedAttribute
from zope.component.interfaces import ComponentLookupError
import zope.component.persistentregistry
import zope.interface.adapter
import OFS.ObjectManager

_marker = object()

class AqAwareAdapterLookup(Acquisition.Explicit,
                           zope.interface.adapter.VerifyingAdapterLookup):
    """A lookup that is identical to VerifyingAdapterLookup except that
    it returns updated aq-wrapped components.
    """

    def lookup(self, *args, **kwargs):
        import pdb; pdb.set_trace()
        comp = super(AqAwareAdapterLookup, self).lookup(*args, **kwargs)
        return self._wrap(comp)

    def _wrap(self, comp):
        """Return an aq wrapped component with the site as the parent but
        only if the comp has an aq wrapper to begin with.
        """

        # BBB: The primary reason for doing this sort of wrapping of
        # returned utilities is to support CMF tool-like functionality where
        # a tool expects it's aq_parent to be the portal object.  New code
        # (ie new utilities) should not rely on this predictability to
        # get the portal object and should search out an alternate means
        # (possibly retrieve the ISiteRoot utility).  Although in most
        # cases getting at the portal object shouldn't be the required pattern
        # but instead looking up required functionality via other (possibly
        # local) components.

        if Acquisition.interfaces.IAcquirer.providedBy(comp):
            compregistry = self._registry._compregistry
            parent = Acquisition.aq_parent(compregistry)
            if parent is None:
                raise ValueError('Not enough context to acquire parent')

            base = Acquisition.aq_base(comp)

            if base is not Acquisition.aq_base(parent):
                # If the component is not the cmoponent registry container,
                # wrap it in the parent
                comp = base.__of__(parent)
            else:
                # If the component happens to be the component registry
                # container we are looking up a ISiteRoot.
                # We are not wrapping it in itself but in its own parent
                comp = base.__of__(Acquisition.aq_parent(parent))

        return comp

class PersistentAdapterRegistry \
          (Acquisition.Explicit,
           zope.component.persistentregistry.PersistentAdapterRegistry):
    """An adapter registry that uses a lookup delegate that is aq-aware.
    """

    LookupClass = AqAwareAdapterLookup

    def __init__(self, compregistry):
        super(PersistentAdapterRegistry, self).__init__()
        self._compregistry  = compregistry

class PersistentComponents \
          (zope.component.persistentregistry.PersistentComponents,
           OFS.ObjectManager.ObjectManager):
    """An implementation of a component registry that can be persisted
    and looks like a standard ObjectManager.  It also ensures that all
    utilities have the the parent of this site manager (which should be
    the ISite) as their acquired parent.
    """

    def __init__(self, *args, **kwargs):
        super(PersistentComponents, self).__init__(*args, **kwargs)

    def _init_registries(self):
        self.adapters = zope.component.persistentregistry.\
                        PersistentAdapterRegistry()
        # get our aq aware registry
        self.utilities = PersistentAdapterRegistry(self)
