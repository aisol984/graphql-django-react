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

class UserInput(graphene.InputObjectType):
    user_name = graphene.String()
    user_birthday = graphene.String()

class ProjectInput(graphene.InputObjectType):
    user_id = graphene.Field(UserInput)
    project_name = graphene.String()
    total_budget = graphene.Int()
    deadline = graphene.String()

class IncomeInput(graphene.InputObjectType):
    project_id = graphene.Field(ProjectInput)
    user_id = graphene.Field(UserInput)
    income = graphene.Int()
    date = graphene.String()

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        user_data = UserInput(required=True)
    
    @staticmethod
    def mutate(root, info, user_data):
        user = User.objects.create(user_name = user_data.user_name,\
                                   user_birthday = user_data.user_birthday)
        return CreateUser(user = user)

class CreateProject(graphene.Mutation):
    project = graphene.Field(ProjectType)

    class Arguments:
        project_data = ProjectInput(required=True)
    
    @staticmethod
    def mutate(root, info, project_data):
        user = User.objects.create(user_name = project_data.user_id.user_name,\
                                   user_birthday = project_data.user_id.user_birthday)
        project = Project.objects.create(user = user,\
                                         project_name = project_data.project_name,\
                                         total_budget = project_data.total_budget,\
                                         dealine = project_data.deadline)
        return CreateProject(project=project)

class CreateIncome(graphene.Mutation):
    income = graphene.Field(IncomeType)

    class Arguments:
        income_data = IncomeInput(required=True)
    
    @staticmethod
    def mutate(root, info, income_data):
        user = User.objects.create(user_name = income_data.user_id.user_name,\
                                   user_birthday = income_data.user_id.user_birthday)
        project = Project.objects.create(user = user,\
                                         project_name = income_data.project_id.project_name, \
                                         total_budget = income_data.project_id.total_budget, \
                                         deadline = income_data.project_id.deadline)
        income = Income.objects.create(project_id = project, \
                                       user_id = user,\
                                       income = income,\
                                       date = date)

class mutations(object):
    create_user = CreateUser.Field()
    create_project = CreateProject.Field()
    create_income = CreateIncome.Field()