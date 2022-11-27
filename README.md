## Installation
1) git clone https://github.com/margulanz/project.git
2) cd project
3) pip install pipenv
4) pipenv install
5) pipenv shell
6) python hospital/manage.py migrate
7) python hospital/manage.py createsuperuser` & create a django admin account for you to use locally
8) python hospital/manage.py runserver
## Description
After logged in as admin, you can add Doctors and Patients to database
## API endpoints
- specializations/ -> returns list of specializations
- specializations/{int:id}/doctors/ -> returns list of doctors with specific specialization (id = specialization.id)
- doctors/ -> returns list of doctors
- time-slots/{int:id}/ -> returns time-slots which are not free for specific doctor (id = doctor.id)
- time-slots/ -> can create new time-slot
- requests/ -> create new request
