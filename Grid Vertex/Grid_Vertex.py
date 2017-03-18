import os
import pickle

def init():
    global dir
    dir = os.getcwd()
    global running
    running = False

def send(data, app):
    os.chdir(os.path.join(os.path.expanduser('~'), "Documents" ))
    pickle_out = open('gridVertexData.gv', 'w')
    pickle.dump(data, pickle_out)
    pickle_out.close()
    pickle_out = open('gridVertexApp.gv', 'w')
    pickle.dump(app, pickle_out)
    pickle_out.close()
    os.chdir(dir)

def receive():
    os.chdir(os.path.join(os.path.expanduser('~'), "Documents" ))
    pickle_in = open('gridVertexData.gv', 'r')
    return(pickle.load(pickle_in))
    os.chdir(dir)

def app():
    os.chdir(os.path.join(os.path.expanduser('~'), "Documents" ))
    pickle_in = open('gridVertexApp.gv', 'r')
    return(pickle.load(pickle_in))
    os.chdir(dir)

def setDir(path):
    global dir
    dir(path)