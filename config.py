from dynaconf import Dynaconf
from mongoengine import connect

settings = Dynaconf(envvar_prefix="DYNACONF",settings_files=['settings.yaml'])


