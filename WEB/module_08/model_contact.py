from datetime import datetime

from mongoengine import CASCADE, Document, EmbeddedDocument, ReferenceField
from mongoengine.fields import (BooleanField, DateTimeField,
                                EmbeddedDocumentField, ListField, StringField)


class Contact(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    personal_email = StringField(required=True)
    address = StringField()
    sent_flag = BooleanField(default=False)

    date_modified = DateTimeField(default=datetime.utcnow)
    date_created = DateTimeField(default=datetime.utcnow)

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def business_email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@microsoft.com"
