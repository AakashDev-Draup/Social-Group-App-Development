#Tech Stack: Python, Flask, Mongo, and RQ


#Work Completed:

	1. Formulation of program architecture. 	(Wednesday)
	2. Formulation of document schema.		(Wednesday)
	3. Implementing the document schema.		(Wednesday-Thursday)
	4. Setting up app configuration and URL for API requests.					(Thursday)
	5. Setting up of POST and PUT requests using REST for the group, post, user, and comment view.	(Thursday)
	6. Adding authentication and authorization to the requests.					(Thursday-Friday)


#Work Ahead:

	1. Updating the corrections discussed at Friday's meeting.				(Friday)
	2. Updating document schema to insert create and update time variables. 		(Friday)
	3. Setting up remaining requests such as DELETE and GET for post and comment view.	(Monday)	
	4. Setting up the Queue tasks.					(Monday)
	5. Setting up the Queue tasks with mail setup.			(Tuesday)	
	6. Test the application with a data dump.			(Wednesday) 






#The application architecture


	SocialGroup		...The main app folder

		run.py		...gets the application running
		app.py		...social group application
		/Exception
			exceptions.py		...file containing the error response
		/templates			...contains the templates for response
		/model
			__init__.py
			models.py		...use data through python objects 
		/config
			__init__.py
			config.py 		...this config file makes connection to the database
		/view
			__init__.py
			mail.py			
			comment.py		...files containing user services
			post.py
			etc

		/urls
			url.py			...assigning the routes
		/auth
			auth.py			...assigning authorisation
		
		/taskqueue			...Queued tasks
			feed.py			...functions handles the daily feed for
			inactive.py		...delete the inactive members
			notify.py		...daily notification for posts
		/datadump
			__init__.py
			dump.py




#Mongodb schema

	*Entities:
	    * Permission
		* ID 
		* Name

	    * Role
		* ID
		* NAME
		* Permission[]
	    * User
		* ID
		* NAME
		* email
		* groups =[]
		* posts = []
		* comments = []
	    * GROUP
		* ID
		* Name
		* Users {} with id and role
		* Visibilty = PUBLIC | PRIVATE
	    * POST
		* ID
		* UserId
		* GroupId
		* approval boolean
		* content
	    
	    * Comment
		* Id
		* PostId
		* userId
		* content
	


#List of APIS

1. api.add_resource(roleapi, '/api/role/<id>')  # create role and assign permission, id is special key here
2. api.add_resource(Userapi, '/api/User')                      # create user
3. api.add_resource(Groupapi, '/api/<id>/Group')               # create group with user id
4. api.add_resource(addtogroupapi, '/api/addtogroup/<id>')       # add user to the group
5. api.add_resource(removegroupapi, '/api/removefromgroup/<id>')   # Remove user from the group
6. api.add_resource(postapi, '/api/Group/<id>/post')               # add post
7. api.add_resource(commentapi, '/api/<gid>/<pid>/comment')        # add comment





