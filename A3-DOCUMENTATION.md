# Message Forum #

Welcome to use the documentation of the Message Forum Application. "Message Forum" is a program which allows users to post their messages not only in the public pages where all users using this application would see, but send private message to one of the other users in person. The main functionality of this application is to maintain a safe channel of high efficiency for users to transform their messages as well as exchange information.

## Introduction ##

The documentation contains **User's Guide** and **Developer's Reference**. User Guide demonstrates how to use the program for implementing AWS Manager Function. Developer's Reference explains the working principle to help other programmers understanding and upgrading the program easily.

## User Guide ##

### Main Structure of the Application ###

In Message Forum Application, the pages could be divided into 3 different respects:
> login-register-logout-security pages<br>
> personal setting pages<br>
> message transforming pages<br>

In the first aspect, we designed 3 pages providing log-in, register as well as log-out service for users. In the personal setting aspect, we include 3 different pages in order to cater for users' needs for avatar changing, password changing as well as the change of personal memo showing in the user-listing page as well as on the top of their private pages. <br>

The last also the most important part includes 3 different pages: the private page which can show all the messages one could received and also provide the private message sending service; the public page which would show all the messages all the users posted and in the meantime provide the public message sending service; the all-user page listing all the users' names, which could provide great convenience for users who in dire need of sending messages to other users while couldn't recall the receiver's name.

### Access to this web application ###

For assignment requirement as well as the future development, this application is automatically deployed in a serverless form using zappa module. the python based application is stored in one lambda function and is running in API gateway. You could get access to this web application via the following url:
>https://k8n9es02bh.execute-api.us-east-1.amazonaws.com/dev/ <br>


  
### login page (welcome page)###

Open the browser and enter the dynamic URL **https://k8n9es02bh.execute-api.us-east-1.amazonaws.com/dev/** to access the login page. You could login directly if you have possessed one account or click on **Don't have an account?** to redirect to the register page to create a new account.

