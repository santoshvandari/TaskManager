# Task Scheduler
## Introduction
This is the web based application for task management. It is developed using the technologies like HTML, CSS, JS and BootStrap in frontend and python(django Framework) in backend as well as sqlite database(default) as a database. This may be suitable for the college project.

## Features
The Web app has the following features.
 - A new User can Create the Account.
 - A existing User can login using the credentials. 
 - A logged user can add and remove the task.
 - A logged user can modify the existing task.

## Usages
You System must have the following things to use this project.
 - Installation of `python` and  `pip`

    Python is available for every platform. Download it according to you os. You can download it from [Here.](https://www.python.org/downloads/)


Follow the mentioned procedure to run this project in your local system.
 - Clone or Download the Repository
```bash
    git clone https://github.com/santoshvandari/TaskManager.git 
    cd TaskManager
```
 - Create the Virtual Environment Before installing the requirements. 
 ```Bash
    python3 -m virtualenv venv #For Linux User
    python -m virtualenv venv #For Windows and Mac User

 ```
  - Activate the Virtual Environment
  ```bash
    source venv/bin/activate  #For Linux and Windows User
    venv/Scripts/activate  #For Windows User

     Note: It is not Necessary to Create Virtual Environment but recommanded.
  ``` 
 - Install the Requirements
```bash
    pip install -r requirements.txt
```
 - Run the Server
```bash
    python3 manage.py runserver #FOr Linux User
    python manage.py runserver # For Windows User
```
 - Open the url in Browser
 ```bash
    http://127.0.0.1:8000/
 ```

## Contributing
We welcome contributions! If you'd like to contribute to this project, please check out our [Contribution Guidelines](Contribution.md).

## Code of Conduct
Please review our [Code of Conduct](CodeOfConduct.md) before participating in this project.

## License
This project is licensed under the [License](LICENSE).