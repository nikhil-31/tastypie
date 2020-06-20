from tastypie.resources import ModelResource
from tastypie.constants import ALL
from tastypie.authorization import Authorization

from apiserver.models import Whatever, Entry
from django.contrib.auth.models import User
from tastypie import fields


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        includes = ['username', 'first_name', 'last_name', 'last_login']
        allowed_methods = ['get']


class WhateverResource(ModelResource):
    class Meta:
        queryset = Whatever.objects.all()
        resource_set = 'whatever'
        filtering = {'title': ALL}


class EntryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Entry.objects.all()
        authorization = Authorization()
