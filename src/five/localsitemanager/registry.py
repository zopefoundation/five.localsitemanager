import Acquisition
import zope.component.persistentregistry
import OFS.ObjectManager

_marker = object()

class PersistentComponents \
          (zope.component.persistentregistry.PersistentComponents,
           OFS.ObjectManager.ObjectManager):
    """An implementation of a component registry that can be persisted
    and looks like a standard ObjectManager.  It also ensures that all
    utilities have the the parent of this site manager (which should be
    the ISite) as their acquired parent.
    """

    def _wrap(self, comp):
        """Return an aq wrapped component with the site as the parent.
        """
        parent = Acquisition.aq_parent(self)
        if parent is None:
            raise ValueError('Not enough context to acquire parent')

        base = Acquisition.aq_base(comp)

        return Acquisition.ImplicitAcquisitionWrapper(base, parent)

    def queryUtility(self, provided, name=u'', default=None):
        comp = self.utilities.lookup((), provided, name, default)
        if comp is not default:
            comp = self._wrap(comp)
        return comp

    def getUtility(self, provided, name=u''):
        utility = self.queryUtility(provided, name, _marker)
        if utility is _marker:
            raise interfaces.ComponentLookupError(provided, name)
        return utility

    def getUtilitiesFor(self, interface):
        return ((name, self._wrap(utility))
                for name, utility in self.utilities.lookupAll((), interface))

    def getAllUtilitiesRegisteredFor(self, interface):
        return (self._wrap(x)
                for x in self.utilities.subscriptions((), interface))
