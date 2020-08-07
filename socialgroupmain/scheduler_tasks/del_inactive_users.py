
from datetime import datetime, timedelta
from socialgroupmain.model.models import Group,SaveLogs
from mongoengine import connect


def inactive_users():

    connect("Social-Group")
    # connect("Social-Group-Dump")
    print('Scheduler working')
    present_time = datetime.now()
    groups = Group.objects()
    for group in groups:
        temp_role_dict = {}
        temp_role_dict.update(group.role_dict)
        temp_lactive_dict = {}
        temp_lactive_dict.update(group.lastactive_dict)
        messagelist = []
        for userid,lastactive in group.lastactive_dict.items():
            if lastactive<present_time-timedelta(minutes=1) and group.role_dict[userid] != 'ADMIN':
                message = "{name} got deleted due to inactivity".format(name=userid)
                messagelist.append(message)

                for key in list(group.role_dict):
                    if key == userid:
                        del temp_role_dict[userid]
                        break
                for key in list(group.lastactive_dict):
                    if key == userid:
                        del temp_lactive_dict[userid]
                        break
        group.update(set__lastactive_dict=temp_lactive_dict)
        group.update(set__role_dict=temp_role_dict)
        SaveLogs(groupid=group, message=messagelist).save()

