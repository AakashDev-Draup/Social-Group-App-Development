## List of APIS

    api.add_resource(SignupApi, '/api/signup')                                              # signup user
    api.add_resource(CreateGroupApi, '/api/group/create')                                   # create group
    api.add_resource(AddUserGroupApi, '/api/group/<groupid>/add/user')                   		# add user to the group
    api.add_resource(PostApi, '/api/group/<groupid>/add/post')                              # add post
    api.add_resource(ReadGroupApi, '/api/group/<groupid>/read')                        			# read posts from group
    api.add_resource(RemoveUserGroupApi, '/api/group/<groupid>/remove/user')                # Remove user from the group
    api.add_resource(CommentApi, '/api/group/<groupid>/post/<postid>/add/comment')          # add comment
    api.add_resource(DeletePostApi, '/api/group/<groupid>/post/<postid>/delete')            # delete post
    api.add_resource(DeleteCommentApi, '/api/group/<groupid>/comment/<commentid>/delete')   # delete comment
    api.add_resource(ChangeRoleApi, '/api/group/<groupid>/changerole')                      # change user role
    api.add_resource(EditCommentApi, '/api/group/<groupid>/comment/<commentid>/edit')  # edit comment
    
    api.add_resource(EditPostApi, '/api/group/<groupid>/post/<postid>/edit')  # Edit the post
    api.add_resource(GetGroupApi, '/api/group/<groupid>')                                   # get the group by id
    api.add_resource(GetPostApi, '/api/group/<groupid>/post/<postid>')                      # get the post by id
    api.add_resource(GetCommentApi, '/api/group/<groupid>/comment/<commentid>')             # get the comment by id
    api.add_resource(GetUserApi, '/api/user')  																						# get user by id
    api.add_resource(EditGroupApi, '/api/group/<groupid>/edit')  													# edit group name or visibility
    api.add_resource(ApprovePostApi, '/api/group/<groupid>/post/<postid>/approve')  			# Approve the post
    api.add_resource(AllCommentsApi, '/api/group/<groupid>/post/<postid>/comments')  			# get all the comments for a post
    api.add_resource(DeleteUserApi, '/api/delete/user')																	# Delete user
    api.add_resource(DeleteGroupApi, '/api/group/<groupid>/delete')											# Delete group

## Description

_Note : Format in which data is supplied through the body of the request is shown with examples below._

### (SignupApi, '/api/signup')

This is the first thing you need to do for accessing the social group app, you have to signup using your name,
a password, and an email id. In the body of the request put the name, password, and email. The response will 
return an user id which you have to use for future use.

For ex : Body<br>
{<br>
"name":"aakash",<br>
"password":"12340",<br>
"email":"blah@gmail.com"<br>
}<br>

_Note : After signup authorisation is needed in all the APIs. Use your username and password in the authorisation
tab before submitting the request._

### (CreateGroupApi, '/api/group/create')

After you signup you can create your group using this api. As you created the group you will be the admin of the
group and you will have the rights to add user and change their roles. The body of the request will contain the
the name of the group, and the visibility. By default the visibility is public.

For ex : Body<br>
{<br>
"name":"Test group",<br>
"visibility":"private"<br>
}<br>

### (AddUserGroupApi, '/api/group/<groupid>/add/user')  

This api is used for adding member to the group. The user adding the member should be an admin. The body of the 
request will contain  a dictionary containing user id of the member being added to the group and his role between 'ADMIN', 'MEMBER', and 'MODERATOR'.

For ex : Body<br>
{<br>
"adduser":{"dfdfasdfdsf":"MEMBER"}<br>
} <br>

### (RemoveUserGroupApi, '/api/group/<groupid>/remove/user')

This api is used to remove user from the group. The body of the request contains user id of the member being removed.

 For ex : Body<br>
{<br>
"deleteuser":"dsfgdfgfhfghfghfg"<br>
} <br>

### (PostApi, '/api/group/<groupid>/post/add')

This API is used to create a post. The body contains content. The user creating the post must be member of the group.

 For ex : Body<br>
{<br>
"content":"my first post"<br>
} <br>

### (CommentApi, '/api/group/<groupid>/post/<postid>/comment/add')

This API is used to create a comment. The body contains the  content. The user creating the comment must be member of the group.

 For ex : Body<br>
{<br>
"content":"my first comment"<br>
}<br>

### (DeletePostApi, '/api/group/<groupid>/post/<postid>/delete')

This Api is used to delete a post. User can delete his post. ADMIN and MODERATOR can delete any post.


### (DeleteCommentApi, '/api/group/<groupid>/comment/<commentid>/delete') 

This Api is used to delete a comment. User can delete his comment. ADMIN and MODERATOR can delete any comment.


### (ReadGroupApi, '/api/group/<groupid>/read')

This Api fetches all the posts in a group. You must be a member of the group.


### (GetGroupApi, '/api/group/<groupid>') 

To get a single group information you use this Api.
                

### (GetPostApi, '/api/group/<groupid>/post/<postid>')   

This Api is used to fetch a particular post. The person accessing must be a member of the group.
         

### (GetCommentApi, '/api/group/<groupid>/comment/<commentid>')

This Api is used to fetch a particular comment. The person accessing must be a member of the group.

### (GetUserApi, '/api/user')

This Api is used to get user with authorization.

### (EditGroupApi, '/api/group/<groupid>/edit')  													

This Api is used to edit group name or visibility. Body requires data whichever you want to edit.

### api.add_resource(ApprovePostApi, '/api/group/<groupid>/post/<postid>/approve')  			

This Api is used to Approve the post by admin.

### api.add_resource(AllCommentsApi, '/api/group/<groupid>/post/<postid>/comments')  			

This Api gets all the comments for a post.

### api.add_resource(DeleteUserApi, '/api/delete/user')																	

This Api is used to delete user from the app.

### api.add_resource(DeleteGroupApi, '/api/group/<groupid>/delete')											

This Api is used to delete group and associated posts and comments.

