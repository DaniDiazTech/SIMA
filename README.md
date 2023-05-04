# Habit tracker in Django
Habit tracker app with Calendar made with Django.

Home:
![Home](screenshots/home.png)

Gym habit:
![Gym](screenshots/gym.png)

Create habit:
![Create](screenshots/create-habit.png)

To clone and run the project:
```bash
git clone git@github.com:DaniDiazTech/Habit-tracker.git
cd Habit-tracker
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

To run the project:

```bash
django-admin startproject --template=https://github.com/momentumlearn/django-project-template/archive/main.zip --name=Pipfile project .
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
