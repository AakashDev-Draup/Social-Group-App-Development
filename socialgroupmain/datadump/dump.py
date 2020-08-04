
from mongoengine import connect
connect("Social-Group")

from socialgroupmain.datadump.functions import makeuser,makegroup,addusergroup,addpostcomment

"""The data dump can be done by removing the comment tags and running the functions one by one
    select users and group such that users % groups == 0
    The sequence goes like first make users say 15000
    Then make groups say 300
    Then run the add user to group it will equally distribute all the users to group say 15000/300 = 50 users in each group
    Then run the add post and comment module. All user i.e. 15000 users in total will put one post
     and also add a comment with auto generated content"""

"""This function is used to make user
    name, password, and email is auto generated 
    just supply the no of users as argument"""
# makeuser(15000)

"""This function makes the group supply the no of group as argument"""
# makegroup(300)

"""This function adds user to the group by distributing the users equally in all groups"""
# addusergroup()

"""This function adds post from each user and they also add a comment for their post """
# addpostcomment()
