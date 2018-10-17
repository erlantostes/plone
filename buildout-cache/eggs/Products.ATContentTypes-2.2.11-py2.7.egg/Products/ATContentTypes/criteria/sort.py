# -*- coding: utf-8 -*-
from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import BooleanField
from Products.Archetypes.atapi import BooleanWidget
from Products.Archetypes.atapi import Schema
from Products.ATContentTypes import ATCTMessageFactory as _
from Products.ATContentTypes.criteria import registerCriterion
from Products.ATContentTypes.criteria import SORT_INDICES
from Products.ATContentTypes.criteria.base import ATBaseCriterion
from Products.ATContentTypes.criteria.schemata import ATBaseCriterionSchema
from Products.ATContentTypes.interfaces import IATTopicSortCriterion
from Products.ATContentTypes.permission import ChangeTopics
from Products.CMFCore.permissions import View
from zope.interface import implements


ATSortCriterionSchema = ATBaseCriterionSchema + Schema((
    BooleanField('reversed',
                 required=0,
                 mode="rw",
                 write_permission=ChangeTopics,
                 default=0,
                 widget=BooleanWidget(label=_(u'Reverse')),
                 ),

))


class ATSortCriterion(ATBaseCriterion):
    """A sort criterion"""

    implements(IATTopicSortCriterion)
    security = ClassSecurityInfo()
    schema = ATSortCriterionSchema
    meta_type = 'ATSortCriterion'
    archetype_name = 'Sort Criterion'
    shortDesc = 'Sort'

    @security.protected(View)
    def getCriteriaItems(self):
        result = [('sort_on', self.Field())]

        if self.getReversed():
            result.append(('sort_order', 'reverse'))

        return tuple(result)

registerCriterion(ATSortCriterion, SORT_INDICES)
