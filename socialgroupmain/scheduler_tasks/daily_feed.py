
from datetime import datetime, timedelta
from mongoengine import Q
from redis import Redis
from rq import Queue

from socialgroupmain.model.models import Group,Post, User
from socialgroupmain.mail_module.mail_functions import send_mail
from mongoengine import connect

sch_queue = Queue('test',connection=Redis())


def dailyfeed():
    # time now is given such that its mid night
    connect("Social-Group")
    print("working")

    time_now = datetime.now()
    lastday = time_now - timedelta(hours=24)
    groups = Group.objects()
    for group in groups:
        posts = Post.objects(Q(groupid=group.id) & Q(date_created__lte=time_now) & Q(date_created__gte=lastday))
        if posts:
            total = len(posts)
            content = '{total} posts were put within 24 hrs'.format(total=total)
            recipients = []
            for userid, access in group.role_dict.items():
                if access == 'ADMIN' or access == 'MODERATOR':
                    user = User.objects.get(id=userid)
                    recipients.append(user.email)

            sch_queue.enqueue(send_mail, recipients, content)




