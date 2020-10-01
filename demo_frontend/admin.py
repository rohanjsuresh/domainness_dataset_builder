from django.contrib import admin
from .models import Keywords
from .models import Keywords_Classified
from .models import Arxiv_Titles_In_Circulation
from .models import Arxiv_Titles_Classified
from .models import User_Extended
from .models import Arxiv_Titles_Skipped
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from keyword_relation_builder.models import Keywords_in_Circulation as keyword_relation_builder_Keywords_in_Circulations
from keyword_relation_builder.models import Keyword_Pairs as keyword_relation_builder_Keyword_Pairs
from keyword_relation_builder.models import Keywords_Classified as keyword_relation_builder_Keywords_Classified
from keyword_relation_builder.models import Keywords_Skipped as keyword_relation_builder_Keywords_Skipped

from .models import UserExtension

admin.site.register(Keywords)
admin.site.register(Keywords_Classified)
admin.site.register(Arxiv_Titles_In_Circulation)
admin.site.register(Arxiv_Titles_Classified)
admin.site.register(User_Extended)
admin.site.register(Arxiv_Titles_Skipped)

admin.site.register(keyword_relation_builder_Keywords_in_Circulations)
admin.site.register(keyword_relation_builder_Keyword_Pairs)
admin.site.register(keyword_relation_builder_Keywords_Classified)
admin.site.register(keyword_relation_builder_Keywords_Skipped)


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserExtentionInline(admin.StackedInline):
    model = UserExtension
    can_delete = False
    verbose_name_plural = 'user_extension'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserExtentionInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)