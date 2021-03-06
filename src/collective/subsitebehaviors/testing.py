# -*- coding: utf-8 -*-
"""Base module for unittesting."""

from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import applyProfile
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.testing import z2

import collective.subsitebehaviors


class CollectiveSubsiteBehaviorsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)
    products = [
        'collective.subsitebehaviors',
    ]

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        self.loadZCML(package=collective.subsitebehaviors,
                      name='testing.zcml')
        for product in self.products:
            z2.installProduct(app, product)

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        applyProfile(portal, 'collective.subsitebehaviors:testing')

        # Login and create some test content
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)

    def tearDownZope(self, app):
        """Tear down Zope."""
        for product in reversed(self.products):
            z2.uninstallProduct(app, product)


FIXTURE = CollectiveSubsiteBehaviorsLayer(
    name='FIXTURE'
    )


INTEGRATION = IntegrationTesting(
    bases=(FIXTURE,),
    name='INTEGRATION'
    )


FUNCTIONAL = FunctionalTesting(
    bases=(FIXTURE,),
    name='FUNCTIONAL'
    )


ACCEPTANCE = FunctionalTesting(
    bases=(FIXTURE, AUTOLOGIN_LIBRARY_FIXTURE, z2.ZSERVER_FIXTURE),
    name='ACCEPTANCE'
    )
