
from django.urls import path
from ninja_extra import NinjaExtraAPI

from backendNumanis.Numanis.views import router

api = NinjaExtraAPI()

api.add_router('/compression', router, tags=['Numanis'])

