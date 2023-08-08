# ExchangeLogisticsApp
This is an app for a logistics company with built in freight exchange. (including tests for both SSR and API endpoints)

Stack used:
 - python
 - django - server side rendering
 - django rest framework
 - bootstrap
 
 This project has both - server side rendering and APIs.
 All endpoints are visible in the swagger url -- - http://127.0.0.1:8000/swagger-ui/
 
 
 
 In this app we have an initial part where the information about the logistics company is displayed - Services offered, Locations, About.
 I have put some exemplary text in the templates in order for the app to start without creating models.
 There are four models for the basic data regarding the company which are displayed in the initial part of the app.
 As soon as a model is created the examplary text and images disappear and the created model's data is displayed on the page.
 Only users with staff privileges have permisions to access the 'Settings' feature which allows them to make CRUD opeations to these models.
 Using the admin page we can create a staff group and user with staff permissions or grant such permissions to an existing user.
 When a staff user logs in, a button "Settings" is displayed on the main navigation. Using this button the user can access the 'Settings' feature.
 
 The second feature of the app is a freight exchange where registered users can publish their loads or free trucks.
 A user can sign up with username and password. After that a blank profile is created and the user should fill the neccessary data for his profile.
 After that he can publish freight or truck offers on the market. The user can search for siutable offers on the market and see the offer's details by clicking on it.
 Every offer includes information about the company that had posted it and also a link to this company's profile, where the user can see all actual offers of this particular company.
 
 # Run the project
 
 I. Using Docker image:
 
 1. Run the docker image with the following command:
 - docker run --name logistics-app  -d -p 8000:8000 vasilmg/logistics-app:latest
 
 2. Open your browser and type - http://127.0.0.1:8000/ or http://localhost:8000/
 
 II. Clone the repository from GitHub
 
 1. Clone the repository

 2. Open it with your preferred IDE and create a virtual environment

   2.1 Windows:
 
    Create virtual environment:
    - python -m venv ./venv

    Activate the environment:
     - venv/Scripts/activate

  2.2 Linux:
 
    Create virtual environment:
    - python3 -m venv ./venv

    Activate the environment:
    - source ./venv/bin/activate 
   <br/>
   <br/>

3. Install all dependencies
  - pip install -r requirements.txt
  
4. Make the migrations
  - python manage.py makemigrations
  - python manage.py migrate
 
5. Run the project
 - python manage.py runserver
 
6. Finally open the project in your browser - http://127.0.0.1:8000/ or http://localhost:8000/
 

 - If you wish, you can create a superuser with the command  -> python manage.py createsuperuser
 - After that through the admin page (http://127.0.0.1:8000/admin/) you can create a staff user/group so that you can access the 'Settings' feature.

 
 I have used PostgresSQL but I have left both Postgres and SQLite settings in the settings.py file. So feel free to use the DB you prefer.
 
  - Below you can find some photos:
 
![front page](https://github.com/VasilMG/Django-ExchangeLogisticsApp/blob/main/Screenshots/Screenshot%202023-07-05%20003045.png)

![front page](https://github.com/VasilMG/Django-ExchangeLogisticsApp/blob/main/Screenshots/Screenshot%202023-07-05%20003100.png)

![front page](https://github.com/VasilMG/Django-ExchangeLogisticsApp/blob/main/Screenshots/Screenshot%202023-07-05%20003114.png)

![front page](https://github.com/VasilMG/Django-ExchangeLogisticsApp/blob/main/Screenshots/Screenshot%202023-07-05%20000604.png)

![front page](https://github.com/VasilMG/Django-ExchangeLogisticsApp/blob/main/Screenshots/Screenshot%202023-07-05%20001622.png)

![front page](https://github.com/VasilMG/Django-ExchangeLogisticsApp/blob/main/Screenshots/Screenshot%202023-03-11%20232327.png)

