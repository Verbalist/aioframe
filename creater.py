__author__ = 'verbalist'

import os
import shutil

def init():

    os.mkdir('controllers')
    f = open('controllers/main.py', 'w')
    f.close()
    os.mkdir('models')
    f = open('models/main.py', 'w')
    f.close()
    os.mkdir('views')
    f = open('views/main.py', 'w')
    f.close()
    os.mkdir('routes')
    f = open('routes/main.py', 'w')
    f.close()

    print('init success')

def remove(name):
    if name == 'all':
        name = ''

    shutil.rmtree('controllers/'+ name)
    shutil.rmtree('models/'+ name)
    shutil.rmtree('routes/'+ name)
    shutil.rmtree('views/'+ name)

    print('remove {0} completed'.format(name))


def default():

    f = open('default_create.py', 'w')
    f.close()
    f = open('default_delete.py', 'w')
    f.close()
    f = open('default_update.py', 'w')
    f.close()
    f = open('default_show.py', 'w')
    f.close()
    f = open('default_controller.py', 'w')
    f.close()
    f = open('default_models.py', 'w')
    f.close()
    f = open('default_routes.py', 'w')
    f.close()

    print('default create')

def create_rest(name, default=False):

    #controllers
    os.mkdir('controllers/' + name)
    f = open('controllers/' + name + '/' + name + '.py', 'w')
    if default:
        with open('default_controller.py') as d_c:
            for line in d_c:
                f.writelines(line)
    f.close()

    #models
    os.mkdir('models/' + name)
    f = open('models/' + name + '/' + name + '.py', 'w')
    if default:
        with open('default_models.py') as d_c:
            for line in d_c:
                f.writelines(line)
    f.close()

    #routes
    os.mkdir('routes/' + name)
    f = open('routes/' + name + '/' + name + '.py', 'w')
    if default:
        with open('default_routes.py') as d_c:
            for line in d_c:
                f.writelines(line)
    f.close()

    #views
    os.mkdir('views/' + name)
    f = open('views/' + name + '/create.py', 'w')
    if default:
        with open('default_create.py') as d_c:
            for line in d_c:
                f.writelines(line)
    f.close()
    f = open('views/' + name + '/show.py', 'w')
    if default:
        with open('default_show.py') as d_c:
            for line in d_c:
                f.writelines(line)
    f.close()
    f = open('views/' + name + '/update.py', 'w')
    if default:
        with open('default_update.py') as d_c:
            for line in d_c:
                f.writelines(line)
    f.close()
    f = open('views/' + name + '/delete.py', 'w')
    if default:
        with open('default_delete.py') as d_c:
            for line in d_c:
                f.writelines(line)
    f.close()

    print('create base tree with name: {0}'.format(name))