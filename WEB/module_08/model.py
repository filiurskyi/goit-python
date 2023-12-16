from datetime import datetime

from mongoengine import Document, EmbeddedDocument, ReferenceField
from mongoengine.fields import (BooleanField, DateTimeField,
                                EmbeddedDocumentField, ListField, StringField)


class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    date_modified = DateTimeField(default=datetime.utcnow)
    date_created = DateTimeField(default=datetime.utcnow)


class Tag(EmbeddedDocument):
    tag = StringField()


class Quote(Document):
    author = ReferenceField(Author)
    tags = ListField(EmbeddedDocumentField(Tag))
    quote = StringField(required=True)
    date_modified = DateTimeField(default=datetime.utcnow)
    date_created = DateTimeField(default=datetime.utcnow)


# person_dict = {
#     "fullname": fullname,
#     "born_date": born_date,
#     "born_location": born_location,
#     "description": description,
# }
#
# quote_dict = {
#     "tags": [],
#     "author": author,
#     "quote": quote,
# }
