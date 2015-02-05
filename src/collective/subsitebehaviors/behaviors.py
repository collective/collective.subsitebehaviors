from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model


from . import _

class ISubSite(model.Schema):
   """Behavior interface to add a customer logo etc.
   """

   model.fieldset('customization', label=u"Customization", fields=['logoImage'])

   logoImage = NamedBlobImage(
      title=_(u"Custom logo"),
      description=u"Custom logo to be used",
      required=False
   )

alsoProvides(ISubSite, IFormFieldProvider)
