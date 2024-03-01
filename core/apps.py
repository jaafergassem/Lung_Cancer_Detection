from django.apps import AppConfig
from django.conf import settings
from tensorflow import keras

import os

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'


