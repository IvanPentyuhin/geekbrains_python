"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""

import os



projectname = 'my_project'

folders = ['settings', 'mainapp', 'adminapp', 'authapp']


if not os.path.exists(projectname):
    os.mkdir(projectname)

for dir in folders:
    folder = os.path.join(projectname, dir)
    if not os.path.exists(folder):
        os.mkdir(folder)







