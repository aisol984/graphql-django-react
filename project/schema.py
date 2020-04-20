import graphene
from graphene_django.types import DjangoObjectType
from project.models import User, Project, Income

class UserType(DjangoObjectType):
    class Meta:
        model = User

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project

class IncomeType(DjangoObjectType):
    class Meta:
        model = Income