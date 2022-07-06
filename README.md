# Bike-Rental-Application
A Bike Rental Application using Python and flask integrations

The environment configuration involved in this webpage application includes 
-python3 IDE like Spyder
-Mysql Workbench 8.0 CE, 
-browsers that support html language

Content：
1.Database_sql folder：
Contains all the database scripts, which can be used to execute to obtain the local database, 
scripts also has some dummy data we used for testing
2.static folder：
Contains some supporting resources needed by web pages, 
including pictures, css files, and java script files that we used to perform data visualization
3.templates folder:
Contains all the html we used for the GUI,
4.main.py:
The main file of the application, all python codes are concentrated in this file,
running this file will directly start the application


Step to set up：
1.Download the whole application and keep the folder structure
2.Run the 'trycycle_qa.sql' scripts in Database_sql folder on your own Mysql Workbench,
This will create a database named trycycle_qa and all the necessary tables used to store all the data involved in the application
Note that after generating the database, you need to change the 'connectDB()' method in the main.py code to connect to the local database
3.Open the main.py file in any python IDE,  recommended to use spyder， run this file directly.
4.If the operation is successful, you will see Running on /ip/ in the last line,where /ip/ will be your current local ip address, copy this IP address to the browser,
if the login interface appears, it proves that this application has been successfully run on your computer.
