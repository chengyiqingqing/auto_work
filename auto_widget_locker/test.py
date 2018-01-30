from make_lwp import *
from fun import *
if __name__ == '__main__':
    # base_path = "/Users/gavin/Work/AmberWeatherWork/lwp_group3/wallpaper/src/main/"
    # copyIcon(basePath=base_path)
    base_path = copy_lwp_project()

    copy_resource(base_path)

    pkgName = getPkgName()
    print(pkgName)
    print(base_path)

    renamePkg(base_path, pkgName, file_name='LwpHelper.java')

    make_lwp(base_path)


