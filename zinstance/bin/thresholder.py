#!/opt/plone/zinstance/bin/python2.7
#
# The Python Imaging Library
# $Id$
#
# this demo script illustrates how a 1-bit BitmapImage can be used
# as a dynamically updated overlay
#

try:
    from tkinter import *
except ImportError:
    from Tkinter import *



import sys
sys.path[0:0] = [
  '/opt/plone/buildout-cache/eggs/Plone-5.0.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Pillow-3.1.1-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.upgrade-1.3.24-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.openid-2.1.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.iterate-3.1.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.dexterity-2.1.20-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.caching-1.2.10-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.CMFPlone-5.0.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.CMFPlacefulWorkflow-1.6.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.ATContentTypes-2.2.11-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.Archetypes-1.10.13-py2.7.egg',
  '/opt/plone/zinstance/lib/python2.7/site-packages',
  '/opt/plone/buildout-cache/eggs/Zope2-2.13.24-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.ZCatalog-3.0.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.SecureMailHost-1.1.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.ResourceRegistries-3.0.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.PortalTransforms-2.2.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.PluggableAuthService-1.11.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.PlonePAS-5.0.9-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.MimetypesRegistry-2.0.8-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.GenericSetup-1.8.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.DCWorkflow-2.2.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.CMFUid-2.2.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.CMFQuickInstallerTool-3.0.13-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.CMFFormController-3.0.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.CMFEditions-2.2.19-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.CMFDiffTool-3.0.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.CMFCore-2.2.10-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.contentmigration-2.1.12-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Acquisition-4.2.2-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/zope.site-3.9.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.ramcache-1.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.location-3.9.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.interface-3.6.7-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/zope.component-3.9.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/transaction-1.1.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.portlets-3.1.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.folder-1.2.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.session-3.5.6-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.portlets-2.2.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/five.localsitemanager-2.0.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/borg.localrole-3.1.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.i18nmessageid-3.5.3-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/plone.openid-2.0.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/ZODB3-3.10.5-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/Products.statusmessages-4.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/DateTime-4.0.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.viewlet-3.7.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.schema-4.4.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.lifecycleevent-3.6.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.event-3.5.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.annotation-3.5.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.memoize-1.2.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.locking-2.1.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/z3c.form-3.2.9-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.publisher-3.12.6-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.deprecation-3.4.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.browserpage-3.12.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.z3cform-0.8.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.supermodel-1.2.7-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.contentrules-2.0.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.autoform-1.6.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.z3cform-1.2.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.uuid-1.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.layout-2.5.19-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.content-3.0.20-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/lxml-3.5.0-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/plone.schemaeditor-2.0.9-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.rfc822-1.1.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.namedfile-3.0.8-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.formwidget.namedfile-1.0.15-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.dexterity-2.4.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.behavior-1.1.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.textfield-1.2.6-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/z3c.zcmlhook-1.0b1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.CMFDynamicViewFTI-4.1.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.registry-1.0.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.protect-3.0.18-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.pagetemplate-3.6.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.browserresource-3.10.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.registry-1.3.11-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.cachepurging-1.0.11-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.caching-1.0.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/python_dateutil-2.4.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.traversing-3.13.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.tales-3.5.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.tal-3.5.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.structuredtext-3.5.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.i18n-3.7.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.dottedname-3.4.6-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.deferredimport-3.5.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.container-3.11.2-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/zope.cachedescriptors-3.5.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.app.locales-3.6.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/z3c.autoinclude-0.3.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/slimit-0.8.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plonetheme.barceloneta-1.6.18-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.theme-3.0.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.schema-1.0.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.portlet.static-3.0.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.portlet.collection-3.0.6-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.outputfilters-2.1.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.intelligenttext-2.1.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.indexer-1.0.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.i18n-3.0.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.browserlayer-2.1.6-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.batching-1.1.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.workflow-2.2.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.vocabularies-2.2.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.viewletmanager-2.0.9-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.users-2.3.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.theming-1.2.19-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.redirector-1.3.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.locales-5.0.9-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.linkintegrity-3.0.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.multilingual-3.0.16-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.i18n-3.0.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.discussion-2.4.11-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.customerize-1.3.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.controlpanel-3.0.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.contenttypes-1.2.11-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.contentrules-4.0.10-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.contentmenu-2.1.7-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.contentlisting-1.2.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.api-1.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/mockup-2.1.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/five.pt-2.2.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/five.customerize-1.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/cssmin-0.2.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.PluginRegistry-1.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.PlacelessTranslationService-2.0.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.PasswordResetTool-2.2.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.ExternalEditor-1.1.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.ExtendedPathIndex-3.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/ExtensionClass-4.1.2-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/ZConfig-2.9.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.validation-2.0.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.widgets-2.0.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.collection-1.1.6-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.blob-1.6.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.uuid-1.0.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.folder-1.0.7-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.ZSQLMethods-2.13.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.datetime-3.4.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.contenttype-3.5.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.StandardCacheManagers-2.13.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.PythonScripts-2.13.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.MIMETools-2.13.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.MailHost-2.13.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.ExternalMethod-2.13.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.BTreeFolder2-2.14.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.testing-3.9.7-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.testbrowser-3.11.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.size-3.4.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.sequencesort-3.4.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.sendmail-3.7.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.security-3.7.4-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/zope.ptresource-3.9.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.proxy-3.6.1-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/zope.processlifetime-1.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.exceptions-3.6.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.contentprovider-3.7.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.configuration-3.7.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.browsermenu-3.9.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.browser-1.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zLOG-2.11.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zExceptions-2.13.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zdaemon-2.0.7-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/tempstorage-2.12.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/pytz-2015.7-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/initgroups-2.13.0-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/docutils-0.12-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/ZopeUndo-2.12.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/RestrictedPython-3.6.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Record-2.13.0-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/Products.ZCTextIndex-2.13.5-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/Products.OFSP-2.13.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Persistence-2.13.2-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/MultiMapping-2.13.0-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/Missing-2.13.1-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/DocumentTemplate-2.13.2-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/AccessControl-3.0.12-py2.7-linux-x86_64.egg',
  '/opt/plone/buildout-cache/eggs/Markdown-2.6.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.formlib-4.0.6-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.ZopeVersionControl-1.1.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.copy-3.5.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.app.publication-3.12.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/feedparser-5.2.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.keyring-3.0.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/python_openid-2.2.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zc.lockfile-1.0.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/six-1.10.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.componentvocabulary-1.0.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.globalrequest-1.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/z3c.formwidget.query-0.12-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.scale-1.4.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.app.file-3.6.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.filerepresentation-3.6.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.synchronize-1.0.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.alterego-1.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/collective.monkeypatcher-1.1.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/five.globalrequest-1.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/repoze.xmliter-0.6-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.transformchain-1.1.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/z3c.caching-2.0a1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.broken-3.6.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/ply-3.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Unidecode-0.4.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.querystring-1.3.14-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/roman-1.4.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.subrequest-1.6.11-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.resourceeditor-2.0.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.resource-1.0.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/diazo-1.2.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.relationfield-1.3.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.intid-1.1.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/z3c.relationfield-0.7-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/archetypes.multilingual-3.0.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.lockingbehavior-1.0.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.versioningbehavior-1.2.7-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.event-2.0.7-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.stringinterp-1.1.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/decorator-4.0.9-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Chameleon-2.24-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/z3c.pt-3.0.0a1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/sourcecodegen-0.6.14-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/python_gettext-3.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.app.imaging-2.0.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/archetypes.schemaextender-2.1.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/mechanize-0.2.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.error-3.7.4-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.authentication-3.7.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.dublincore-3.7.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/future-0.15.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/cssselect-0.9.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/five.intid-1.1.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.intid-3.7.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zc.relation-1.0-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/z3c.objpath-1.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.formwidget.recurrence-2.0.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/plone.event-1.3-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/icalendar-3.9.2-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/collective.elephantvocabulary-0.2.5-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/Products.DateRecurringIndex-2.1-py2.7.egg',
  '/opt/plone/buildout-cache/eggs/zope.keyreference-3.6.4-py2.7.egg',
  ]


