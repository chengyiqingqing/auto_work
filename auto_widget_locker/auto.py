# -*- coding: utf-8 -*-
# author: LiuZh
# date: 2017-07-26

import os
from fun import *

print('\n=================************************=====================')
print('current version only supports lock screens and widgets! lwp please not use this version!')
print('=================************************=====================')

basePath = copyProject()

copyIcon(basePath)

pkgName = getPkgName()

renamePkg(basePath, pkgName)

