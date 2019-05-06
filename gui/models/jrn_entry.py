from peewee import *
from vaaya.contexts import Context


# Database for Journal Entry storage
class JrnEntry(Model):
    log_time = DateTimeField()
    journal = TextField()
    analysis = TextField()

    class Meta:
        database = Context.db
