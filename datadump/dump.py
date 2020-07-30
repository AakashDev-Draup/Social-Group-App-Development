
from mongoengine import connect
connect("Social-Group")

from datadump.functions import makeuser,makegroup,addusergroup,addpost

# makeuser(9700)
# makegroup(300)
# addusergroup()
# addpost()
# addcomment()