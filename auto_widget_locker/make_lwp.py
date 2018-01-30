# -*- coding: utf-8 -*-
# author: Gavin
# date: 2017-09-19
from fun import *

# 图片所在的路径
IMG_DIR_NAME = 'imgs'
RESOURCE_DIR_NAME = 'resources'
DEV_USE_IMG_DIR_NAME = 'operation'
DOWNLOAD_NAME = 'Live Wallpaper'


def copy_lwp_project():
    print(
        '\n---please input from group number: \n(eg. input \'1\' = \'lwp_group1\')')
    fromGroupName = input()

    print('\n---please input from project name:')
    fromProjectName = input()

    print(
        '\n---please input into group number: \n(eg. input \'1\' = \'lwp_group1\')')
    intoGroupName = input()

    print('\n---please input into project name:')
    intoProjectName = input()

    fromGroupName = group_name(fromGroupName)

    intoGroupName = group_name(intoGroupName)

    if fromGroupName == None or intoGroupName == None:
        return

    fromPath = os.path.join('..', fromGroupName, fromProjectName)
    intoPath = os.path.join('..', intoGroupName, intoProjectName)
    # dir exists
    if os.path.exists(fromPath):
        # copy旧项目，并重命名为新名
        shutil.copytree(fromPath, intoPath)
        return os.path.join(intoPath, 'src', 'main')
    else:
        print('\n===path not found! please input again!===\n')
        return copyProject()


def end_with(s, *end_string):
    array = map(s.endswith,end_string)
    if True in array:
        return True
    else:
        return False

def group_name(group_number):
    return 'lwp_group'+str(group_number)

def copy_resource(basePath):
    print('\n--------coping icon...')

    icon72Path = os.path.join(basePath, 'res', 'drawable-hdpi', 'icon.png')
    icon512Path = os.path.join(basePath, 'res', 'drawable-xxhdpi', 'icon.png')
    resource_path = os.path.join(basePath, 'assets')

    # delete 72x72 icon
    if os.path.exists(icon72Path):
        os.remove(icon72Path)
    # delete 512x512 icon
    if os.path.exists(icon512Path):
        os.remove(icon512Path)

    # copy 72x72 icon
    shutil.copy(os.path.join('.', IMG_DIR_NAME, DEV_USE_IMG_DIR_NAME,'ic_72.png'), icon72Path)
    # copy 512x512 icon
    shutil.copy(os.path.join('.', IMG_DIR_NAME, DEV_USE_IMG_DIR_NAME,'ic_512.png'), icon512Path)
    
    for file in file_name(os.path.join('.', IMG_DIR_NAME, RESOURCE_DIR_NAME)):
        shutil.copy(os.path.join('.', IMG_DIR_NAME, RESOURCE_DIR_NAME, file), resource_path)

    print('\n--------copy icon72x72 & icon512x512 success!--------')


def file_name(file_dir):
    resource_file=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if end_with(file, '.png', '.jpg', '.webp', '.mp4'):
                resource_file.append(file)
    return resource_file #当前路径下所有非目录子文件
        
        

def choose_engine(engine):
    lwp_engine = ''
    if engine == 'video':
        lwp_engine = 'LwpConstants.ENGINE_TYPE_VIDEO'
    elif engine == 'picture':
        lwp_engine = ' LwpConstants.ENGINE_TYPE_PARALLAX'
    else:
        print("error engine")
    return lwp_engine

def input_parameter():
    print("please input sens")
    sens = input()
    print("please input resents")
    resents = input()
    print("please input resents2")
    resents2 = input()
    print("please input xPageOffset")
    xPageOffset = input()
    print("please input xInitOffset")
    xInitOffset = input()
    print("please input tX_1")
    tX_1 = input()
    print("please input tY_1")
    tY_1 = input()
    print("please input tX_2")
    tX_2 = input()
    print("please input tY_2")
    tY_2 = input()
    print("please input tX_3")
    tX_3 = input()
    print("please input tY_3")
    tY_3 = input()
    parameter = {
        "sens":sens,
        "resents":resents,
        "resents2":resents2,
        "xPageOffset":xPageOffset,
        "xInitOffset":xInitOffset,
        "tX_1":tX_1,
        "tY_1":tY_1,
        "tX_2":tX_2,
        "tY_2":tY_2,
        "tX_3":tX_3,
        "tY_3":tY_3
                     }
    return parameter

