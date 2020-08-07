

from socialgroupmain.datadump.functions import makeuser,makegroup,addusergroup,addpostcomment

"""The data dump can be done by removing the comment tags and running the functions one by one
    The sequence goes like first make users say 15000
    Then make groups say 300. The dump puts maximum 300 users in a group.
    So make sufficient no group ex: for 15000 users make at least 50 groups
    Then run the add user to group. It will put 300 users in each group till users last.
    Then run the add post and comment module. 
    All users will add a comment and a post with auto generated content"""

"""This function is used to make user
    name, password, and email is auto generated 
    just supply the no of users as argument"""
# makeuser(5000)
# makegroup(50)
"""This function makes the group supply the no of group as argument"""


"""This function adds user to the group"""
# addusergroup()

"""This function adds post from each user and they also add a comment for their post """
# addpostcomment()


