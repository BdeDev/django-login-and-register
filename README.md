# About Django Login and Registration

Django Login and Registration is a simple web application with basic user functionalitye using Django.

You can easily login and register through web interface.
- Log in
    - via username & password
    - via email & password
    - via email or username & password
    - with a remember me checkbox (optional)
- Register
- Log out
- Profile activation via email
- Reset password
- Remind a username
- Resend an activation code
- Change password
- Change email
- Change profile


# Prerequisites
 To run this project you must have installed these Packages and dependacies.
	
```
sudo apt-get install python3
sudo apt-get install python3-pip
pip3 install Django==2.1.7
```
	
## Installation

Use the package manager pip to install requirement.txt.
```
pip3 install -r requirement.txt --user
```

# How To Started Project
	
	
Run this command for makemigrations.

```
python3 manage.py makemigrations
```
			
Run this command for migrate 

```
python3 manage.py migrate
```
			
Run this command to create superuser.

```
python3 manage.py createsuperuser
```

Run this command to start app

```
   python3 manage.py runserver
```

