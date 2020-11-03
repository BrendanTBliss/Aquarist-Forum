from django.apps import AppConfig
from django.conf import settings #delete this line
from django.db.models.signals import post_migrate #delete this line
from django.utils.translation import gettext_noop as _ #delete this line


class MainAppConfig(AppConfig):
    name = 'main_app'


#DELETE EVERYTHING BELOW THIS LINE

notifier_app_label = getattr(settings, 'POSTMAN_NOTIFIER_APP', 'pinax_notifications')
if notifier_app_label:
    def create_notice_types(*args, **kwargs):
        create = apps.get_model(notifier_app_label, 'NoticeType').create
        create("postman_rejection", _("Message Rejected"), _("Your message has been rejected"))
        create("postman_message", _("Message Received"), _("You have received a message"))
        create("postman_reply", _("Reply Received"), _("You have received a reply"))

class PostmanConfig(AppConfig):
    name = 'postman'

    def ready(self):
        from .models import setup
        setup()

        if notifier_app_label:
            try:
                notifier_app_config = apps.get_app_config(notifier_app_label)
            except LookupError:  # means the app is not in INSTALLED_APPS, which is valid
                pass
            else:
                post_migrate.connect(create_notice_types, sender=notifier_app_config)
