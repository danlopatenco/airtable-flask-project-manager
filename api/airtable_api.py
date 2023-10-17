import requests

from core.settings import (
    AIRTABLE_TOKEN,
    AIRTABLE_BASE_ID,
    AIRTABLE_PROJECTS_TABLE_NAME,
    AIRTABLE_TASKS_TABLE_NAME
)


class AirtableBase:
    """
    Represents a base class for interacting with Airtable API.

    Attributes:
        api_key (str): The Airtable API key.
        base_id (str): The Airtable base ID.
        headers (dict): The HTTP headers for the API requests.
    """

    def __init__(self):
        """
        Initializes an instance of AirtableBase with the provided API key and base ID.
        """
        self.api_key = AIRTABLE_TOKEN
        self.base_id = AIRTABLE_BASE_ID
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def get_records(self, table_name):
        """
        Retrieve all records from a specified table.

        Args:
            table_name (str): The name of the table to retrieve records from.

        Returns:
            dict: JSON response containing the records.
        """

        url = f'https://api.airtable.com/v0/{self.base_id}/{table_name}'
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_record(self, table_name, record_id):
        """Retrieve a specific record."""

        url = f'https://api.airtable.com/v0/{self.base_id}/{table_name}/{record_id}'
        response = requests.get(url, headers=self.headers)
        return response.json()

    def create_record(self, table_name, **kwargs):
        """Create a new record."""

        data = {"fields": kwargs}
        url = f'https://api.airtable.com/v0/{self.base_id}/{table_name}'
        response = requests.post(url, headers=self.headers, json=data)
        return response.json()

    def update_record(self, table_name, record_id, **kwargs):
        """Update a specific record."""

        data = {"fields": kwargs}
        url = f'https://api.airtable.com/v0/{self.base_id}/{table_name}/{record_id}'
        response = requests.patch(url, headers=self.headers, json=data)
        return response.json()

    def delete_record(self, table_name, record_id):
        """Delete a specific record."""
        url = f'https://api.airtable.com/v0/{self.base_id}/{table_name}/{record_id}'
        response = requests.delete(url, headers=self.headers)
        return response.json()

    # Additional methods for updating and deleting records can be added here


class ProjectsTable(AirtableBase):
    """
    Represents a class for interacting with the projects table in Airtable.

    Inherits from AirtableBase.

    Attributes:
        table_name (str): The name of the projects table.
    """

    def __init__(self):
        """
        Initializes an instance of ProjectsTable with the specified table name.
        """
        super().__init__()
        self.table_name = AIRTABLE_PROJECTS_TABLE_NAME

    def get_all_projects(self):
        """Retrieve all projects."""

        return self.get_records(self.table_name)

    def get_project_details(self, project_id):
        """Retrieve details of a project."""

        return self.get_record(self.table_name, project_id)

    def create_project(self, **data):
        """Create a new project."""

        return self.create_record(self.table_name, **data)

    def update_project(self, task_id, **data):
        """Update a project."""

        return self.update_record(self.table_name, task_id, **data)

    def delete_project(self, project_id):
        """Delete a project."""

        return self.delete_record(self.table_name, project_id)


class TasksTable(AirtableBase):
    """
    Represents a class for interacting with the tasks table in Airtable.

    Inherits from AirtableBase.

    Attributes:
        table_name (str): The name of the tasks table.
    """

    def __init__(self):
        """
        Initializes an instance of TasksTable with the specified table name.
        """
        super().__init__()
        self.table_name = AIRTABLE_TASKS_TABLE_NAME

    def get_all_tasks(self):
        """Retrieve all tasks."""

        return self.get_records(self.table_name)

    def get_task_details(self, task_id):
        """Retrieve details of a task."""

        return self.get_record(self.table_name, task_id)

    def create_task(self, **data):
        """Create a new task."""

        return self.create_record(self.table_name, **data)

    def update_task(self, task_id, **data):
        """Update a task."""

        return self.update_record(self.table_name, task_id, **data)

    def delete_task(self, task_id):
        """Delete a task."""

        return self.delete_record(self.table_name, task_id)
