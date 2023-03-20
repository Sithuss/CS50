#  CS50 Final Project - HOSPITAL

#### Video Demo: https://youtu.be/WHMY2Uvs6xg
#### Description: This web app is for patinet recording.

# How to run:

#### First your teminal execute "export DEFAULT_MAIL_SENDER=your mail address"
#### Then "export MAIL_PASSWORD=your passowrd"
#### And "export MAIL_USERNAME=your mail address"
#### Then execute "flask run"
#### Then execute "flask run".

# About this app

#### You can register as two status. Admin registration and member registration. Admin control member regsition and remove member.
#### And also admin can see registration record for security.
#### Both admin and member can add patient registration form and details.
#### In patient details tab, member cannot see the total cash for hospital privacy.
#### In history, you can see what time and who registered the patient.
#### In account profile all users can change name, passowrd, contact number and email address.
#### Be cautious that this app is not suitable for general public.

## Technologies Used:
- python3
- python3 flask framework
- sqlite3
- html, css, javascript, bootstrap

## Session

#### The web app uses session to confirm that user regiered. Once the uer logins, the credentials are checked with data in the database. After that send OTP token to your mail account. If OTP is correct, login profile is stored in the cookies.

## Database

#### Database store all members, patient registration forms as tables in back-end. Patient_details table uses foreign keys to relate with patient registration form.

## design
#### I use cs50 finance design again as its nav bar is my favorite. In patient details, I have imagine that I could use table form for description. But in reality the table form has too many fields(columns) this is not good lookin for mobile view. So, I desided to use other form form bootstrap framework. Also in details.html page I designed pateint name to put in a show box that is pretty good looking.
#### Account profile page is the lognest html page. I have googled many times to choose the best design suitable for this webb app.

## Possible Improvements
* I Have noticed that in password changing I should send OTP code again for security sake.

## How to launch app
1. copy or down all files in to local computer.
2. install python3.
3. install python3 libraries: Flask, Flask-Mail, datetime, cs50
4. import enviroment variables MAIL_DEFAULT_SENDER=your mail, MAIL_PASSWORD=your mail password, MAIL_USERNAME=your mail
5. flask run
6. copy link appear below and paste it in your browser
7. you are good to go