from peewee import *
from vaaya.contexts import Context


class DMoods(Model):
    log_time = DateTimeField()
    smiley = IntegerField()
    sad = IntegerField()
    angry = IntegerField()
    disgusted = IntegerField()
    fear = IntegerField()
    surprised = IntegerField()

    class Meta:
        database = Context.db
