from django.contrib import admin
from logins.models import UserProfile, Profiler, InstagramProfile, TwitterProfile, MeetupToken, GithubProfile, LinkedinProfile, TumblrProfile

# Register your models here.
class TwitterProfileAdmin(admin.ModelAdmin):
	list_display = ('user','twitter_user')

admin.site.register(UserProfile)
admin.site.register(Profiler)
admin.site.register(InstagramProfile)
admin.site.register(TwitterProfile, TwitterProfileAdmin)
admin.site.register(GithubProfile)
admin.site.register(MeetupToken)
admin.site.register(LinkedinProfile)
admin.site.register(TumblrProfile)
