from flask import Blueprint, request
from api.airtable_api import TasksTable

tasks_bp = Blueprint('tasks', __name__)


tasks_table = TasksTable()


@tasks_bp.route('/tasks', methods=["GET"])
def show_tasks():
    tasks = tasks_table.get_all_tasks()
    return tasks


@tasks_bp.route('/tasks/<string:task_id>', methods=["GET"])
def show_task_details(task_id):
    task_details = tasks_table.get_task_details(task_id)
    return task_details


@tasks_bp.route('/create_task', methods=["POST"])
def create_task():
    data = request.get_json()
    res = tasks_table.create_task(**data)
    return res


@tasks_bp.route('/tasks/<string:task_id>', methods=['PATCH'])
def update_task(task_id):
    data = request.get_json()
    task_details = tasks_table.update_task(task_id, **data)
    return task_details


@tasks_bp.route('/tasks/<string:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task_details = tasks_table.delete_task(task_id)
    return task_details
