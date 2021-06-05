## setup the project
Create a new venv by typing `python -m venv venv` and activate the venv by typing `source venv/bin/activate (linux)` or `source venv/Scripts/activate (Windows)`.<br><br>

Install requirements by typing `pip install -r requirements`. Then `cd src` and create migrations by typing `python manage.py makemigrations` and then `python manage.py migrate`. 

Finally, start the project by typing `python manage.py runserver`.