# -*- coding: utf-8 -*-
# author: LiuZh
# date: 2017-07-26
import os
import shutil

# 图片所在的路径
IMG_DIR_NAME = 'imgs'
# 开发所用图片素材的文件夹名字
DEV_USE_IMG_DIR_NAME = 'operation'

isLocker = False

def fmtGroupName(groupName):
	if 'w' in groupName:
		isLocker = False
		return 'weather-widget-new-group' + groupName[1:]
	elif 's' in groupName:
		isLocker = True
		return 'skin' + groupName[1:]
	else:
		print('\n===into project name error! please input again!===\n')
		return

# 输入组名和项目名 并且 return
def copyProject():

	print('\n---please input from group name: \n(eg. input \'w1\' = \'weather-widget-new-group1\'; input \'s1\' = \'skin1\')')
	fromGroupName = input()

	print('\n---please input from project name:')
	fromProjectName = input()

	print('\n---please input into group name: \n(eg. input \'w1\' = \'weather-widget-new-group1\'; input \'s1\' = \'skin1\')')
	intoGroupName = input()

	print('\n---please input into project name:')
	intoProjectName = input()

	fromGroupName = fmtGroupName(fromGroupName)

	intoGroupName = fmtGroupName(intoGroupName)
	
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


# 复制icon  含72x72和512x512
def copyIcon(basePath):
	print('\n--------coping icon...')

	icon72Path = os.path.join(basePath, 'res', 'drawable', 'icon.png')
	icon512Path = os.path.join(basePath, 'res', 'drawable-xxhdpi', 'icon.png')

	# delete 72x72 icon
	if os.path.exists(icon72Path):
		os.remove(icon72Path)
	# delete 512x512 icon
	if os.path.exists(icon512Path):
		os.remove(icon512Path)

	# copy 72x72 icon
	shutil.copy(os.path.join('.', IMG_DIR_NAME, DEV_USE_IMG_DIR_NAME, 'ic_72.png'), icon72Path)
	# copy 512x512 icon
	shutil.copy(os.path.join('.', IMG_DIR_NAME, DEV_USE_IMG_DIR_NAME, 'ic_512.png'), icon512Path)

	print('\n--------copy icon72x72 & icon512x512 success!--------')


# 输入新包名
def getPkgName():
	print('\n---please input complete package name:')
	return input()

# 输入下载下来的名字
def getPluginName():
	print('\n---please input plugin name :')
	return input()

# 找到MainActivity.java所在的文件路径，没找到的话啥也不返回
def getMAPath(path, file_name):
	for file in os.listdir(path):
		# 如果是文件
		if os.path.isfile(os.path.join(path, file)):
			# 判断文件名是否为MainActiivyt.java，是的话返回路径
			if file == file_name:
				return path
		else : # 不是文件->是文件夹，继续搜索
			maPath = getMAPath(os.path.join(path, file), file_name)
			if(maPath):
				return maPath

# 将该路径下的java文件修改包名
def renameJavaFilePkgName(path, pkgName):
	fileContent = ''
	with open(path, 'r', encoding='utf-8') as f:
		for line in f:
			if 'package mobi' in line:
				line = 'package ' + pkgName +';\n'
			fileContent += line
	with open(path, 'w', encoding='utf-8') as f:
		f.write(fileContent)

# 将该路径下的所有java文件都修改包名
def renameAllJavaFilePkgName(path, pkgName):
	for file in os.listdir(path):
		filePath = os.path.join(path, file)
		if os.path.isfile(filePath) and os.path.splitext(filePath)[1] == '.java':
			renameJavaFilePkgName(filePath, pkgName)
		elif os.path.isdir(filePath):
			renameAllJavaFilePkgName(filePath, pkgName + '.' + file)



# 改包名
# 1.改路径，将旧包名下MainActivity同级所有文件/文件夹copy到新包名下
# 2.改manifest、gradle等地方的包名
def renamePkg(basePath, newPkgName, file_name = "MainActivity.java"):
	print('\n--------renaming...')
	# 路径分隔符
	delimiter = os.path.join(' ', ' ').split(' ')[1]
	# 路径拆分后的数组
	pathArr = basePath.split(delimiter)

