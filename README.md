
### Application Description
The Airtable Project Manager is a Flask-based web application designed for efficient project and task management. It interfaces with the Airtable API to provide seamless integration with your project data.

The application comprises two main components: Projects and Tasks, allowing users to create, update, and delete projects and tasks as needed. Each project can be associated with multiple tasks, providing a comprehensive view of project progress

Before running the application, you need to set up your environment variables. Copy the content of the ***.env.example*** file and create a new file named ***.env*** . Fill in the required values.

1. Clone the repository
```
git clone https://github.com/danlopatenco/airtable-flask-project-manager.git
```

2. Navigate to the project directory:
```
cd airtable-flask-project-manager
```

3. Build and run the Docker container:

```
docker-compose up --build
```

4. Access the application at http://localhost:5000.


### Routes

#### Projects

- `GET /projects`: Get all projects.
- `GET /projects/<string:project_id>`: Get details of a specific project.
- `PATCH /projects/<string:task_id>`: Update project details.
- `DELETE /projects/<string:project_id>`: Delete a project.

#### Tasks

- `GET /tasks`: Get all tasks.
- `GET /tasks/<string:task_id>`: Get details of a specific task.
- `POST /create_task`: Create a new task.
- `PATCH /tasks/<string:task_id>`: Update task details.
- `DELETE /tasks/<string:task_id>`: Delete a task.


Sample Project Table
```
{
  "Name": "Project 5",
  "Status": "Todo",
  "Tasks": ["receARQCS57s3C7yG"],
  "Notes": "Note update again",
  "createdTime": "2023-10-16T18:50:35.000Z",
  "id": "rec8dBvFEy51swiWq"
}

```


Sample Task Table
```
{
  "Name": "tt4556",
  "Status": "Done",
  "Priority": "Low",
  "Start date": "2023-10-14",
  "Deadline": "2023-10-18",
  "createdTime": "2023-10-17T17:51:48.000Z",
  "id": "recsjRf9pxmWxSH1g"
}
```



## License
This project is licensed under the MIT License.
