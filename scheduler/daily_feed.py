
from datetime import datetime, timedelta
from mongoengine import Q
from model.models import Group,Post, User
from mail.mail import send_email


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
        # send_email(subject, sender, recipients, text_body)
        send_email('Daily feed','socialgroup.co.in',recipients,content)