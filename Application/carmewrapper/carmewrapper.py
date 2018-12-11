"""
Definition of views.
"""

from src.cli import commands
import os
import io
import logging
import ruamel.yaml

def new(projectid):
    """carme new"""
    cwd=os.getcwd()
    commands.new.callback('projects/'+projectid, 'az-z2jh', False)
    os.chdir(cwd)
    
    return projectid
    
def _cmd(projectid, package, command):
    logger = logging.getLogger()
    stream = io.StringIO()
    streamHandler = logging.StreamHandler(stream=stream)
    logger.addHandler(streamHandler)
    logger.addHandler(logging.FileHandler('projects/'+projectid+"/cmd.log"))
    cwd=os.getcwd()
    os.chdir('projects/'+projectid)
    commands.cmd.callback(package, command, False, False, False, True)
    os.chdir(cwd)
    streamHandler.flush()
    stream.flush()
    return stream.getvalue()
    
def getClusterConfig(projectid):
    """carme cmd az-cluster show_config --yes"""
    #Verifying Cluster Configuration Settings
    result=_readFile(projectid,"./config/az-cluster.yaml")
    return result
    
def createCluster(projectid):
    """carme cmd az-cluster create_all --yes"""
    #Lauch the Cluster
    result=_cmd(projectid, 'az-cluster', 'create_all')
    return result

def getJupyterHubConfig(projectid):
    """carme cmd jupyterhub show_config --yes"""
    result=_readFile(projectid,"./config/jupyterhub.yaml")
    return result

def installJupyter(projectid):
    """carme cmd jupyterhub install_all --yes"""
    result=_cmd(projectid, 'jupyterhub', 'install_all')
    return result
    
def cleanUp(projectid):
    """carme cmd az-cluster delete_group"""
    result=_cmd(projectid, 'az-cluster', 'delete_group')
    return result

def _getFilePath(projectid, filename):
    return os.path.abspath(os.path.join("projects",projectid,filename))

def _readFile(projectid,filename):
    """reads a log or config file"""
    path = _getFilePath(projectid,filename)
    if not os.path.isfile(path):
        return None
    # Open the file as f.
    # The function readlines() reads the file.             
    with open(path) as f:
        content = f.readlines()
    return os.sep.join(content)

CMD_LOG_FILE = './cmd.log'
STATUS_FILE = './status.yaml'

def getLastLog(projectid):
    return _readFile(projectid,CMD_LOG_FILE)

def getStatuses(projectid):
    return _readFile(projectid,STATUS_FILE)

def setStatus(projectid, status, value):
    config(projectid, {status:value},STATUS_FILE)

azConfigKeys = set(("subscription","resource_group","cluster_name","location","dns_prefix","machine_type","kubernetes_version","num_nodes","num_nodes_class","max_nodes"))
jhConfigKeys = set(("platform","cluster_name","namespace","releasename","version","security"))

def configAll(projectid, config):
    keys = set(config.keys())
    newkeys = keys.intersection(jhConfigKeys)
    _setConfigValues(projectid, "./config/az-cluster.yaml",config, keys)
    newkeys = keys.intersection(azConfigKeys)
    _setConfigValues(projectid, "./config/juptyerhub.yaml",config, keys)

def config(projectid, config, filename):
    _setConfigValues(projectid, filename, config, config.keys())

def _setConfigValues(projectid, filename, config, keys, make=True):
    path = _getFilePath(projectid,filename)
    if not os.path.isfile(path):
        if make:
            with open(path, 'w') as fp:
                fp.close()
        else:
            print("Couldn't find file", filename)
            return

    yaml = ruamel.yaml.YAML()

    with open(path) as fp:
        data = yaml.load(fp)

    if data is None:
        data = {}

    for key in keys:
        if(config[key] and (not config[key].isspace())):
            data[key] = config[key]

    with open(path, 'w') as fp:
        yaml.dump(data, fp)
    return

def getProjectDetails(projectid):
    return {
        'projectid': projectid,
        'clusterConfig' : getClusterConfig(projectid),
        'jupyterHubConfig' : getJupyterHubConfig(projectid),
        'status' : getStatuses(projectid),
        'lastLog' : getLastLog(projectid),
    }