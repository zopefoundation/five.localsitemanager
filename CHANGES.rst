Changelog
=========

5.1 (unreleased)
----------------

- Nothing changed yet.


5.0 (2025-02-15)
----------------

* Drop support for ``pkg_resources`` namespace and replace it with
  PEP 420 native namespace.
  Caution: This change requires to switch all packages in the `five`
  namespace to versions using a PEP 420 namespace.

* Drop support for Python 3.7, 3.8.

* Add support for Python 3.12, 3.13.

4.0 (2023-02-01)
----------------

* Drop support for Python 2.7, 3.5, 3.6.


3.4 (2022-12-16)
----------------

* Fix insidious buildout configuration bug for tests against Zope 4.

* Add support for Python 3.11.


3.3 (2022-04-11)
----------------

* Add support for Python 3.8, 3.9, 3.10.


3.2.2 (2018-11-09)
------------------

* Fix deprecation warnings.


3.2.1 (2018-10-11)
------------------

* Update the tests to a current `persistent` version.


3.2 (2018-10-05)
----------------

* Add support for Python 3.7


3.1 (2018-05-18)
----------------

* More PEP8 compliance.

* Avoid deprecation warnings in tests.

* Drop support for Python 3.4.


3.0.1 - 2017-05-27
------------------

* #4: Replace dependency on ZODB3 with persistent, add zope.site.


3.0.0 - 2017-05-23
------------------

* Target use with Zope 4: no longer support 2.13.x.

* Python 3 compatibility

* Added tox test scripts.


2.0.6 - 2017-05-02
------------------

* Don't complain if the site root has no Acquisition parent.
  [davisagli]

* Removed zope.site dependency. Using Zope 2.12 it is an indirect dependency
  and using Zope 2.13 or later it is no longer required.
  [yuppie]

* Ensure that the PersistentComponents has no aquisition wrapper before passing
  to the superclass, to allow the caching of component roots in zope.interface
  to make a weakref to this root.
  [MatthewWilkes]

2.0.5 - 2011-02-06
------------------

* Made the tests compatible with Zope 2.13.2.

2.0.4 - 2010-06-13
------------------

* Deal with deprecation warnings for Zope 2.13.

* Provide a more meaningful error message if the current site is not set
  correctly or the Acquisition chain of the site is messed up.
  [hannosch]

2.0.3 - 2010-01-02
------------------

* Made 'update_sitemanager_bases_handler' fail silently instead of raising an
  error. This allows to import broken sites, in particular old CMF sites.
  [yuppie]

2.0.2 - 2009-11-15
------------------

* Fix regression in five.localsitemanager 2.0.1 where unregistering a utility
  based on its provided interface broke if no utility was registered for that
  interface.
  [davisagli]

2.0.1 - 2009-10-19
------------------

* Adapt unregistering of components work to work with latest zope.component.
  [hannosch]

* Fix unregistering of components which have a physical path.
  [thefunny42]

2.0 - 2009-09-27
----------------

* Cleaned up package documentation and fixed spelling errors in the tests.
  [hannosch]

* Made sure that the __of__ method is only called on objects providing the
  IAcquirer interface.
  [hannosch]

* Updated forked registerUtility method to match the zope.component 3.7.1
  code base. This fixes the two bugs with the implicit unregistration of
  utilities for existing interface / name pairs.
  [hannosch]

* Simplified some code, aq_parent now respects __parent__ pointers.
  [hannosch]

2.0a1 - 2009-05-27
------------------

* Updated to use IObjectMovedEvent from zope.lifecycleevent instead of
  zope.container. We require zope.lifecycleevent >= 3.5.2 now.
  [hannosch]

* Removed package dependencies that did collide with the KGS of Zope 2.12.
  [yuppie]

* Adjusted code to use the new zope.site and zope.container packages and use
  the ISite interface from zope.location.
  [hannosch]

* Specify all package dependencies including Acquisition and Zope2. You need
  to use either the eggified Zope 2.12 or create fake-eggs for these.
  [hannosch]

* 'make_site' no longer stores the path of the site manager in its name. This
  way the name can't become out-dated. PersistentComponents' __repr__ method
  now returns the current path instead of the name of the site manager.
  [yuppie]

* Requiring zope.component >= 3.5.0.
  [icemac]

1.0 - 2008-11-18
----------------

* Utilities registered with an absolute path were returned with the
  RequestContainer in the aq_chain. As the result of the first utility
  look-up is stored in the adapter look-up cache, subsequent utility
  look-ups return the utlitiy with the RequestContainer of the first
  look-up.

  Solution: For utilities registered with an absolute path the
  RequestContainer is now also removed at look-up.
  [icemac]


1.0c1 - 2008-08-27
------------------

* Added buildout for project, so testing can be done using ``bin/test``.
  [icemac]

* Added ability to register utilities with an absolute path. These
  utilities are returned wrapped into their original context. This
  change is backward compatible to existing registries.

  But registering utilities having an acquisition context will behave
  different because these utilities will be returned in their original
  context. To restore the previous behavior, register utilities
  unwrapped (aq_base).

  For storing path information the component must implement
  getPhysicalPath and have an absolute path.

  When a component registered as utility is moved and registered again
  the path stored in registry gets updated.
  [icemac]


0.4 - 2008-07-23
----------------

* Rewrite PersistentComponents.registeredUtilities to not use
  internal methods. This makes it compatible with both zope.component <3.5.0dev
  and >3.5.0dev.
  [wichert]


0.3 - 2007-12-24
----------------

* Fixed potential aq problem when assigning various values to the utilities
  registry of the component registry.
  [hannosch]


0.2 - 2007-06-30
----------------

* Refactored and fixed aq wrapping: Nested site managers now return utilities
  wrapped in the right context. RequestContainers are removed and wrapped
  utilities are cached. This requires a special LookupClass called
  'FiveVerifyingAdapterLookup' in all 'utilities' registries used below a
  five.localsitemanager site.
  [yuppie, hannosch]


0.1.2 - 2007-06-23
------------------

* Corrected the zip-safe flag to be False.


0.1.1 - 2007-03-05
------------------

* Fixed aq wrapping when looking up a utility that is actually the component
  registry's parent (the ISite).


0.1 (2007-02-27)
----------------

* Initial version
