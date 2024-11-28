from .BaseService import BaseService
from ..models import Role
from django.db import connection
from ..utility.DataValidator import DataValidator


class RoleService(BaseService):

    def get_model(self):
        return Role