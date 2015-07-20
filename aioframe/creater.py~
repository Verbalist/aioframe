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


# def default(path):
#
#     f = open(path + 'default_create.py', 'w')
#     f.close()
#     f = open(path + 'default_delete.py', 'w')
#     f.close()
#     f = open(path + 'default_update.py', 'w')
#     f.close()
#     f = open(path + 'default_show.py', 'w')
#     f.close()
#     f = open(path + 'default_controllers.txt', 'w')
#     f.close()
#     f = open(path + 'default_models.txt', 'w')
#     f.close()
#     f = open(path + 'default_routes.txt', 'w')
#     f.close()
#     f = open(path + 'default_views.txt', 'w')
#     f.close()
#
#     print(path + 'default create')

def create_rest(name, path, default=True):

    #controllers
    # os.mkdir(path + 'controllers/' + name)
    f = open(path + 'controllers/' + name + '.txt', 'w')
    if default:
        with open(path + 'default_controllers.txt') as d_c:
            for line in d_c:
                f.writelines(line.replace("{PATH}", name))
    f.close()

    #models
    # os.mkdir(path + 'models/' + name)
    f = open(path + 'models/' + name + '.txt', 'w')
    if default:
        with open(path + 'default_models.txt') as d_c:
            for line in d_c:
                f.writelines(line.replace("{PATH}", name))
    f.close()

    #routes
    # os.mkdir(path + 'routes/' + name)
    f = open(path + 'routes/' + name + '.txt', 'w')
    if default:
        with open(path + 'default_routes.txt') as d_c:
            for line in d_c:
                f.writelines(line.replace("{PATH}", name))
    f.close()

    #views
    # os.mkdir(path + 'views/' + name)
    f = open(path + 'views/' + name + '.txt', 'w')
    if default:
        with open(path + 'default_views.txt') as d_c:
            for line in d_c:
                f.writelines(line.replace("{PATH}", name))
    f.close()
    # f = open(path + 'views/' + name + '/create.py', 'w')
    # if default:
    #     with open(path + 'default_create.py') as d_c:
    #         for line in d_c:
    #             f.writelines(line)
    # f.close()
    # f = open(path + 'views/' + name + '/show.py', 'w')
    # if default:
    #     with open(path + 'default_show.py') as d_c:
    #         for line in d_c:
    #             f.writelines(line)
    # f.close()
    # f = open(path + 'views/' + name + '/update.py', 'w')
    # if default:
    #     with open(path + 'default_update.py') as d_c:
    #         for line in d_c:
    #             f.writelines(line)
    # f.close()
    # f = open(path + 'views/' + name + '/delete.py', 'w')
    # if default:
    #     with open(path + 'default_delete.py') as d_c:
    #         for line in d_c:
    #             f.writelines(line)
    # f.close()

    print('create base tree with name: {0}'.format(name))