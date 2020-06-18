from django.contrib import admin
from django.urls import path, include
from apiserver.api import WhateverResource, EntryResource
from tastypie.api import Api

v1_api = Api(api_name="v1")
v1_api.register(WhateverResource())
v1_api.register(EntryResource())

urlpatterns = [
    path('api/', include(v1_api.urls)),
    path('admin/', admin.site.urls),
]
