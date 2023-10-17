from flask import Blueprint, request

from api.airtable_api import ProjectsTable

projects_bp = Blueprint('projects', __name__)

projects_api = ProjectsTable()


@projects_bp.route('/projects')
def show_projects():
    all_projects = projects_api.get_all_projects()
    return all_projects


@projects_bp.route('/projects/<string:project_id>', methods=["GET"])
def show_task_details(project_id):
    task_details = projects_api.get_project_details(project_id)
    return task_details


@projects_bp.route('/projects/<string:task_id>', methods=['PATCH'])
def update_project(task_id):
    data = request.get_json()
    task_details = projects_api.update_project(task_id, **data)
    return task_details


@projects_bp.route('/projects/<string:project_id>', methods=["DELETE"])
def delete_project(project_id):
    task_details = projects_api.delete_project(project_id)
    return task_details
