__author__ = 'verbalist'

import os
import shutil

def init(path):

    os.mkdir(path + 'controllers')
    f = open(path + 'controllers/main.py', 'w')
    with open(path + 'controllers_main.py') as d_c:
        for line in d_c:
            f.writelines(line)
    f.close()
    os.mkdir(path + 'models')
    f = open(path + 'models/main.py', 'w')
    with open(path + 'models_main.py') as d_c:
        for line in d_c:
            f.writelines(line)
    f.close()
    os.mkdir(path + 'views')
    f = open(path + 'views/main.py', 'w')
    with open(path + 'views_main.py') as d_c:
        for line in d_c:
            f.writelines(line)
    f.close()
    os.mkdir(path + 'routes')
    f = open(path + 'routes/main.py', 'w')
    with open(path + 'routes_main.py') as d_c:
        for line in d_c:
            f.writelines(line)
    f.close()

    print('init success')

def remove(name, path):
    if name == 'all':
        name = ''

    shutil.rmtree(path + 'controllers/'+ name)
    shutil.rmtree(path + 'models/'+ name)
    shutil.rmtree(path + 'routes/'+ name)
    shutil.rmtree(path + 'views/'+ name)

    print('remove {0} completed'.format(name))



def create_rest(name, path, default=True):

    #controllers
    f = open(path + 'controllers/' + name + '.py', 'w')
    if default:
        with open(path + 'default_controllers.txt') as d_c:
            for line in d_c:
                f.writelines(line.replace("{PATH}", name))
    f.close()

    #models
    f = open(path + 'models/' + name + '.py', 'w')
    if default:
        with open(path + 'default_models.txt') as d_c:
            for line in d_c:
                f.writelines(line.replace("{PATH}", name))
    f.close()

    #routes
    f = open(path + 'routes/' + name + '.py', 'w')
    if default:
        with open(path + 'default_routes.txt') as d_c:
            for line in d_c:
                f.writelines(line.replace("{PATH}", name))
    f.close()

    #views
    f = open(path + 'views/' + name + '.py', 'w')
    if default:
        with open(path + 'default_views.txt') as d_c:
            for line in d_c:
                f.writelines(line.replace("{PATH}", name))
    f.close()


    print('create base tree with name: {0}'.format(name))