# Spy Cat Agency Management System

This CRUD application was developed for the Spy Cat Agency (SCA) to streamline their operational processes. The system allows managing spy cats, their missions, and assigned targets effectively through a RESTful API. Key features include:

 - **Cats Management**: Add and view spy cats, ensuring only available agents are assigned to missions.
 - **Missions Management**: Create and assign missions to cats, each with 1-3 targets. Cats can only have one active mission at a time.
 - **Target Tracking**: Log notes for targets during missions. Once marked as complete, notes are frozen, ensuring data integrity.
 - **Mission Completion Workflow**: Automatically marks missions as completed once all associated targets are resolved.
 - This application demonstrates expertise in designing **RESTful APIs**, interacting with **SQL-like** databases, and integrating **third-party services** within a constrained timeline.

# Installation
## With docker
- **Clone the repository**
```bash
git clone https://github.com/BileichukIvan/spy_cat_agency.git
```
- **Set up .env file** 
You have to create .env using .env.sample. like example
- **Build docker-compose container**
```bash
docker-compose build
```
- **Run docker compose**
```bash
docker-compose up
```

## Without docker
- **Clone the repository**
```bash
git clone https://github.com/BileichukIvan/spy_cat_agency.git
cd spy_cat_agency
```
- **Set Up the Virtual Environment**\
Create and activate a Python virtual environment to isolate project dependencies:

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```
**On Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```
  
- **Install Dependencies**\
Once your virtual environment is active, install the required dependencies:
```bash
pip install -r requirements.txt
```
Set Up Environment Variables
Create a .env file in the root directory of the project to store sensitive information, such as API keys, database credentials, and other settings.

Here is an example .env file:
```
# Database settings
POSTGRES_PASSWORD=*****
POSTGRES_USER=*********
POSTGRES_DB=********
POSTGRES_HOST=*******
POSTGRES_PORT=********
PGDATA=*******
```

# Secret keys for Django
```
SECRET_KEY=*****
```
- **Run Server**
```bash
python manage.py runserver
```

Project includes Postman collection for better understanding of endpoints in **Spy Cats API.postman_collection.json** file.