
from datetime import datetime, timedelta
from mongoengine import Q
from socialgroupmain.model.models import Group,Post, User
from socialgroupmain.mail_module.mail_functions import send_mail


def dailyfeed():
    # time now is given such that its mid night
    time_now = datetime.now()
    lastday = time_now - timedelta(hours=24)
    groups = Group.objects()
    for group in groups:
        posts = Post.objects(Q(groupid=group.id) & Q(date_created__lte=time_now) & Q(date_created__gte=lastday))
        total = len(posts)
        content = '{total} posts were put today'.format(total=total)
        recipients = []
        for userid,access in group.role_dict.items():
            if access == 'ADMIN' or access == 'MODERATOR':
                user = User.objects(id=userid)
                recipients.append(user)
        """remove the comment tag to make the mail function effective"""
        # send_mail(recipients,content)
        # send_mail(recipients,content)