def get_helper_path(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            if file == 'LwpHelper.java':
                return path
        else:
            maPath = get_helper_path(os.path.join(path, file))
            if (maPath):
                return maPath

def make_lwp(basePath):
    file_path = get_helper_path(basePath)
    file_path = os.path.join(file_path, 'LwpHelper.java')
    print("input engine video or picture")
    engine_kind = input()
    if engine_kind == 'picture':
        params = input_parameter()
    engine = choose_engine(engine_kind)
    resource_path = os.path.join(basePath, 'assets')
    files = file_name(resource_path)
    print(files)
    
    
    with open(file_path,'r', encoding='utf-8') as file:
        all_lines = ''
        for line in file:
            if engine_kind == 'picture':
                if "LwpConstants.sens" in line:
                    line = "\t\tLwpConstants.sens = " + params.get('sens') + ";\n"
                if "LwpConstants.resents" in line:
                    line = "\t\tLwpConstants.resents = " + params.get('resents') + ";\n"
                if "LwpConstants.resents2" in line:
                    line = "\t\tLwpConstants.resents2 = " + params.get('resents2') + ";\n"
                if "LwpConstants.xPageOffset" in line:
                    line = "\t\tLwpConstants.xPageOffset = " + params.get('xPageOffset') + ";\n"
                if "LwpConstants.xInitOffset" in line:
                    line = "\t\tLwpConstants.xInitOffset = " + params.get('xInitOffset') + ";\n"
                if "LwpConstants.tX_1" in line:
                    line = "\t\tLwpConstants.tX_1 = " + params.get('tX_1') + ";\n"
                if "LwpConstants.tY_1" in line:
                    line = "\t\tLwpConstants.tY_1 = " + params.get('tY_1') + ";\n"
                if "LwpConstants.tX_2" in line:
                    line = "\t\tLwpConstants.tX_2 = " + params.get('tX_2') + ";\n"
                if "LwpConstants.tY_2" in line:
                    line = "\t\tLwpConstants.tY_2 = " + params.get('tY_2') + ";\n"
                if "LwpConstants.tX_3" in line:
                    line = "\t\tLwpConstants.tX_3 = " + params.get('tX_3') + ";\n"
                if "LwpConstants.tY_3" in line:
                    line = "\t\tLwpConstants.tY_3 = " + params.get('tY_3') + ";\n"
                if 'LwpConstants.WALL_PAPER_IMAGE_PATH_ONE' in line:
                    line = '\t\tLwpConstants.WALL_PAPER_IMAGE_PATH_ONE =' + '"' + files[0] + '"' +';\n'
                if 'LwpConstants.WALL_PAPER_IMAGE_PATH_TWO' in line:
                    line = '\t\tLwpConstants.WALL_PAPER_IMAGE_PATH_TWO =' + '"' + files[1] + '"' + ';\n'
                if 'LwpConstants.WALL_PAPER_IMAGE_PATH_THREE' in line:
                    line = '\t\tLwpConstants.WALL_PAPER_IMAGE_PATH_THREE =' + '"' + files[2] + '"' + ';\n'
            else:
                if "LwpConstants.videoName" in line:
                    line = "\t\tLwpConstants.videoName =" + '"' + files[0] +'"' + ';\n'

            if line.startswith("LwpConstants.ENGINE_TYPE_CODE") and "LwpConstants.ENGINE_TYPE_CODE" in line:
                line = "\t\tLwpConstants.ENGINE_TYPE_CODE = " + engine + ";\n"

            all_lines += line
    with open(file_path,  'w', encoding='utf-8') as file:
        file.write(all_lines)


