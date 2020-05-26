import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from .models import SentMessages, ReceivedMessages

class SentMessagesType(DjangoObjectType):
    class Meta:
        model = SentMessages


class ReceivedMessagesType(DjangoObjectType):
    class Meta:
        model = ReceivedMessages


# Query Received SMS received from Gateway (Stored in ReceivedMessages Model)
class Query(graphene.ObjectType):
    r_messages = graphene.List(ReceivedMessagesType)

    def resolve_r_messages(self, info, **kwargs):
        return ReceivedMessages.objects.all()


# Query Sent SMS sent from Django (Stored in SentMessages Model)
class Query(graphene.ObjectType):
    s_messages = graphene.List(SentMessagesType)

    def resolve_s_messages(self, info, **kwargs):
        return SentMessages.objects.all()


# Send SMS (All Messages that are sent from Django to be stored at SentMessages Model)
class SendMessage(graphene.Mutation):
    id = graphene.Int()
    sender = graphene.String()
    recipient = graphene.String()
    message = graphene.String()
    datetime = graphene.String()

    class Arguments:
        sender = graphene.String()
        recipient = graphene.String()
        message = graphene.String()

    def mutate(self, info, sender, recipient, message):
        s_msg = SentMessages(sender=sender, recipient=recipient, message=message)
        s_msg.save()

        return SendMessage(
            id=s_msg.id,
            sender=s_msg.sender,
            recipient=s_msg.recipient,
            message=s_msg.message,
            datetime=s_msg.datetime,
        )


# Received SMS (All Messages that are received from Gateway to be stored at ReceivedMessages Model)
class ReceiveMessage(graphene.Mutation):
    id = graphene.Int()
    sender = graphene.String()
    recipient = graphene.String()
    message = graphene.String()
    datetime = graphene.String()

    class Arguments:
        sender = graphene.String()
        recipient = graphene.String()
        message = graphene.String()

    def mutate(self, info, sender, recipient, message):
        r_msg = ReceivedMessages(sender=sender, recipient=recipient, message=message)
        r_msg.save()

        return ReceiveMessage(
            id=r_msg.id,
            sender=r_msg.sender,
            recipient=r_msg.recipient,
            message=r_msg.message,
            datetime=r_msg.datetime,
        )


class Mutation(graphene.ObjectType):
    send_message = SendMessage.Field()
    receive_message = ReceiveMessage.Field()