AWS Chalice Tutorial

Repo Layout
===========

chalicelib

Release

tests


Building the project
=================

Create Virtual environment::
   
    $ python3 -m venv venv37

Activate the vitual environment::
    
	$ . venv37/bin/activate
	
Go to project directory::

	$ cd {PATH}/vfc-lambda/
	
Install Chalice::

	$ python3 -m pip install chalice

Install requirements::

    $ pip install -r requirements.txt


To Run local::

    $ chalice local
 
To Run test::
	
	$ py.test tests/
	
	$ pytest --log-cli-level=DEBUG
	 
 
To deploy it in AWS lambda::

    $ chalice deploy
    
    
To get the AWS URL::
    
    $ chalice url
    
    
To generate HTML::

    $ chalice generate-sdk --sdk-type javascript ../{output directory}
    

Commit and Push to Git
======================

Push it to bitbucket::

	$ git push
	
Push it to AWS CodeCommit::

	$ git push codecommit master
	