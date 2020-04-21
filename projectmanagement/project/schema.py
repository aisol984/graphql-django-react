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

    user = graphene.Field(UserType,\
                          id = graphene.Int(),\
                          user_name = graphene.String())
    
    project = graphene.Field(ProjectType,\
                             id = graphene.Int(),\
                             project_name = graphene.String())

    income = graphene.Field(IncomeType,\
                             id = graphene.Int(),\
                             income = graphene.Int())

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_all_projects(self, info, **kwargs):
        return Project.objects.all()

    def resolve_all_incomes(self, info, **kwargs):
        return Income.objects.all()

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        user_name = kwargs.get('user_name')
        if id is not None:
            return User.objects.get(pk=id)
        if user_name is not None:
            return User.objects.get(user_name=user_name)
        return None

    def resolve_project(self, info, **kwargs):
        id = kwargs.get('id')
        project_name = kwargs.get('project_name')
        if id is not None:
            return Project.objects.get(pk=id)
        if project_name is not None:
            return Project.objects.get(project_name=project_name)
        return None

    def resolve_income(self, info, **kwargs):
        id = kwargs.get('id')
        income = kwargs.get('income')
        if id is not None:
            return Project.objects.get(pk=id)
        if income is not None:
            return Project.objects.get(income=income)
        return None