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
            parent = Acquisition.aq_parent(self)
            if parent is None:
                raise ValueError('Not enough context to acquire parent')

            base = Acquisition.aq_base(comp)
            comp = base.__of__(parent)

        return comp

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
