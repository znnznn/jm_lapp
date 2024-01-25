from celery import shared_task

from clickup_api import celery_app
from clickup_api.client import ClickUpClient
from settings import CLICKUP_API_KEY


@shared_task
def get_tasks():
    client = ClickUpClient(accesstoken=CLICKUP_API_KEY)
    teams = client.get_teams()
    print(teams)
    spaces = client.get_spaces(teams.teams[0].id)
    print(spaces)
    print("1+++++++++++++++++++++++++++")
    space = client.get_space(spaces.spaces[0].id)
    print(space)
    print("2+++++++++++++++++++++++++++")
    folders = client.get_folders(space.id)
    print(folders)
    print("3+++++++++++++++++++++++++++")
    folder = client.get_folder(folders.folders[0].id)
    print(folder)
    print("4+++++++++++++++++++++++++++")
    lists = client.get_lists(folder_id=folder.id)
    print(lists)
    print("5+++++++++++++++++++++")
    list = client.get_list(lists.lists[0].id)
    print(list)
    print("6+++++++++++++++++++++")
    tasks = client.get_tasks(lists.lists[0].id)
    print(tasks)
    print("7+++++++++++++++++++++")
    task = client.get_task(tasks.tasks[0].id)
    print(task)



if __name__ == "__main__":
    get_tasks()