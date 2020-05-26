import graphene

import jihakiki.schema

class Query(jihakiki.schema.Query, graphene.ObjectType):
    pass


class Mutation(jihakiki.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)