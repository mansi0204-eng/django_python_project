from .BaseService import BaseService
from ..models import User
from django.db import connection
from ..utility.DataValidator import DataValidator


class UserService(BaseService):

    def authenticate(self, params):
        q = self.get_model().objects.filter()
        loginId = params.get("loginId", None)
        if (DataValidator.isNotNull(loginId)):
            q = q.filter(loginId=loginId)
        password = params.get("password", None)
        if (DataValidator.isNotNull(password)):
            q = q.filter(password=password)
        if (q.count() == 1):
            return q[0]
        else:
            return None

    def get_model(self):
        return User
