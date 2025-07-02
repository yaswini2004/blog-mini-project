# Flask Blogging App

![blog-banner](https://img.shields.io/badge/Flask-Blog-blue)

This project is a basic blogging platform built using the Flask web framework. It allows users to register, log in, create, view, and manage blog posts. The project is ideal for learning Flask with SQLAlchemy, Flask-WTF, and templating using Jinja2.

## Project Live Link

🚧 *This project is currently not deployed. You can run it locally by following the instructions below.*

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Running the Application](#running-the-application)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

This Flask Blogging App allows users to create an account, log in, and write blog posts. It uses Flask-WTF for form handling, SQLAlchemy for database management, and follows MVC structure for better modularity.

## Features

- User registration and login functionality
- Secure password storage with hashing
- Create, view, and delete blog posts
- Form validation using Flask-WTF
- Clean and responsive HTML templates

## Technologies Used

- Python
- Flask
- Flask-WTF
- Flask-SQLAlchemy
- Jinja2 (Templating)
- HTML & CSS

## Getting Started

### Prerequisites

Ensure you have Python 3.7+ installed.

## Running the Application

### 1. Clone the repository

 https://github.com/yaswini2004/blog-mini-project
 ### 2. Navigate to the project directory
 ```bash
 cd blog-mini-project
```
  ### 3. Create and activate a virtual environment
```bash
  python -m venv venv
source venv/bin/activate        # On macOS/Linux
venv\Scripts\activate           # On Windows
```
  ### 4. Install dependencies
  ```bash
  pip install -r requirements.txt
```
  ### 5. Set environment variables (for development mode)
  ```bash
  set FLASK_APP=run.py            # On Windows
export FLASK_APP=run.py         # On macOS/Linux
```
### 6. Initialize the database (if using Flask-Migrate)
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
### 7. Run the development server
```bash
flask run
```
### 8. Run the development server
```bash
http://127.0.0.1:5000/
```
## Usage
- Register a new user.
- Log in using your credentials.
- Start creating blog posts.
- Log out or delete posts as needed.
## Contributing
Contributions are welcome! Please feel free to fork the repo and submit a pull request.
### 1. Fork the repository.
### 2. Create a feature branch
```bash
git checkout -b feature/YourFeature
```
### 3. Commit your changes
```bash
git commit -m "Add Your Feature"
```
### 4. Push to the branch
```bash
git push origin feature/YourFeature
```
### 5. Open a pull request.




 
  





  







