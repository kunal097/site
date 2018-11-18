from django.contrib import admin

from .models import (
    DeletedMessage, DocumentationLink,
    Member, MessageDeletionContext,
    OffTopicChannelName, Role,
    SnakeFact, SnakeIdiom,
    SnakeName, SpecialSnake,
    Tag
)


admin.site.register(DeletedMessage)
admin.site.register(DocumentationLink)
admin.site.register(Member)
admin.site.register(MessageDeletionContext)
admin.site.register(OffTopicChannelName)
admin.site.register(Role)
admin.site.register(SnakeFact)
admin.site.register(SnakeIdiom)
admin.site.register(SnakeName)
admin.site.register(SpecialSnake)
admin.site.register(Tag)