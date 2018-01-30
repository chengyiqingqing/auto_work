# widget和locker自动化脚本(Python)

暂时不支持lwp

# 使用步骤

**1. 此包放在组的同级目录下**

例如:

-skin5

-auto_widget_locker

----auto.py

----fun.py

----imgs

--------operation(包含icon,icon名需为ic_72.png、ic_512.png)

- operation文件夹名可能与设计师给的文件夹名字不一样,可以自行修改fun.py内DEV_USE_IMG_DIR_NAME变量值

- ic_71.png、ic_512.png设计师给的图片可能也不一样,也可在fun.py内70及71行修改

**2. 你要从哪copy项目过来**

- 输入组名

> 例:
> s1表示skin1
> w1表示weather-widget-new-group1

- 输入项目名(全名)

**3. 你要copy到哪一个组,项目叫什么名字**

- 输入组名(同上)

- 输入项目名(新做项目的名字)

此时,就把旧项目copy到了你要写的项目,并把APP的icon替换完成

**4. 输入包名**

输入全包名(不可遗漏,全长的包名)

此时会将各处与包名有关的地方都替换修改好

**5. 输入插件名**

也就是"下载下来的名字",此处输入后会自动在config.xml中将内容替换好


整个流程完成