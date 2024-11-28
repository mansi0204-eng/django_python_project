from django.shortcuts import render
from ..forms import RoleForm
from .BaseCtl import BaseCtl
from ..models import Role
from ..service.RoleService import RoleService
from ..utility.DataValidator import DataValidator


class RoleCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['name'] = requestForm['name']
        self.form['description'] = requestForm['description']

    def form_to_model(self, obj):
        pk = int(self.form['id'])
        if (pk > 0):
            obj.id = pk
        obj.name = self.form['name']
        obj.description = self.form['description']
        return obj

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']
        if (DataValidator.isNull(self.form['name'])):
            inputError['name'] = "Name can not be null"
            self.form['error'] = True
        if (DataValidator.isNull(self.form['description'])):
            inputError['description'] = "Description can not be null"
            self.form['error'] = True
        return self.form['error']

    def model_to_form(self, obj):
        if (obj == None):
            return
        self.form['id'] = obj.id
        self.form['name'] = obj.name
        self.form['description'] = obj.description

    def display(self, request, params={}):
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def submit(self, request, params={}):
        r = self.form_to_model(Role())
        self.get_service().save(r)
        res = render(request, self.get_template(), {'form': self.form})
        return res

    def get_template(self):
        return "Role.html"

    def get_service(self):
        return RoleService()
