Scenario 1: Valid Date of Birth
As a user of FindMate, I am able to sign up and log in when I am 16 years old.

Step#	Action	Expected outcome	OK/NOK	URL	Link to issue
1	Go to login page FindMate	Login page appears	OK	https://findmate.masterschool.com/	
2	Click on Sign up	You are directed to the sign up page	OK	/auth	
3a	Fill in RandomUsername				
3b	Fill 18-08-2008 as Date of Birth				
3c	Write 'This is my Bio'				
3d	Write karin@faculty.masterschool.com as e-mail address				
3e	Password is 'RandomPassword1'				
4	Click sign up	You are directed to the login page. The e-mail and password are filled automatically	OK		
5	Click on log in	You are successfully logged in	OK		
image image image image

Scenario 2: Invalid Date of Birth
As a user of FindMate, I am not able to sign up when I register with an invalid Date of Birth.

Step#	Action	Expected outcome	OK/NOK	URL	Link to issue
1	Go to login page FindMate	Login page appears	OK	https://findmate.masterschool.com/	
2	Click on Sign up	You are directed to the sign up page	OK	/auth	
3a	Fill in 'InputValidationTest' as username				
3b	Fill 19-08-1820 as Date of Birth				
3c	Write 'This is my Bio'				
3d	Write karin@faculty.masterschool.com as e-mail address				
3e	Password is 'RandomPassword1'				
4	Click sign up	You ca
