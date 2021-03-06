plone.rfc822 marshaler
======================

This package includes a field marshaler for ``plone.rfc822``

Next, we will create a simple schema with which to test the marshaler

    >>> from zope.interface import Interface
    >>> from z3c.relationfield import Relation, RelationChoice, RelationList

    >>> class ITestContent(Interface):
    ...     _relation = Relation()
    ...     _relationChoice = RelationChoice(values=[])
    ...     _relationList = RelationList()

We'll create an instance with some data, too. Note that for the purposes of
this test, we don't bother creating actual relations in the relationship
catalog. All we care about is the 'to_id' variable.

    >>> from z3c.relationfield import RelationValue
    >>> from zope.interface import implements
    >>> class TestContent(object):
    ...     implements(ITestContent)
    ...     _relation = RelationValue(123)
    ...     _relationChoice = RelationValue(234)
    ...     _relationList = [RelationValue(345), RelationValue(456)]

    >>> t = TestContent()

We can now look up and test the marshaler:

    >>> from zope.component import getMultiAdapter
    >>> from plone.rfc822.interfaces import IFieldMarshaler

Relation field
--------------

    >>> marshaler = getMultiAdapter((t, ITestContent['_relation']), IFieldMarshaler)
    >>> marshaler.marshal()
    '123'
    >>> decoded = marshaler.decode('123')
    >>> decoded.to_id
    123
    >>> marshaler.getContentType() is None
    True
    >>> marshaler.getCharset('utf-8') is None
    True
    >>> marshaler.ascii
    True

Relation choice
---------------

    >>> marshaler = getMultiAdapter((t, ITestContent['_relationChoice']), IFieldMarshaler)
    >>> marshaler.marshal()
    '234'
    >>> decoded = marshaler.decode('234')
    >>> decoded.to_id
    234
    >>> marshaler.getContentType() is None
    True
    >>> marshaler.getCharset('utf-8') is None
    True
    >>> marshaler.ascii
    True

Relation list
-------------

    >>> marshaler = getMultiAdapter((t, ITestContent['_relationList']), IFieldMarshaler)
    >>> marshaler.marshal()
    '345||456'
    >>> decoded = marshaler.decode('345||456')
    >>> len(decoded)
    2
    >>> decoded[0].to_id
    345
    >>> decoded[1].to_id
    456
    >>> marshaler.getContentType() is None
    True
    >>> marshaler.getCharset('utf-8') is None
    True
    >>> marshaler.ascii
    True