# code begin=================================移动文件============================
	path = os.path.join(basePath, 'java')

	# 临时文件夹路径，将MainActivit同级的所有文件/文件夹全部暂时存在这里
	tempPath = os.path.join(basePath, 'temp_dir')
	# 如果临时文件夹存在，先删掉
	if os.path.exists(tempPath):
		shutil.rmtree(tempPath)
	# 拿到MA的路径

	maPath = getMAPath(basePath, file_name)
	# 此处判断是否找到MA的路径，即MA.java是否存在，不存在提示错误并终止运行
	if maPath == None:
		print('\n--------find MainActivity.java path failure :::: no MainActivity.java file!!')
		return
	# 将MA文件同级文件全部copy到临时文件夹
	shutil.copytree(maPath, tempPath)
	# 将java文件夹删掉
	shutil.rmtree(path)
	# 拼接新包名路径
	for dirName in newPkgName.split('.'):
		path = os.path.join(path, dirName)
	# 创建新包名路径
	shutil.copytree(tempPath, path)
	shutil.rmtree(tempPath)
	print('\n--------remove old package & create new package success!--------')
# code end=================================移动文件==============================

# ===============================================================================

# code begin=============================改manifest内包名========================
	fileContent = ''
	amPath = os.path.join(basePath, 'AndroidManifest.xml')
	with open(amPath, 'r', encoding='utf-8') as f:
		for line in f:
			# 如果这一行含有'package'表示這一行需要被重写包名
			if 'package="' in line:
				line = line.split('=')[0] + '="' + newPkgName + '"\n'
			fileContent += line
	with open(amPath, 'w', encoding='utf-8') as f:
		f.write(fileContent)

	print('\n--------edit package name in AndroidManifest.xml success!--------')
# code end=============================改manifest内包名==========================

# ===============================================================================

# code begin=====================settings.gradle内include本项目==================
	sgPath = os.path.join('..', pathArr[1], 'settings.gradle')

	fileContent = 'include \':' + pathArr[2] + '\'\n'

	with open(sgPath, 'r', encoding='utf-8') as f:
		fileContent += f.read()

	with open(sgPath, 'w', encoding='utf-8') as f:
		f.write(fileContent)

	print('\n--------include project in settings.gradle success!--------')
# code end=====================settings.gradle内include本项目====================

# ===============================================================================

# code begin=====================build.gradle内包名修改==========================
	bgPath = os.path.join('..', pathArr[1], pathArr[2], 'build.gradle')

	fileContent = ''
	with open(bgPath, 'r', encoding='utf-8') as f:
		for line in f:
			if 'applicationId "mobi' in line:
				line = line.split('"')[0] + '"' + newPkgName + '"\n'
			fileContent += line
	with open(bgPath, 'w', encoding='utf-8') as f:
		f.write(fileContent)

	print('\n--------edit package name in build.gradle success!--------')
# code end=====================build.gradle内包名修改============================

# ===============================================================================

# code begin=========config.xml内改pluginName、productId、description============
	configPath = os.path.join(basePath, 'res', 'values', 'config.xml')

	oldPluginName = ''
	if os.path.isfile(configPath):
		pluginName = getPluginName()
		fileContent = ''
		with open(configPath, 'r', encoding='utf-8') as f:
			for line in f:
				if 'pluginName' in line:
					# oldPluginName = line[line.index('>') + 1:line.index('/') - 1]
					# print('---=-=-=-=-=-' + oldPluginName)
					# break
					line = '<string name="pluginName">' + pluginName + '</string>\n'
				elif 'productId' in line:
					line = '<string name="productId">' + pluginName + '</string>\n'
				elif 'description' in line:
					if isLocker:
						line = '<string name="description">' + pluginName + ' Design,get Sense Flip Clock on your screen.(4x2/5x2/4x1/5x1)</string>\n'
					else:
						line = '<string name="description">' + pluginName + ' .(4x2/5x2/4x1/5x1)</string>\n'
				elif 'widget_of_ezweather' in line:
					line = '<string name="widget_of_ezweather">' + pluginName +' style Widget of Amber Weather</string>\n'
				fileContent += line
	# with open(configPath, 'r', encoding='utf-8') as f:
	# 	for line in f:
	# 		if oldPluginName in line:
	# 			line.replace(oldPluginName, pluginName)
	# 		fileContent += line

		with open(configPath, 'w', encoding='utf-8') as f:
			f.write(fileContent)
		print('\n--------edit pluginName in config.xml success!--------')
		print('\n========this name need verify, please see config.xml!========')
# code end===========config.xml内改pluginName、productId、description============

# ===============================================================================

# code begin=====================修改所有.java文件的包名=========================
	newPkgPath = path
	renameAllJavaFilePkgName(newPkgPath, newPkgName)
	print('\n--------rename all java file package success!--------')
# code end=======================修改所有.java文件的包名=========================


	print('\n--------rename success!--------\n')