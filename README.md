# 📋 Django Task Manager Project

This Django Task Manager Project is a simple yet functional web application designed for task management. It allows users to add, edit, and delete tasks, each with a title and description. This project is an excellent starting point for those looking to understand CRUD (Create, Read, Update, Delete) operations in Django.

## Features

- **Adding Tasks**: Users can add new tasks with a title and description. Each task is displayed on the homepage in a list format.
- **Editing Tasks**: Users have the ability to edit the title and description of existing tasks.
- **Deleting Tasks**: Users can delete tasks, which are then removed from the list on the homepage.

## Technologies and Libraries  
![Alt text for Logo1](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Alt text for Logo1](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Alt text for Logo1](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Alt text for Logo1](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
- **Django Forms**: Utilized for creating forms for task addition and editing.
- **Jinja**: The template engine for rendering the HTML pages with dynamic data.
## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

- Python (3.x)
- Django
### Installation

1. Clone this repository to your local machine:
```bash
git clone git@github.com:Talantino/ToDO-project.git
```
2. Change directory to the project folder:
```bash
cd ToDo-project
```
4. Install the required dependencies:
```bash
pip install -r requirements.txt
```

6. Run the migrations to create the database schema:
```bash
python manage.py migrate
```

7. Start the development server:
```bash
python manage.py runserver
```
### Usage

After starting the server, navigate to `http://127.0.0.1:8000/` in your web browser to view the application. From there, you can add, edit, and delete tasks as needed.

## Contributing

🤗 Contributions to improve the project are welcome. Feel free to fork the repository and and submit pull requests.