![Figure1](https://i.imgur.com/Xes4KiA.jpg)
<h6 style="text-align: center;" markdown="1">Login Page</h6>

### Register page ###

In this page you could simply register for your first account. You could simply enter your user name as well as your password, and the system will allocate one default personal tag as well as avatar for you, you could change them later in the **setting** pages. After one successful registration, system will jump back to the **login** page for new account login.

![Figure2](https://i.imgur.com/ww28D6u.jpg)
<h6 style="text-align: center;" markdown="1">Register Page</h6>
![Figure3](https://i.imgur.com/vo71JnG.jpg)
<h6 style="text-align: center;" markdown="1">Fill in the forms in the Register page</h6>

### Private page ###

After logging into one regular Message Forum account, you will first enter into the private page where you could see the messages sent by other people. In this page you could also send private messages to other users who are using this application.<br>

![Figure4](https://i.imgur.com/dsTf6kl.jpg)
<h6 style="text-align: center;" markdown="1">Private Page</h6>

Upon first login, you could find that your avatar is one default image and the top personal information column is filled with the words "This is your private pages **your name**, please enjoy!", these two contents are automatically set by the system, you could always change them later by entering corresponding setting pages. <br>

In the navigation bar on the top of this page, you could find 7 different options, among them all ** Pw Setting**,**Mm Setting** and ** Av Setting ** are 3 different pages apt for the password, personal tag as well as avatar information reset. <br>

Then, ** All Users** will navigate you to one page where all users using this application are shown in list, **Private Page** will redirect you to your private page, ** Public Page** will redirect you to your public page,which we will cover in the latter documentation, and ** Log out ** age will log you out of this application and redirect you into one page which could indicate your that you've been successfully logged out.<br>

Now let's try the private message sending function provided in private page by simply sending one message to ourselves. In the message typing form typing "Hello, Collins!", and in the sender choosing form typing your own personal user name: Collins (If you type in the user name not existed in this application,  the system will flash error message), and then click on **Post it**. After a short while, you could find your own message shown as one block in the ** All Message** form. The picture below well illustrate this message sending process


![Figure5](https://i.imgur.com/xGjuD2M.jpg)
<h6 style="text-align: center;" markdown="1">Send private message in Private page</h6>

### Public Page ###

Now let's explore what's behind the public page. In this page, you're allowed to send messages to all the users who are using this application. As you could see in the picture below, there already existed some of the public messages which are sent by the former users who are using this application: 

![Figure6](https://i.imgur.com/BF8TsnU.jpg)
<h6 style="text-align: center;" markdown="1">All messages in public page</h6>

Now let's send our own public message to this application. In the message typing form typing "Hello World" and just click on ** Post it ** button, after a short while you could just find your message shown in the ** All Message** column.

![Figure7](https://i.imgur.com/dlaX0Wf.jpg)
<h6 style="text-align: center;" markdown="1">post your own public message public page</h6>
![Figure8](https://i.imgur.com/dwfYLme.jpg)
<h6 style="text-align: center;" markdown="1">Your messages in public page</h6>

### All User page###

In this page, you could see all the users using this application. this page will provide convenience to private message sending process when users having troubles finding exact name of one proper user.

![Figure9](https://i.imgur.com/Fs8nVKi.jpg)
<h6 style="text-align: center;" markdown="1">All User page</h6>

In the picture illustrated above, you could find all users listed in the block.

### Private information setting pages###

In this application, there are 3 different pages providing the functionalities of password resetting, personal tag information resetting as well as avatar image resetting. these pages are accessible via clicking button on the top navigation bar.

![Figure10](https://i.imgur.com/cQmTgQY.jpg)
<h6 style="text-align: center;" markdown="1">password setting page</h6>
![Figure11](https://i.imgur.com/nxMjzXQ.jpg)
<h6 style="text-align: center;" markdown="1">personal tag setting page</h6>
![Figure12](https://i.imgur.com/cHVHvkW.jpg)
<h6 style="text-align: center;" markdown="1">avatar image page</h6>

After changing the personal tag and avatar image, you could find the changes in your **Private page** as well as in the **All user** page.

### Logout page###

After clicking on the ** Logging out ** button on the top far-right corner, you would be directly redirect to one log out page indicating that you've been successfully logged out.

![Figure13](https://i.imgur.com/B5UR6Ig.jpg)
<h6 style="text-align: center;" markdown="1">Logout page</h6>


## Deverlopor's Reference ##

### Program development ###

#### Programming environment ####

> Programming language: **Python 3.7** <br>
> Web framework: **Flask 0.11.1** <br>
> Integrated Development Environment: **PyCharm 2018.3.4 x64 bit** <br>
> Database: **RDS-Mysql** <br>
> Server Connector: **cygwin 2.11.2** , **TightVNC 2.8.11** , **FileZilla 3.40.0 x64 bit**<br>
> Browser: **firefox 51.0.1 x64 bit**(server), **google chrome 70.0.3538.110 x64 bit**(developer) <br>

#### Program Structure ####

    Manager_Program                                       # Project directory
    ├ templates                                           # Web page file directory
    │├ Login_Page.html
    │├ Logout_Page.html
    │├ Private_Page.html
    │├ Private_Setting_Page.html
    │├ Private_User_Page.html
    │├ Public_Page.html
    │└ Register_Page.html
    ├ venv                                                # Virtual environment directory
    ├ . idea                                              # Support file directory (flask project)
    ├ __pycache__                                         # Support file directory (flask project)
    ├ app.py                                              # Main Module
    ├ DynamoDB.py                                         # Customized Module (Manipulation with DynamoDB)
    └ S3.py                                               # Customized Module (Manipulation with S3 bucket)


#### Main Program ####

> Open Module: <br>

    boto3 client('Dynamodb')       # Connect to the AWS Dynamodb Nosql Server
    boto3 client('S3')             # Connect to  AWS S3 storage bucket
    jinja2                         # Operator that writes the server's output to the web page
    flask_bootstrap                # Renderer for HTML template

> Customized Module: <br>

    DynamoDB                       # The module define the interfaces for aws DynamoDB operations such as Create a new table,Add items to one table, scan existing table.
    S3                             # The module define the interfaces for aws s3 operations such as copying existing itmes from one bucket as well as uploading new items into one exsiting bucket

    
> Templates: <br>

    Login_Page.html              # Display the login page
    Logout_Page.html             # Display the logout page
    Private_Page.html            # Display the private page
    Private_Setting_Page.html    # Display the setting page
    Private_User_Page.html       # Display the all user page
    Public_Page.html			 # Display the public page
	Register_Page.html			 # Display the register page


#### Open Code ####

> The open code is made public at the Github.<br>

local debug version:<br>
[https://github.com/ChauserMondieu/ECE1779-A3-local](https://github.com/ChauserMondieu/ECE1779-A3-local)<br>
API Gateway deploy version:<br>
[https://github.com/ChauserMondieu/ECE1779-A3-API](https://github.com/ChauserMondieu/ECE1779-A3-API)<br>



### AWS Server development ###

#### Lambda & API Gateway ####

In this assignment, we deployed our web application onto one Lambda function and then public it using AWS API Gateway, all the deployments were accomplished by python Module Zappa.

##### Zappa Deployment Structure #####

In order to make our application suitable for Zappa auto-deployment structure, we change the structure of our application into the following:

    ECE1779_Message_Forum                                 # Project directory
    ├ app                                                 # Python file storage
    │├ __pycache__                                        # Copy of python interpretors
    │├ templates                                          # Web page file directory
    ││├ auto_scaling.html
    ││├ CPU_GRAPH.html
    ││├ EC2.html
    ││├ MAIN.html
    ││└ S3.html
    │├ __init__.py                                        # Start script of python files
    │└ app.py                                             # All scripts of application    
    ├ . idea                                              # Support file directory (flask project)
    ├ venv                                                # Lib documents & virtual environment
    ├ run.py                                              # Initializing document of zappa
    └ zappa_settings.json                                 # Setting document of zappa

In short conclusion, all the program-related script files should be stored in one portfolio, in this case is named **app**. In this particular file all python scripts should be divided into the following 4 main parts:
>data<br>
>server<br>
>backup<br>
>connection<br>

In this case, as we only have the server-related python script (which is named **app.py**), we only need to put our scripts directly under the directory of **/app**   <br>

Next, the content of setting document of zappa, aka the **zappa_setting.json** is listed below:

		{
		    "dev": {
		       "project_name": "ece1779-message-forum",
		       "keep_warm": false,
		       "debug": true,
		       "log_level": "DEBUG",
		       "s3_bucket": "zappadeployss",
		       "app_function": "app.webapp",
		       "http_methods": ["GET","POST"],
		       "parameter_depth": 1,
		       "timeout_seconds": 300,
		       "memory_size": 128,
		       "use_precompiled_packages": true
		    }
		}

 After initializing zappa and create dev under the environment of Zappa, we deployed our application into AWS Lambda and then upload it into AWS API Gateway: 


![Figure21](https://i.imgur.com/n5kG1Kj.jpg)
<h6 style="text-align: center;" markdown="1">Lambda function</h6>
![Figure22](https://i.imgur.com/oeFODa8.jpg)
<h6 style="text-align: center;" markdown="1">Deploy details of function</h6>

As we can see above, we put our application as a whole function in one Lambda function, and this Lambda function invoke the service of DynamoDB, S3 and other AWS service.

![Figure23](https://i.imgur.com/I5guUuW.jpg)
<h6 style="text-align: center;" markdown="1">API Gateway</h6>
![Figure24](https://i.imgur.com/PXGp3zx.jpg)
<h6 style="text-align: center;" markdown="1">Dashboard of API Gateway</h6>

As we can see above, the application did receive some quest and also send out responses due to the calling of server users.

#### Database - DynamoDB ####

In this application, we use DynamoDB for user information storage. DynamoDB is structured based on the Nosql Database concept, and to make the best use out of this Database form, we Set up 4 different tables which are used for:

> **People**: users' personal information: user name, password<br>
> **Private**: users' private page messages<br>
> **Memo**: users' personal tags<br>
> **Public**: public page messages  <br>

As for the inner structure requirement, unlike Mysql Database, there is no specific name for DynamoDB, as mentioned above, we have four different table stored in Dynamo DB:

> table name   : **People**  **Private** **Public** **Memo**<br>

![Figure14](https://i.imgur.com/TJhWCvU.jpg)
<h6 style="text-align: center;" markdown="1">Overview of DynamoDB</h6>

Next, we will show the inner structure of each table in DynamoDB:<br>

In table **People**, we set the main key **user_name**, and the first attribute is password, which is assigned the form "String/S":

![Figure15](https://i.imgur.com/IbbGq2q.jpg) 
<h6 style="text-align: center;" markdown="1">Table structure of People</h6>

In table **Memo**, as it is in table **People**, we set the main key **user_name**, and the first attribute is memo, which will store the personal tags of each user. During the operation, the application will automatically create one default personal tag upon new user creating process under the **user_name** key. 

![Figure16](https://i.imgur.com/FJeojNW.jpg)
<h6 style="text-align: center;" markdown="1">Table structure of Memo</h6>

In table **Private**, we also set the main key **user_name**, while the attributes are stored in string series form (**SS**), which will store both the sender's name as well as the content of the message:

![Figure17](https://i.imgur.com/MvpneUj.jpg)
<h6 style="text-align: center;" markdown="1">Table structure of Private</h6>
![Figure18](https://i.imgur.com/MVogPOk.jpg)
<h6 style="text-align: center;" markdown="1">Inner structure of items of Private</h6>

The last table **Public** show totally different inner structure. in this table ,we store all messages information only in one item, and the main key is **public**:

![Feagure19](https://i.imgur.com/jzNhdEz.jpg)
<h6 style="text-align: center;" markdown="1">Table structure of Public</h6>
![Feagure20](https://i.imgur.com/RqTjTtT.jpg)
<h6 style="text-align: center;" markdown="1">Inner structure of items of Public</h6>

#### S3 ####
In this assignment, we store all the pictures uploaded by users in S3 bucket

We create one bucket under the domain of AWS S3 Server, the information of the existing bucket is shown:

![Figure25](https://i.imgur.com/6js6TSR.jpg)
<h6 style="text-align: center;" markdown="1">Bucket in S3 Service</h6>

In bucket **ece1779avatarss**, we store all the pictures which are set to be the background as well as ornamentation pictures of our web pages as well as avatar pictures uploaded by users. <br>

Bucket **zappadeployss** is designed to store the deployment documentations from zappa.

In the bucket **ece1779avatarss**, stored data are divided into 2 different groups: 
> People </br>
> Public </br> 

In **People** portfolio, we store all the avatar pictures uploaded from users, upon new account creation, we will copy the default avatar image from **Public** portfolio where the default avatar image is stored:

![Figure26](https://i.imgur.com/TitNsYq.jpg)
<h6 style="text-align: center;" markdown="1">Storing data in People portfolio</h6>

And as we have mentioned before, the **Public** portfolio stores all the background as well as ornamentation images of the web pages:

![Figure27](https://i.imgur.com/SUDclAF.jpg)
<h6 style="text-align: center;" markdown="1">Storing data in Public portfolio</h6>


<hr>@ Copyright 2019, Zhonghao Li & Botao Liu & Qiuchen Wang. Created using Markdownpad 2
