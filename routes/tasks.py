from typing import List
from flask import Blueprint, render_template, request
from src.controller.tasksController import TasksController
from src.repositories.taskRepository import TaskRepository
from src.models.tasks import Task

task_route = Blueprint('task', __name__)

tasks: List[Task] = []
repository = TaskRepository(tasks)
controller = TasksController(repository)

controller.create("Atividade de SO", "to-do")

"""
FUNÇÕES:
    - LISTAR TAREFAS (GET)
    - CRIAR TAREFAS (POST)
    - DELETAR TAREFAS (DELETE)
    - ATUALIZAR TAREFAS (PUT)

    * /tarefas/ (GET) - LISTAR
    * /tarefas/ (POST) - CRIAR
    * /tarefas/new (GET) - mostrar formulário para criar tarefa
    * /tarefas/<id> (GET) - OBTER DADOS DE UMA TAREFA
    * /tarefas/<id>/edit (GET) - mostrar formulário para editar
    * /tarefas/<id>/update (PUT) - ATUALIZAR
    * /tarefas/<id>/delete (DELETE) - DELETAR 
"""

@task_route.route('/')
def list_tasks():
    return render_template('list_tasks.html', tasks = controller.list())

@task_route.route('/', methods=['POST'])
def create_task():

    data = request.json

    task_ = controller.create(data['name'], data['type'])

    return render_template('item_task.html', task = task_)

@task_route.route('/new')
def form_task():
    return render_template('form_tasks.html')

@task_route.route('/<int:task_id>')
def get_task(task_id):
    return render_template('get_task.html')

@task_route.route('/<int:task_id>/edit')
def form_edit_task(tasl_id):
    return render_template('form_edit_task.html')

@task_route.route('/<int:task_id>/update', methods=['PUT'])
def update_task(task_id):
    pass

@task_route.route('/<int:task_id>/delete', methods=['DELETE'])
def delete_task(task_id):
    
    controller.delete(task_id)
    
    return {'ok': 'ok'}