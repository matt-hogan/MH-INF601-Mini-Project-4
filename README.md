# Mini Project 4  
#### INF601 - Advanced Programming in Python  
#### Matt Hogan  
  
## Description
This is a basic to-do list application built with Django.
## Running the App
1. Clone or download repository  
2. Create and activate a virtual environment  
```
python -m venv .venv  
.\.venv\Scripts\activate.bat
```  
3. Install necessary packages  
```
pip install -r requirements.txt
```
4. Initialize the databases  
```
python manag.epy makemigrations tasks
```
5. Apply the database changes  
```
python manage.py migrate
```
6. Create an admin user  
```
python manage.py createsuperuser
```
7. Run the django app  
```
python manage.py runserver
```
8. Navigate to `http://127.0.0.1:8000/` in a browser