from tastypie.resources import ModelResource
from tastypie.constants import ALL

from apiserver.models import Whatever, Entry


class WhateverResource(ModelResource):
    class Meta:
        queryset = Whatever.objects.all()
        resource_set = 'whatever'
        filtering = {'title': ALL}


class EntryResource(ModelResource):
    class Meta:
        queryset = Entry.objects.all()