from PIL import Image, ImageTk
import sys

#
# an image viewer


class UI(Frame):
    def __init__(self, master, im, value=128):
        Frame.__init__(self, master)

        self.image = im
        self.value = value

        self.canvas = Canvas(self, width=im.size[0], height=im.size[1])
        self.backdrop = ImageTk.PhotoImage(im)
        self.canvas.create_image(0, 0, image=self.backdrop, anchor=NW)
        self.canvas.pack()

        scale = Scale(self, orient=HORIZONTAL, from_=0, to=255,
                      resolution=1, command=self.update_scale, length=256)
        scale.set(value)
        scale.bind("<ButtonRelease-1>", self.redraw)
        scale.pack()

        # uncomment the following line for instant feedback (might
        # be too slow on some platforms)
        # self.redraw()

    def update_scale(self, value):
        self.value = eval(value)

        self.redraw()

    def redraw(self, event=None):

        # create overlay (note the explicit conversion to mode "1")
        im = self.image.point(lambda v, t=self.value: v >= t, "1")
        self.overlay = ImageTk.BitmapImage(im, foreground="green")

        # update canvas
        self.canvas.delete("overlay")
        self.canvas.create_image(0, 0, image=self.overlay, anchor=NW,
                                 tags="overlay")

# --------------------------------------------------------------------
# main

root = Tk()

im = Image.open(sys.argv[1])

if im.mode != "L":
    im = im.convert("L")

# im.thumbnail((320,200))

UI(root, im).pack()

root.mainloop()
