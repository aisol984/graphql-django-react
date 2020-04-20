import graphene
from graphene_django.types import DjangoObjectType
from projectmanagement.project.models import User, Project, Income

class UserType(DjangoObjectType):
    class Meta:
        model = User

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project

class IncomeType(DjangoObjectType):
    class Meta:
        model = Income

class Query(object):
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    all_incomes = graphene.List(IncomeType)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_all_projects(self, info, **kwargs):
        return Project.objects.all()

    def resolve_all_incomes(self, info, **kwargs):
        return Income.objects.all()