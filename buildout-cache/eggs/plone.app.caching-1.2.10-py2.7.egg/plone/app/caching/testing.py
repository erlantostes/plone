from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.interface import implements

from zope.component import getUtility
from zope.component import provideUtility

from zope.configuration import xmlconfig

from plone.cachepurging.interfaces import IPurger

try:
    from plone.protect.authenticator import _getKeyring
except ImportError:
    # so we can run tests on plone 4.3
    from plone.keyring.interfaces import IKeyManager
    def _getKeyring(username):
        manager = getUtility(IKeyManager)
        return manager['_system']

import hmac
from hashlib import sha1 as sha


class FauxPurger(object):

    implements(IPurger)

    def __init__(self):
        self.reset()

    def reset(self):
        self._sync = []
        self._async = []

    def purgeAsync(self, url, httpVerb='PURGE'):
        self._async.append(url)

    def purgeSync(self, url, httpVerb='PURGE'):
        self._sync.append(url)

    def stopThreads(self, wait=False):
        pass

    errorHeaders = ('X-Squid-Error',)
    http_1_1 = True


class PloneAppCaching(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):

        # Load ZCML
        import plone.app.caching
        xmlconfig.file('configure.zcml', plone.app.caching, context=configurationContext)

        # Install fake purger
        self.oldPurger = getUtility(IPurger)
        provideUtility(FauxPurger(), IPurger)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plone.app.caching:default')

        portal['portal_workflow'].setDefaultChain('simple_publication_workflow')

    def tearDownZope(self, app):
        # Store old purger
        provideUtility(self.oldPurger, IPurger)


PLONE_APP_CACHING_FIXTURE = PloneAppCaching()
PLONE_APP_CACHING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_APP_CACHING_FIXTURE,), name="PloneAppCaching:Integration")
PLONE_APP_CACHING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONE_APP_CACHING_FIXTURE,), name="PloneAppCaching:Functional")


def getToken(username):
    ring = _getKeyring(username)
    secret = ring.random()
    return hmac.new(secret, username, sha).hexdigest()
