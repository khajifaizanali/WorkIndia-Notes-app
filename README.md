# WorkIndia-Notes-app
## Requirements:
1.	Flask
2.	Flask_mysqldb
3.	cryptography.fernet (For encryption and decryption of Notes)
4.	hashlib
### User account registration:
![app_user](https://user-images.githubusercontent.com/39943248/88019037-7f2c9980-cb46-11ea-9aaa-690ff8238b3a.PNG)
### User account login:
![app_auth](https://user-images.githubusercontent.com/39943248/88018853-28bf5b00-cb46-11ea-90ab-819033afc6c8.PNG)
### Save A notes
![app_save notes](https://user-images.githubusercontent.com/39943248/88019032-7b007c00-cb46-11ea-8404-c7fef5afe24f.PNG)
### List a saved notes:
![app_list_notes](https://user-images.githubusercontent.com/39943248/88018984-6a500600-cb46-11ea-8380-eb15fd14f112.PNG)

## database
### Tables in database:
![tables](https://user-images.githubusercontent.com/39943248/88019139-b8650980-cb46-11ea-81d6-03f4cd1e4dd0.PNG)
### Users Table:
Id is primary key in users table
![user_id](https://user-images.githubusercontent.com/39943248/88019143-ba2ecd00-cb46-11ea-928c-ba34ca321216.PNG)
### Notes Table:
User id column in the table is foreign key referring to primary key id in users
![Notes](https://user-images.githubusercontent.com/39943248/88019132-b69b4600-cb46-11ea-8b76-fc9a2d7b13e1.PNG)

