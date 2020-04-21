import graphene
from projectmanagement.project import schema

class Query(schema.Query, graphene.ObjectType):
    pass

class Mutation(schema.mutations, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)