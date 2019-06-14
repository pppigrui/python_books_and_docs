[TOC]



# 1. 搭建项目环境

------

## 一、创建工程

当前，较新的Pycharm版本都支持同时创建虚拟环境和Django工程。所以我们下面的操作都在Pycharm中进行。

首先打开Pycharm，进入创建工程的对话框，注意下面的红框提示：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-71e0ce49d06ae624.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 在Location处选择工程目录
- 在New environment using处选择Virtualenv（这可能需要你提前pip install virtualenv进行虚拟工具virtualenv的安装）。通常情况下，虚拟环境会以venv的名字，自动在工程目录下生成。
- 在Base interpreter处，选择你要使用的Python解释器
- 下面两个单选框，根据需要自行选择
- 如果想使用现成的解释器或者虚拟环境，请选择Existing interpreter

![image.png](https://upload-images.jianshu.io/upload_images/2458108-14b1ef2fb3401340.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

再点开下方的More Settings：

- Template language选择使用的模板语言，默认Django就行，可选Jinjia。
- Templates folder：Pycharm安利给我们的功能，额外创建一个工程级别的模板文件的保存目录，可以不设置，空着，这里使用默认设置吧。
- 启用Admin，一般勾上。

![image.png](https://upload-images.jianshu.io/upload_images/2458108-6e777c2e2c25a95e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

没什么问题了，就点击Create吧。

下面就是一段时间的等待，Pycharm会帮助我们自动创建虚拟环境，以及安装最新版本的Django。

创建完成之后，进入Pycharm的设置菜单，可以看到当前Django版本是最新的2.2版本。如果你要指定过去的版本，比如2.1、1.11等，那就不能这么操作了，需要在命令行下自己创建虚拟环境并安装django。或者在这里先删除Django，再安装你想要的指定版本。

![image.png](https://upload-images.jianshu.io/upload_images/2458108-0dfa5bccfbd43740.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

看下我们当前的状态，注意venv这个虚拟环境目录，以及我们额外创建的templats目录：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-b9dc72921e4fe4df.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 二、创建app

点击Pycharm最下方工具栏中的Terminal按钮，进入终端界面，可以看到，我们已经在工程的根目录下，并且自动进入了虚拟环境内。（如果你不是通过Pycharm创建的虚拟环境，那么在这里，你可能需要手动激活虚拟环境。）

使用`where python`和`python -V`查看一下环境：

```python
(venv) D:\work\2019\for_test\mysite>where python
D:\work\2019\for_test\mysite\venv\Scripts\python.exe
C:\Program Files\Python37\python.exe
C:\Program Files\Python36\python.exe
C:\Users\feixuelym\Anaconda3\python.exe

(venv) D:\work\2019\for_test\mysite>python -V
Python 3.7.3
```

接下来运行`python manage.py startapp login`创建login这个app。

按照上面的步骤操作完后，login应用就创建成功了，让我们看一下Pycharm中的目录结构：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-a4aa77b0b7b3c39e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 三、 设置时区和语言

Django默认使用美国时间和英语，在项目的settings文件中，如下所示：

```python
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
```

我们把它改为`亚洲/上海`时间和中文（别问我为什么没有北京时间，也别把语言写成`zh-CN`），注意USE_TZ 改成False了。

```python
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'     # 这里修改了

TIME_ZONE = 'Asia/Shanghai'    # 这里修改了

USE_I18N = True

USE_L10N = True

USE_TZ = False    # 这里修改了
```

## 四、 启动开发服务器

现在，我们可以启动一下开发服务器，测试一下我们的工程了。

在Pycharm的`Run/Debug Configurations`配置界面里，将HOST设置为`127.0.0.1`，Port保持原样的`8000`，确定后，点击绿色三角，走你！

![image.png](https://upload-images.jianshu.io/upload_images/2458108-21d958d1bae92b7e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

在本机的浏览器中访问`http://127.0.0.1:8000/`，或者点击Pycharm界面里的链接：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-c7b98396969434df.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

顺利的话，在浏览器中，你可以看到如下的欢迎界面：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-5adae15363e392ec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)





# 2. 设计数据模型

------

使用Django开发Web应用的过程中，很多人都是急急忙忙地写视图，写前端页面，把最根本的模型设计给忽略了。模型中定义了数据如何在数据库内保存，也就是数据表的定义方式。这部分工作体现在Django的代码中，其实就是model类的设计。

## 一、 数据库模型设计

作为一个用户登录和注册项目，需要保存的都是各种用户的相关信息。很显然，我们至少需要一张用户表User，在用户表里需要保存下面的信息：

- 用户名
- 密码
- 邮箱地址
- 性别
- 创建时间

我们现在就暂定保存这些信息吧，更多的内容，请大家在实际项目中自行添加。

进入`login/models.py`文件，这里将是我们整个login应用中所有模型的存放地点，代码如下：

```python
from django.db import models

# Create your models here.


class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"
```

各字段含义：

- name: 必填，最长不超过128个字符，并且唯一，也就是不能有相同姓名；
- password: 必填，最长不超过256个字符（实际可能不需要这么长）；
- email: 使用Django内置的邮箱类型，并且唯一；
- sex: 性别，使用了一个choice，只能选择男或者女，默认为男；
- 使用`__str__`方法帮助人性化显示对象信息；
- 元数据里定义用户按创建时间的反序排列，也就是最近的最先显示；

注意：这里的用户名指的是网络上注册的用户名，不要等同于现实中的真实姓名，所以采用了唯一机制。如果是现实中的人名，那是可以重复的，肯定是不能设置unique的。另外关于密码，建议至少128位长度，原因后面解释。

## 二、 设置数据库后端

定义好了模型后，就必须选择我们用来保存数据的数据库系统。Django支持Mysql，SQLite，Oracle等等。

Django中对数据库的设置在settings文件中，如下部分：

```python
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

Django默认使用SQLite数据库，并内置SQLite数据库的访问API，也就是说和Python一样原生支持SQLite。本项目使用SQLite作为后端数据库，因此不需要修改settings中这部分内容。如果你想要使用别的数据库，请自行修改该部分设置。

## 三、注册app

每次创建了新的app后，都需要在全局settings中注册，这样Django才知道你有新的应用上线了。在settings的下面部分添加‘login’，建议在最后添加个逗号。

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
]
```

## 四、创建记录和数据表

app中的models建立好了后，并不会自动地在数据库中生成相应的数据表，需要你手动创建。

进入Pycharm的terminal终端，执行下面的命令：

```python
python manage.py makemigrations
```

返回结果：

```python
(venv) D:\work\2019\for_test\mysite>python manage.py makemigrations
Migrations for 'login':
  login\migrations\0001_initial.py
    - Create model User
```

Django自动为我们创建了`login\migrations\0001_initial.py`文件，保存了我们的第一次数据迁移工作，也就是创建了User模型。

接着执行下面的命令：

```
python manage.py migrate
```

Django将在数据库内创建真实的数据表。如果是第一次执行该命令，那么一些内置的框架，比如auth、session等的数据表也将被一同创建，如下所示：

```python
(venv) D:\work\2019\for_test\mysite>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, login, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying login.0001_initial... OK
  Applying sessions.0001_initial... OK
```

# 3. admin后台

------

在我们开发的初期，没有真实的用户数据，也没有完整的测试环境，为了测试和开发的方便，通常我们会频繁地使用Django给我们提供的Admin后台管理界面，创建测试用例，观察模型效果等等。

## 一、 在admin中注册模型

admin后台本质上是Django给我们提供的一个app，默认情况下，它已经在settings中注册了，如下所示的第一行！同样的还有session会话框架，后面我们会使用的。

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',     # 看这里
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',      # 看这里
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
]
```

进入`login/admin.py`文件，代码如下：

```python
from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.User)
```

暂时简单点，直接注册就好了。

## 二、创建超级管理员

Django的admin后台拥有完整的较为安全的用户认证和授权机制，防护等级还算可以。

要进入该后台，需要创建超级管理员，该管理员和我们先前创建的User用户不是一个概念，要注意区别对待。

同样在Pycharm的终端中，执行下面的命令：

```
python manage.py createsuperuser
```

用户名、邮箱和密码请自行设定，但一定不要忘记。密码最好有一定强度，并且不能太简单和普遍，会有提示，我这里强制通过了。

```PYTHON
(venv) D:\work\2019\for_test\mysite>python manage.py createsuperuser
用户名 (leave blank to use 'feixuelym'): admin
电子邮件地址: admin@admin.com
Password:
Password (again):
这个密码太常见了。
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```

## 三、 使用Admin后台

创建好超级管理员后，就可以启动我们的开发服务器了，然后在浏览器中访问`http://127.0.0.1:8000/admin/`地址，可以看到如下的登录界面：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-fb819965b1edfabf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

输入我们先前创建的超级管理员账户，进入管理界面：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-083c3175bc9d6b75.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

注意，图中下方的`认证和授权`是admin应用自身的账户管理，上面的LOGIN栏目才是我们创建的login应用所对应的User模型。

点击Login栏目中的用户链接，进入用户列表界面，发现是空的，因为我们当前没有任何用户。点击右上方的增加用户按钮，我们创建几个测试用户试试：

通过输入不同的数据，我们看到Email会有地址合法性检查，性别有个选择框，非常的人性化。

![image.png](https://upload-images.jianshu.io/upload_images/2458108-72895a95fe1679cc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

但是，实际上这里还有点小问题，那就是密码相关。密码不能保存为明文，这个问题我们后面再解决；其次，不可以这么随意的修改和设置密码，为了展示的方便性，我们先这样。

这里我随便创建了三个测试账号，如下所示：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-9141cfc07812e515.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

admin的使用和配置博大精深，但在本实战项目里，我们暂时把它当做一个数据库管理后台使用。

# 4. url路由和视图

------

前面我们已经创建好数据模型了，并且在admin后台中添加了一些测试用户。下面我们就要设计好站点的url路由、对应的处理视图函数以及使用的前端模板了。

## 一、 路由设计

我们初步设想需要下面的四个URL：

| URL        | 视图                 | 模板           | 说明 |
| :--------- | :------------------- | :------------- | :--- |
| /index/    | login.views.index    | index.html     | 主页 |
| /login/    | login.views.login    | login.html     | 登录 |
| /register/ | login.views.register | register.html  | 注册 |
| /logout/   | login.views.logout   | 无需专门的页面 | 登出 |

重要说明：由于本项目目的是打造一个针对管理系统、应用程序等需求下的可重用的登录/注册app，而不是门户网站、免费博客等无需登录即可访问的网站，所以在url路由、跳转策略和文件结构的设计上都是尽量自成体系。具体访问的策略如下：

- 未登录人员，不论是访问index还是login和logout，全部跳转到login界面
- 已登录人员，访问login会自动跳转到index页面
- 已登录人员，不允许直接访问register页面，需先logout
- 登出后，自动跳转到login界面

考虑到登录注册系统属于站点的一级功能，为了直观和更易于接受，这里没有采用二级路由的方式，而是在根路由下直接编写路由条目，同样也没有使用反向解析名（name参数）。所以，在重用本app的时候，一定要按照app使用说明，加入相应的url路由。

根据上面的策划，打开`mysite/urls.py`文件，写入下面的代码：

```python
from django.contrib import admin
from django.urls import path
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
]
```

注意要先从login导入views模块。

## 二、 架构初步视图

路由写好了，就进入`login/views.py`文件编写视图的框架，代码如下：

```python
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    pass
    return render(request, 'login/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect("/login/")
```

我们先不着急完成视图内部的具体细节，而是把框架先搭建起来。

注意：

- 在顶部额外导入了`redirect`，用于logout后，页面重定向到‘/login/’这个url，当然你也可以重定向到别的页面；
- 另外三个视图都返回一个render调用，render方法接收request作为第一个参数，要渲染的页面为第二个参数，以及需要传递给页面的数据字典作为第三个参数（可以为空），表示根据请求的部分，以渲染的HTML页面为主体，使用模板语言将数据字典填入，然后返回给用户的浏览器。
- 渲染的对象为login目录下的html文件，这是一种安全可靠的文件组织方式，我们现在还没有创建这些文件。

## 三、 创建HTML页面文件

在项目根路径的login目录中创建一个templates目录，再在templates目录里创建一个login目录。这么做有助于app复用，防止命名冲突，能更有效地组织大型工程，具体说明请参考教程前面的相关章节。

在`login/templates/login`目录中创建三个文件`index.html`、`login.html`以及`register.html` ，并写入如下的代码：

**index.html:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>首页</title>
</head>
<body>
<h1>这仅仅是一个主页模拟！请根据实际情况接入正确的主页！</h1>
</body>
</html>
```

**login.html:**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录</title>
</head>
<body>
<h1>登录页面</h1>
</body>
</html>
```

**register.html**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>注册</title>
</head>
<body>
<h1>注册页面</h1>
</body>
</html>
```

到目前为止，我们的工程目录结构如下图所示：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-a55adfff61d38e3c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 四、 测试路由和视图

启动服务器，在浏览器访问`http://127.0.0.1:8000/index/`等页面，如果能正常显示，说明一切OK！

![image.png](https://upload-images.jianshu.io/upload_images/2458108-ba1546229bdd3330.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

现在，我们整个项目的基本框架已经搭建起来了！



# 5. 前端页面设计



------

基本框架搭建好了后，我们就要开始丰富页面内容了。最起码，得有一个用户登录的表单不是么？（注册的事情我们先放一边。）

## 一、 使用原生HTML页面

删除原来的`login.html`文件中的内容，写入下面的代码：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录</title>
</head>
<body>

    <div style="margin: 15% 40%;">
        <h1>欢迎登录！</h1>
       <form action="/login/" method="post">
            <p>
                <label for="id_username">用户名：</label>
                <input type="text" id="id_username" name="username" placeholder="用户名" autofocus required />
            </p>
            <p>
                <label for="id_password">密码：</label>
                <input type="password" id="id_password" placeholder="密码" name="password" required >
            </p>
            <input type="submit" value="确定">
        </form>
    </div>

</body>
</html>
```

简单解释一下：

- form标签主要确定目的地url和发送方法；
- p标签将各个输入框分行；
- label标签为每个输入框提供一个前导提示，还有助于触屏使用；
- placeholder属性为输入框提供占位符；
- autofocus属性为用户名输入框自动聚焦
- required表示该输入框必须填写
- passowrd类型的input标签不会显示明文密码

以上功能都是HTML5原生提供的，可以减少你大量的验证和JS代码，更详细的用法，请自行学习。

**特别声明：所有前端的验证和安全机制都是不可信的，恶意分子完全可以脱离浏览器伪造请求数据！**

启动服务器，访问`http://127.0.0.1:8000/login/`，可以看到如下图的页面：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-f6bf0c4903f79b93.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 二、引入Bootstrap 4

如果你的实际项目真的使用上面的那个页面外观，妥妥的被老板打死。代码虽然简单，速度虽然快，但没有CSS和JS，样子真的令人无法接受，在颜值即正义的年代，就是错误。

然而，大多数使用Django的人都不具备多高的前端水平，通常也没有专业的前端工程师配合，自己写的CSS和JS却又往往惨不忍睹。怎么办？没关系，我们有现成的开源前端CSS框架！Bootstrap4就是最好的CSS框架之一！

想要在HTML页面中使用Bootstrap4，最方便的方法就是使用国内外的免费CDN（如果app的使用环境不可以使用外部网络，也可以使用内部的CDN，或者静态文件）。

这里推荐BootCDN：https://www.bootcdn.cn/，速度比较快，有大量的不同版本的CDN。

![image.png](https://upload-images.jianshu.io/upload_images/2458108-0097aefe1d470711.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

这里直接给出HTML标签，复制粘贴即可：

```html
CSS：

<link href="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">

以及JS：

<script src="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
```

由于Bootstrap依赖JQuery，所以我们也需要使用CDN引用JQuery 3.3.1:

```html
<script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
```

另外，从Bootstrap4开始，额外需要popper.js的支持，依旧使用CDN的方式引入:

```html
<script src="https://cdn.bootcss.com/popper.js/1.15.0/umd/popper.js"></script>
```

下面，我们就可以创建一个漂亮美观的登录页面了，具体代码如下：

```html
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- 上述meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <!-- Bootstrap CSS -->
    <link href="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <title>登录</title>
  </head>
  <body>
    <div class="container">
            <div class="col">
              <form class="form-login" action="/login/" method="post">
                  <h3 class="text-center">欢迎登录</h3>
                  <div class="form-group">
                    <label for="id_username">用户名：</label>
                    <input type="text" name='username' class="form-control" id="id_username" placeholder="Username" autofocus required>
                  </div>
                  <div class="form-group">
                    <label for="id_password">密码：</label>
                    <input type="password" name='password' class="form-control" id="id_password" placeholder="Password" required>
                  </div>
                <div>
                  <a href="/register/" class="text-success "><ins>新用户注册</ins></a>
                  <button type="submit" class="btn btn-primary float-right">登录</button>
                </div>
              </form>
            </div>
    </div> <!-- /container -->

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    {#    以下三者的引用顺序是固定的#}
    <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
    <script src="https://cdn.bootcss.com/popper.js/1.15.0/umd/popper.js"></script>
    <script src="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>

  </body>
</html>
```

访问一下login页面，看起来如下：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-0751ec298a99a6c4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 三、添加静态文件

然而，上面的登录页面在宽度上依然不太合适，背景也单调，所以一般我们会写一些CSS代码，同时使用背景图片。

在工程根目录下的login目录下，新建一个static目录，再到static目录里创建一个login目录，这种目录的创建方式和模板文件templates的创建方式都是一样的思维，也就是让重用app变得可能，并且不和其它的app发生文件路径和名称上的冲突。

继续在`/login/static/login`目录下创建一个css和一个image目录，css中添加我们为登录视图写的css文件，这里是`login.css`，image目录中，拷贝进来你想要的背景图片，这里是`bg.jpg`。最终目录结构如下：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-066cf8447b3142b7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

下面我们修改一下login.html的代码，主要是引入了login.css文件，注意最开头的`{% load static %}`，表示我们要加载静态文件。

```html
{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- 上述meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <!-- Bootstrap CSS -->
    <link href="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <link href="{% static 'login/css/login.css' %}" rel="stylesheet"/>
    <title>登录</title>
  </head>
  <body>
    <div class="container">
            <div class="col">
              <form class="form-login" action="/login/" method="post">
                  <h3 class="text-center">欢迎登录</h3>
                  <div class="form-group">
                    <label for="id_username">用户名：</label>
                    <input type="text" name='username' class="form-control" id="id_username" placeholder="Username" autofocus required>
                  </div>
                  <div class="form-group">
                    <label for="id_password">密码：</label>
                    <input type="password" name='password' class="form-control" id="id_password" placeholder="Password" required>
                  </div>
                  <div>
                  <a href="/register/" class="text-success "><ins>新用户注册</ins></a>
                  <button type="submit" class="btn btn-primary float-right">登录</button>
                  </div>
              </form>
            </div>
    </div> <!-- /container -->

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    {#    以下三者的引用顺序是固定的#}
    <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
    <script src="https://cdn.bootcss.com/popper.js/1.15.0/umd/popper.js"></script>
    <script src="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>

  </body>
</html>
```

而login.css文件的代码如下，注意其中背景图片bg.jpg的引用方式：

```css
body {
  height: 100%;
  background-image: url('../image/bg.jpg');
}
.form-login {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
}
.form-login{
  margin-top:80px;
  font-weight: 400;
}
.form-login .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;

}
.form-login .form-control:focus {
  z-index: 2;
}
.form-login input[type="text"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-login input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
form a{
  display: inline-block;
  margin-top:25px;
  font-size: 12px;
  line-height: 10px;
}
```

好了，现在可以重启服务器，刷新登录页面，看看效果了：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-9f00841483c42b35.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

以上关于前端的相关内容，实在难以一言述尽，需要大家具备一定的基础。做Django开发，其实就是全栈开发，没有一定的前端能力，很难做好。前端知识薄弱的同学，可以考虑我的前端视频教程，浅显易懂，不会太难太深入，那是前端工程师的要求；也不会太简单，足以应付Django的前端开发需求。

# 6. 登录视图



------

数据模型和前端页面我们都已经设计好了，是时候开始完善我们的登录视图具体内容了。

## 一、登录视图

根据我们在路由中的设计，用户通过`login.html`中的表单填写用户名和密码，并以POST的方式发送到服务器的`/login/`地址。服务器通过`login/views.py`中的`login()`视图函数，接收并处理这一请求。

我们可以通过下面的方法接收和处理请求：

```python
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        return redirect('/index/')
    return render(request, 'login/login.html')
```

说明：

- 每个视图函数都至少接收一个参数，并且是第一位置参数，该参数封装了当前请求的所有数据；
- 通常将第一参数命名为request，当然也可以是别的；
- `request.method`中封装了数据请求的方法，如果是“POST”（全大写），将执行if语句的内容，如果不是，直接返回最后的render()结果，也就是正常的登录页面；
- `request.POST`封装了所有POST请求中的数据，这是一个字典类型，可以通过get方法获取具体的值。
- 类似`get('username')`中的键‘username’是HTML模板中表单的input元素里‘name’属性定义的值。所以在编写form表单的时候一定不能忘记添加name属性。
- 利用print函数在开发环境中验证数据；
- 利用redirect方法，将页面重定向到index页。

启动服务器，然后在`http://127.0.0.1:8000/login/`的表单中随便填入用户名和密码，然后点击提交。然而，页面却出现了错误提示，如下图所示：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-7d83398e9bb3a1df.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

错误原因是CSRF验证失败，请求被中断。CSRF（Cross-site request forgery）跨站请求伪造，是一种常见的网络攻击手段，具体原理和技术内容请自行百科。Django自带对许多常见攻击手段的防御机制，CSRF就是其中一种，还有XSS、SQL注入等。

解决这个问题的办法其实在Django的Debug错误页面已经给出了，我们需要在前端页面的form表单内添加一个`{% csrf_token %}`标签：

```python
                <form class="form-login" action="/login/" method="post">
                  {% csrf_token %}
                  <h3 class="text-center">欢迎登录</h3>
                  <div class="form-group">
                    <label for="id_username">用户名：</label>
                    <input type="text" name='username' class="form-control" id="id_username" placeholder="Username" autofocus required>
                  </div>
                  <div class="form-group">
                    <label for="id_password">密码：</label>
                    <input type="password" name='password' class="form-control" id="id_password" placeholder="Password" required>
                  </div>
                  <div>
                  <a href="/register/" class="text-success " ><ins>新用户注册</ins></a>
                  <button type="submit" class="btn btn-primary float-right">登录</button>
                  </div>
                </form>
```

这个标签必须放在form表单内部，但是内部的位置可以随意。

重新刷新login页面，确保csrf的标签生效，然后再次输入内容并提交。这次就可以成功地在Pycharm开发环境中看到接收的用户名和密码，同时浏览器页面也跳转到了首页。

## 二、数据验证

前面我们提到过，要对用户发送的数据进行验证。数据验证分前端页面验证和后台服务器验证。前端验证可以通过专门的插件或者自己写JS代码实现，也可以简单地使用HTML5的新特性。这里，我们使用的是HTML5的内置验证功能，如下图所示：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-d0c341069e52656d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

它帮我们实现了下面的功能：

- 用户名和密码这类必填字段不能为空
- 密码部分用圆点替代

如果你还想要更强大和丰富的验证功能，比如限定密码长度不低于8位，用户名不能包含特殊字符等等，可以搜索并使用一些插件。

前端页面的验证都是用来给守法用户做提示和限制的，并不能保证绝对的安全，后端服务器依然要重新对数据进行验证。我们现在的视图函数，没有对数据进行任何的验证，如果你在用户名处输入个空格，是可以正常提交的，但这显然是不允许的。甚至，如果跳过浏览器伪造请求，那么用户名是None也可以发送过来。通常，除了数据内容本身，我们至少需要保证各项内容都提供了且不为空，对于用户名、邮箱、地址等内容往往还需要剪去前后的空白，防止用户未注意到的空格。

现在，让我们修改一下前面的代码：

```python
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username.strip() and password:  # 确保用户名和密码都不为空      
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            return redirect('/index/')
    return render(request, 'login/login.html')
```

- get方法是Python字典类型的内置方法，它能够保证在没有指定键的情况下，返回一个None，从而确保当数据请求中没有username或password键时不会抛出异常；
- 通过`if username and password:`确保用户名和密码都不为空；
- 通过strip方法，将用户名前后无效的空格剪除；
- 更多的数据验证需要根据实际情况增加，原则是以最低的信任度对待发送过来的数据。

## 三、验证用户名和密码

数据形式合法性验证通过了，不代表用户就可以登录了，因为最基本的密码对比还未进行。

通过唯一的用户名，使用Django的ORM去数据库中查询用户数据，如果有匹配项，则进行密码对比，如果没有匹配项，说明用户名不存在。如果密码对比错误，说明密码不正确。

下面贴出当前状态下，/login/views.py中的全部代码，注意其中添加了一句`from . import models`，导入我们先前编写好的model模型。

```python
from django.shortcuts import render
from django.shortcuts import redirect
from . import models
# Create your views here.


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username.strip() and password:  # 确保用户名和密码都不为空
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name=username)
            except:
                return render(request, 'login/login.html')
            if user.password == password:
                return redirect('/index/')
    return render(request, 'login/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect("/login/")
```

说明：

- 首先要在顶部导入models模块；
- 使用try异常机制，防止数据库查询失败的异常；
- 如果未匹配到用户，则执行except中的语句；注意这里没有区分异常的类型，因为在数据库访问过程中，可能发生很多种类型的异常，我们要对用户屏蔽这些信息，不可以暴露给用户，而是统一返回一个错误提示，比如用户名不存在。这是大多数情况下的通用做法。当然，如果你非要细分，也不是不行。
- `models.User.objects.get(name=username)`是Django提供的最常用的数据查询API，具体含义和用法可以阅读前面的章节，不再赘述；
- 通过`user.password == password`进行密码比对，成功则跳转到index页面，失败则返回登录页面。

重启服务器，然后在登录表单内，使用错误的用户名和密码，以及我们先前在admin中创建的合法的测试用户，分别登录，看看效果。

## 四、 添加提示信息

上面的代码还缺少很重要的一部分内容，也就是错误提示信息！无论是登录成功还是失败，用户都没有得到任何提示信息，这显然是不行的。

修改一下login视图：

```python
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = '请检查填写的内容！'
        if username.strip() and password:
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                user = models.User.objects.get(name=username)
            except :
                message = '用户不存在！'
                return render(request, 'login/login.html', {'message': message})

            if user.password == password:
                print(username, password)
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', {'message': message})
        else:
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/login.html')
```

请仔细分析一下上面的登录和密码验证逻辑，以及错误提示的安排。

这里增加了message变量，用于保存提示信息。当有错误信息的时候，将错误信息打包成一个字典，然后作为第三个参数提供给render方法。这个数据字典在渲染模板的时候会传递到模板里供你调用。

为了在前端页面显示信息，还需要对`login.html`进行修改：

```html
<form class="form-login" action="/login/" method="post">
                  {% if message %}
                    <div class="alert alert-warning">{{ message }}</div>
                  {% endif %}
                  {% csrf_token %}
                  <h3 class="text-center">欢迎登录</h3>
                  <div class="form-group">
                    <label for="id_username">用户名：</label>
                    <input type="text" name='username' class="form-control" id="id_username" placeholder="Username" autofocus required>
                  </div>
                  <div class="form-group">
                    <label for="id_password">密码：</label>
                    <input type="password" name='password' class="form-control" id="id_password" placeholder="Password" required>
                  </div>
                  <div>
                  <a href="/register/" class="text-success " ><ins>新用户注册</ins></a>
                  <button type="submit" class="btn btn-primary float-right">登录</button>
                  </div>
                </form>
```

Django的模板语言`{% if xxx %}{% endif %}`非常类似Python的if语句，也可以添加`{% else %}`分句。例子中，通过判断message变量是否为空，也就是是否有错误提示信息，如果有，就显示出来！这里使用了Bootstrap的警示信息类alert，你也可以自定义CSS或者JS。

好了，重启服务器，尝试用错误的和正确的用户名及密码登录，看看页面效果吧！下面是错误信息的展示：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-be4a23009e6c1458.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/2458108-347e4ab836fe64af.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/2458108-51c554cf3cd041e4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

# 7. Django表单

------

我们前面都是手工在HTML文件中编写表单form元素，然后在views.py的视图函数中接收表单中的用户数据，再编写验证代码进行验证，最后使用ORM进行数据库的增删改查。这样费时费力，整个过程比较复杂，而且有可能写得不太恰当，数据验证也比较麻烦。设想一下，如果我们的表单拥有几十上百个数据字段，有不同的数据特点，如果也使用手工的方式，其效率和正确性都将无法得到保障。有鉴于此，Django在内部集成了一个表单功能，以面向对象的方式，直接使用Python代码生成HTML表单代码，专门帮助我们快速处理表单相关的内容。

Django的表单给我们提供了下面三个主要功能：

- 准备和重构数据用于页面渲染；
- 为数据创建HTML表单元素；
- 接收和处理用户从表单发送过来的数据。

编写Django的form表单，非常类似我们在模型系统里编写一个模型。在模型中，一个字段代表数据表的一列，而form表单中的一个字段代表`<form>`中的一个`<input>`元素。

## 一、创建表单模型

在项目根目录的login文件夹下，新建一个`forms.py`文件，也就是`/login/forms.py`，又是我们熟悉的Django组织文件的套路，一个app一套班子！

在`/login/forms.py`中写入下面的代码，是不是有一种编写数据model模型的既视感？

```python
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128)
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)
```

说明：

- 顶部要先导入forms模块
- 所有的表单类都要继承forms.Form类
- 每个表单字段都有自己的字段类型比如CharField，它们分别对应一种HTML语言中`<form>`内的一个input元素。这一点和Django模型系统的设计非常相似。
- label参数用于设置`<label>`标签
- `max_length`限制字段输入的最大长度。它同时起到两个作用，一是在浏览器页面限制用户输入不可超过字符数，二是在后端服务器验证用户输入的长度也不可超过。
- `widget=forms.PasswordInput`用于指定该字段在form表单里表现为`<input type='password' />`，也就是密码输入框。

## 二、修改视图

使用了Django的表单后，就要在视图中进行相应的修改：

```python
# login/views.py

from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
# Create your views here.


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except :
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())

            if user.password == password:
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect("/login/")
```

说明：

- 在顶部要导入我们写的forms模块:`from . import forms`
- 对于非POST方法发送数据时，比如GET方法请求页面，返回空的表单，让用户可以填入数据；
- 对于POST方法，接收表单数据，并验证；
- 使用表单类自带的`is_valid()`方法一步完成数据验证工作；
- 验证成功后可以从表单对象的`cleaned_data`数据字典中获取表单的具体值；
- 如果验证不通过，则返回一个包含先前数据的表单给前端页面，方便用户修改。也就是说，它会帮你保留先前填写的数据内容，而不是返回一个空表！

另外，这里使用了一个小技巧，Python内置了一个locals()函数，它返回当前所有的本地变量字典，我们可以偷懒的将这作为render函数的数据字典参数值，就不用费劲去构造一个形如`{'message':message, 'login_form':login_form}`的字典了。这样做的好处当然是大大方便了我们，但是同时也可能往模板传入了一些多余的变量数据，造成数据冗余降低效率。

## 三、 修改login页面

Django的表单很重要的一个功能就是自动生成HTML的form表单内容。现在，我们需要修改一下原来的`login.html`文件：

```html
{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- 上述meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <!-- Bootstrap CSS -->
    <link href="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <link href="{% static 'login/css/login.css' %}" rel="stylesheet"/>
    <title>登录</title>
  </head>
  <body>
    <div class="container">
            <div class="col">
                <form class="form-login" action="/login/" method="post">
                  {% if message %}
                    <div class="alert alert-warning">{{ message }}</div>
                  {% endif %}
                  {% csrf_token %}
                  <h3 class="text-center">欢迎登录</h3>

                  {{ login_form }}

                  <div>
                      <a href="/register/" class="text-success " ><ins>新用户注册</ins></a>
                      <button type="submit" class="btn btn-primary float-right">登录</button>
                  </div>
                </form>
            </div>
    </div> <!-- /container -->

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    {#    以下三者的引用顺序是固定的#}
    <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
    <script src="https://cdn.bootcss.com/popper.js/1.15.0/umd/popper.js"></script>
    <script src="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>

  </body>
</html>
```

上面贴了一个完整版的代码，方便大家对比参考。

说明：

- 你没有看错！一个`{{ login_form }}`就直接完成了表单内容的生成工作！`login_form`这个名称来自你在视图函数中生成的form实例的变量名！
- 但是，它不会生成`<form>...</form>`标签，这个要自己写；
- 使用POST的方法时，必须添加`{% csrf_token %}`标签，用于处理csrf安全机制；
- Django自动为每个input元素设置了一个id名称，对应label的for参数
- 注册链接和登录按钮需要自己写，Django不会帮你生成！

我们到浏览器中，看下实际生成的html源码是什么：

```html
<form class="form-login" action="/login/" method="post"> 

  <input type="hidden" name="csrfmiddlewaretoken" value="5oJMX0z8PkUXY7RPDPGjaD2Q28CndXKeKWlftJD6s0XM1NIUEi7a0iET1NCYikUw"> 
  <h3 class="text-center">欢迎登录</h3>

  <tr><th><label for="id_username">用户名:</label></th><td><input type="text" name="username" maxlength="128" required id="id_username"></td></tr> 
  <tr><th><label for="id_password">密码:</label></th><td><input type="password" name="password" maxlength="256" required id="id_password"></td></tr> 
  <div> 
    <a href="[/register/](http://127.0.0.1:8000/register/)" class="text-success " ><ins>新用户注册</ins></a> 
    <button type="submit" class="btn btn-primary float-right">登录</button>
  </div> 
</form> 
```

也就是说，Django的form表单功能，帮你自动生成了下面部分的代码：

```html
<tr><th><label for="id_username">用户名:</label></th><td><input type="text" name="username" maxlength="128" required id="id_username"></td></tr> 
  <tr><th><label for="id_password">密码:</label></th><td><input type="password" name="password" maxlength="256" required id="id_password"></td></tr> 
```

这看起来好像一个`<table>`标签啊？没错，就是`<table>`标签，而且是不带`<table></table>`的，捂脸！

实际上除了通过`{{ login_form }}`简单地将表单渲染到HTML页面中了，还有下面几种方式：

- `{{ login_form.as_table }}` 将表单渲染成一个表格元素，每个输入框作为一个`<tr>`标签
- `{{ login_form.as_p }}` 将表单的每个输入框包裹在一个`<p>`标签内
- `{{ login_form.as_ul }}` 将表单渲染成一个列表元素，每个输入框作为一个`<li>`标签

注意：上面的渲染方法中都要自己手动编写`<table>`或者`<ul>`标签。

重新启动服务器，刷新页面，如下图所示：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-a71d783b2bdba74f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 四、手动渲染表单字段

直接`{{ login_form }}`虽然好，啥都不用操心，但是界面真的很丑，并且我们先前使用的Bootstraps4都没了。因为这些都需要对表单内的input元素进行额外控制，那怎么办呢？手动渲染字段就可以了！

可以通过`{{ login_form.name_of_field }}`获取每一个字段，然后分别渲染，如下例所示：

```html
<div class="form-group">
  {{ login_form.username.label_tag }}
  {{ login_form.username}}
</div>
<div class="form-group">
  {{ login_form.password.label_tag }}
  {{ login_form.password }}
</div>
```

其中的label标签可以用`label_tag`方法来生成。这样子更加灵活了,但是灵活的代价就是我们要写更多的代码，又偏向原生的HTML代码多了一点。

但是问题又...又...又来了！刷新登录页面，却是下图的样子：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-37804bd1780b6fe3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

好像Bootstrap4没有生效呀！仔细查看最终生成的页面源码，你会发现，input元素里少了`form-control`的class，以及placeholder和autofocus，这可咋办？

在form类里添加attr属性即可，如下所示修改`login/forms.py`

```python
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username",'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': "Password"}))
```

再次刷新页面，我们熟悉的Bootstrap4框架UI又回来了！

![image.png](https://upload-images.jianshu.io/upload_images/2458108-77c2a4628fab3c53.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

实际上，Django针对`{{ login_form }}`表单，提供了很多灵活的模板语法，可以循环，可以取值，可以针对可见和不可见的部分单独控制，详细内容可以参考教程前面的章节。



# 8. 图片验证码

阅读: 19544

------

为了防止机器人频繁登录网站或者破坏分子恶意登录，很多用户登录和注册系统都提供了图形验证码功能。

验证码（CAPTCHA）是“Completely Automated Public Turing test to tell Computers and Humans Apart”（全自动区分计算机和人类的图灵测试）的缩写，是一种区分用户是计算机还是人的公共全自动程序。可以防止恶意破解密码、刷票、论坛灌水，有效防止某个黑客对某一个特定注册用户用特定程序暴力破解方式进行不断的登陆尝试。

图形验证码的历史比较悠久，到现在已经有点英雄末路的味道了。因为机器学习、图像识别的存在，机器人已经可以比较正确的识别图像内的字符了。但不管怎么说，作为一种防御手段，至少还是可以抵挡一些低级入门的攻击手段，抬高了攻击者的门槛。

在Django中实现图片验证码功能非常简单，有现成的第三方库可以使用，我们不必自己开发（也要能开发得出来，囧）。这个库叫做`django-simple-captcha`。

## 一、安装captcha

在Pycharm的terminal中，使用pip安装第三方库：

```python
执行命令：pip install django-simple-captcha
(venv) D:\work\2019\for_test\mysite>pip install django-simple-captcha
Collecting django-simple-captcha
  Downloading https://files.pythonhosted.org/packages/86/d4/5baf10bfc9eb7844872c256898a405e81f22f7213e008ec90875689f913d/django-simple-captcha-0
.5.11.zip (234kB)
    100% |████████████████████████████████| 235kB 596kB/s
Collecting six>=1.2.0 (from django-simple-captcha)
  Downloading https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none
-any.whl
Requirement already satisfied: Django>=1.8 in d:\work\2019\for_test\mysite\venv\lib\site-packages (from django-simple-captcha) (2.2)
Collecting Pillow!=5.1.0,>=2.2.2 (from django-simple-captcha)
  Downloading https://files.pythonhosted.org/packages/40/f2/a424d4d5dd6aa8c26636969decbb3da1c01286d344e71429b1d648bccb64/Pillow-6.0.0-cp37-cp37m
-win_amd64.whl (2.0MB)
    100% |████████████████████████████████| 2.0MB 2.2MB/s
Collecting django-ranged-response==0.2.0 (from django-simple-captcha)
  Downloading https://files.pythonhosted.org/packages/70/e3/9372fcdca8e9c3205e7979528ccd1a14354a9a24d38efff11c1846ff8bf1/django-ranged-response-
0.2.0.tar.gz
Requirement already satisfied: sqlparse in d:\work\2019\for_test\mysite\venv\lib\site-packages (from Django>=1.8->django-simple-captcha) (0.3.0)

Requirement already satisfied: pytz in d:\work\2019\for_test\mysite\venv\lib\site-packages (from Django>=1.8->django-simple-captcha) (2018.9)
Installing collected packages: six, Pillow, django-ranged-response, django-simple-captcha
  Running setup.py install for django-ranged-response ... done
  Running setup.py install for django-simple-captcha ... done
Successfully installed Pillow-6.0.0 django-ranged-response-0.2.0 django-simple-captcha-0.5.11 six-1.12.0
```

pip自动帮我们安装了相关的依赖库`six`、`olefile`和`Pillow`，其中的Pillow是大名鼎鼎的绘图模块。

## 二、注册captcha

在settings中，将‘captcha’注册到app列表里：

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'captcha',
]
```

captcha需要在数据库中建立自己的数据表，所以需要执行migrate命令生成数据表：

```python
(venv) D:\work\2019\for_test\mysite>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, captcha, contenttypes, login, sessions
Running migrations:
  Applying captcha.0001_initial... OK
```

## 三、添加url路由

在根目录下的urls.py文件中增加captcha对应的url：

```python
from django.contrib import admin
from django.urls import path
from django.urls import include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('captcha/', include('captcha.urls'))   # 增加这一行
]
```

由于使用了二级路由机制，需要在顶部`from django.urls import include`。

## 四、修改forms.py

如果上面都OK了，就可以直接在我们的forms.py文件中添加CaptchaField了。

```python
from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username",'autofocus': ''}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control',  'placeholder': "Password"}))
    captcha = CaptchaField(label='验证码')
```

注意需要提前导入`from captcha.fields import CaptchaField`，然后就像写普通的form字段一样添加一个captcha字段就可以了！

## 五、修改login.html

由于我们前面是手动生成的form表单，所以还要修改一下，添加captcha的相关内容，如下所示：

```html
{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- 上述meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <!-- Bootstrap CSS -->
    <link href="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <link href="{% static 'login/css/login.css' %}" rel="stylesheet"/>
    <title>登录</title>
  </head>
  <body>
    <div class="container">
            <div class="col">
                <form class="form-login" action="/login/" method="post">

                {% if login_form.captcha.errors %}
                    <div class="alert alert-warning">{{ login_form.captcha.errors }}</div>
                {% elif message %}
                    <div class="alert alert-warning">{{ message }}</div>
                {% endif %}

                  {% csrf_token %}
                  <h3 class="text-center">欢迎登录</h3>

                  <div class="form-group">
                    {{ login_form.username.label_tag }}
                    {{ login_form.username}}
                  </div>

                  <div class="form-group">
                    {{ login_form.password.label_tag }}
                    {{ login_form.password }}
                  </div>

                  <div class="form-group">
                    {{ login_form.captcha.label_tag }}
                    {{ login_form.captcha }}
                  </div>

                  <div>
                      <a href="/register/" class="text-success " ><ins>新用户注册</ins></a>
                      <button type="submit" class="btn btn-primary float-right">登录</button>
                  </div>
                </form>
            </div>
    </div> <!-- /container -->

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    {#    以下三者的引用顺序是固定的#}
    <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
    <script src="https://cdn.bootcss.com/popper.js/1.15.0/umd/popper.js"></script>
    <script src="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>

  </body>
</html>
```

这里在顶部的消息处，在`{% if %}`模板代码中，额外增加了一条`{{ login_form.captcha.errors }}`的判断，用于明确指示用户的验证码不正确。

## 六、查看效果

重启服务器，进入登录页面，尝试用用户名错误、密码不对、验证码不对、全对的不同情况，看看我们新增的四位验证码的效果如何。

![image.png](https://upload-images.jianshu.io/upload_images/2458108-41198e8de78fc6e6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/2458108-6cc96081452ce017.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

就是这么简单！我们加入了一个防止机器人或者恶意登录的图形验证码功能，虽然界面难看了点，但底子是好的，你可以根据需要进行美化。其中验证图形码是否正确的工作都是在后台自动完成的，只需要使用`is_valid()`这个forms内置的验证方法就一起进行了，完全不需要在视图函数中添加任何的验证代码，非常方便快捷！

关于captcha的功能，当然绝不仅限于此，你可以设置六位、八位验证码，可以对图形噪点的生成模式进行定制，这些就留待你自己学习和研究了。

# 9. session会话

------

因为因特网HTTP协议的特性，每一次来自于用户浏览器的请求（request）都是无状态的、独立的。通俗地说，就是无法保存用户状态，后台服务器根本就不知道当前请求和以前及以后请求是否来自同一用户。对于静态网站，这可能不是个问题，而对于动态网站，尤其是京东、天猫、银行等购物或金融网站，无法识别用户并保持用户状态是致命的，根本就无法提供服务。你可以尝试将浏览器的cookie功能关闭，你会发现将无法在京东登录和购物。

为了实现连接状态的保持功能，网站会通过用户的浏览器在用户机器内被限定的硬盘位置中写入一些数据，也就是所谓的Cookie。通过Cookie可以保存一些诸如用户名、浏览记录、表单记录、登录和注销等各种数据。但是这种方式非常不安全，因为Cookie保存在用户的机器上，如果Cookie被伪造、篡改或删除，就会造成极大的安全威胁，因此，现代网站设计通常将Cookie用来保存一些不重要的内容，实际的用户数据和状态还是以Session会话的方式保存在服务器端。

但是，必须清楚的是**Session依赖Cookie**！不同的地方在于Session将所有的数据都放在服务器端，用户浏览器的Cookie中只会保存一个非明文的识别信息，比如哈希值。

Django提供了一个通用的Session框架，并且可以使用多种session数据的保存方式：

- 保存在数据库内
- 保存到缓存
- 保存到文件内
- 保存到cookie内

通常情况，没有特别需求的话，请使用保存在数据库内的方式，尽量不要保存到Cookie内。

Django的session框架默认启用，并已经注册在app设置内，如果真的没有启用，那么参考下面的内容添加有说明的那两行，再执行migrate命令创建数据表，就可以使用session了。

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',    # 这一行
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # 这一行
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

当session启用后，传递给视图request参数的HttpRequest对象将包含一个session属性，就像一个字典对象一样。你可以在Django的任何地方读写`request.session`属性，或者多次编辑使用它。

下面是session使用参考：

```python
class backends.base.SessionBase
        # 这是所有会话对象的基类，包含标准的字典方法:
        __getitem__(key)
            Example: fav_color = request.session['fav_color']
        __setitem__(key, value)
            Example: request.session['fav_color'] = 'blue'
        __delitem__(key)
            Example: del request.session['fav_color']  # 如果不存在会抛出异常
        __contains__(key)
            Example: 'fav_color' in request.session
        get(key, default=None)
            Example: fav_color = request.session.get('fav_color', 'red')
        pop(key, default=__not_given)
            Example: fav_color = request.session.pop('fav_color', 'blue')
        # 类似字典数据类型的内置方法
        keys()
        items()
        setdefault()
        clear()


        # 它还有下面的方法：
        flush()
            # 删除当前的会话数据和会话cookie。经常用在用户退出后，删除会话。

        set_test_cookie()
            # 设置一个测试cookie，用于探测用户浏览器是否支持cookies。由于cookie的工作机制，你只有在下次用户请求的时候才可以测试。
        test_cookie_worked()
            # 返回True或者False，取决于用户的浏览器是否接受测试cookie。你必须在之前先调用set_test_cookie()方法。
        delete_test_cookie()
            # 删除测试cookie。
        set_expiry(value)
            # 设置cookie的有效期。可以传递不同类型的参数值：
        • 如果值是一个整数，session将在对应的秒数后失效。例如request.session.set_expiry(300) 将在300秒后失效.
        • 如果值是一个datetime或者timedelta对象, 会话将在指定的日期失效
        • 如果为0，在用户关闭浏览器后失效
        • 如果为None，则将使用全局会话失效策略
        失效时间从上一次会话被修改的时刻开始计时。

        get_expiry_age()
            # 返回多少秒后失效的秒数。对于没有自定义失效时间的会话，这等同于SESSION_COOKIE_AGE.
            # 这个方法接受2个可选的关键字参数
        • modification:会话的最后修改时间（datetime对象）。默认是当前时间。
        •expiry: 会话失效信息，可以是datetime对象，也可以是int或None

        get_expiry_date()
            # 和上面的方法类似，只是返回的是日期

        get_expire_at_browser_close()
            # 返回True或False，根据用户会话是否是浏览器关闭后就结束。

        clear_expired()
            # 删除已经失效的会话数据。
        cycle_key()
            # 创建一个新的会话秘钥用于保持当前的会话数据。django.contrib.auth.login() 会调用这个方法。
```

基本上背下来上面的内容，Django的session你就可以信手拈来了。

## 一、使用session

下面结合我们的项目实战，使用session。

首先，修改`login/views.py`中的login()视图函数：

```python
def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except :
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())
```

通过下面的if语句，我们不允许重复登录：

```python
if request.session.get('is_login',None):
    return redirect("/index/")
```

通过下面的语句，我们往session字典内写入用户状态和数据：

```python
request.session['is_login'] = True
request.session['user_id'] = user.id
request.session['user_name'] = user.name
```

你完全可以往里面写任何数据，不仅仅限于用户相关！

既然有了session记录用户登录状态，那么就可以完善我们的登出视图函数了：

```python
def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")
```

flush()方法是比较安全的一种做法，而且一次性将session中的所有内容全部清空，确保不留后患。但也有不好的地方，那就是如果你在session中夹带了一点‘私货’，会被一并删除，这一点一定要注意。

## 二、在index页面中验证登录

有了用户状态，就可以根据用户登录与否，展示不同的页面，比如在index页面中显示当前用户的名称：

修改index.html的代码：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>首页</title>
</head>
<body>
<h1>{{ request.session.user_name }}!  欢迎回来！</h1>
<p>
    <a href="/logout/">登出</a>
</p>
</body>
</html>
```

注意其中的模板语言，`{{ request }}`这个变量会被默认传入模板中，可以通过圆点的调用方式，获取它内部的`{{ request.session }}`，再进一步的获取session中的内容。其实`{{ request }}`中的数据远不止此，例如`{{ request.path }}`就可以获取先前的url地址。

重新启动服务器，进行登录和登出测试：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-c5070ae65bf2c842.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

可以看出，在已经login的状态下，手动从浏览器地址栏中访问/login/也依然进入的是index页面。在logout的状态下，都会跳转到login页面。但是，需要注意的是，我们目前还没有编写index未登录限制访问的代码。

修改index视图函数，添加相关限制：

```python
def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index.html')
```



# 10. 注册视图



------

前面我们已经完成了项目大部分内容，现在还剩下重要的注册功能没有实现。

## 一、创建forms

显而易见，我们的注册页面也需要一个form表单。同样地，在`/login/forms.py`中添加一个新的表单类：

```python
class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
    captcha = CaptchaField(label='验证码')
```

说明：

- gender字典和User模型中的一样，其实可以拉出来作为常量共用，为了直观，特意重写一遍；
- password1和password2，用于输入两遍密码，并进行比较，防止误输密码；
- email是一个邮箱输入框；
- sex是一个select下拉框；
- 没有添加更多的input属性

## 二、完善register.html

同样地，类似login.html文件，我们手工在register.html中编写forms相关条目：

```html
{% load static %}
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- 上述meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <!-- Bootstrap CSS -->
    <link href="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <link href="{% static 'login/css/register.css' %}" rel="stylesheet"/>
    <title>注册</title>
  </head>
  <body>
    <div class="container">
            <div class="col">
                <form class="form-register" action="/register/" method="post">

                    {% if register_form.captcha.errors %}
                        <div class="alert alert-warning">{{ register_form.captcha.errors }}</div>
                    {% elif message %}
                        <div class="alert alert-warning">{{ message }}</div>
                    {% endif %}

                  {% csrf_token %}
                  <h3 class="text-center">欢迎注册</h3>

                  <div class="form-group">
                      {{ register_form.username.label_tag }}
                      {{ register_form.username}}
                  </div>
                  <div class="form-group">
                      {{ register_form.password1.label_tag }}
                      {{ register_form.password1 }}
                  </div>
                  <div class="form-group">
                      {{ register_form.password2.label_tag }}
                      {{ register_form.password2 }}
                  </div>
                  <div class="form-group">
                      {{ register_form.email.label_tag }}
                      {{ register_form.email }}
                  </div>
                  <div class="form-group">
                      {{ register_form.sex.label_tag }}
                      {{ register_form.sex }}
                  </div>
                  <div class="form-group">
                      {{ register_form.captcha.label_tag }}
                      {{ register_form.captcha }}
                  </div>

                  <div>
                      <a href="/login/"  ><ins>直接登录</ins></a>
                      <button type="submit" class="btn btn-primary float-right">注册</button>
                  </div>
                </form>
            </div>
    </div> <!-- /container -->

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    {#    以下三者的引用顺序是固定的#}
    <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.js"></script>
    <script src="https://cdn.bootcss.com/popper.js/1.15.0/umd/popper.js"></script>
    <script src="https://cdn.bootcss.com/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>

  </body>
</html>
```

需要注意的是：

- 编写了一个register.css样式文件
- form标签的action地址为`/register/`，class为`form-register`
- from中传递过来的表单变量名字为`register_form`
- 最下面的链接修改为直接登录的链接

register.css样式文件的代码很简单，如下所示：

```html
body {
  height: 100%;
  background-image: url('../image/bg.jpg');
}
.form-register {
  width: 100%;
  max-width: 400px;
  padding: 15px;
  margin: 0 auto;
}
.form-group {
  margin-bottom: 5px;
}
form a{
  display: inline-block;
  margin-top:25px;
  line-height: 10px;
}
```

## 三、实现注册视图

进入`/login/views.py`文件，现在来完善我们的`register()`视图：

```python
def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                return redirect('/login/')
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())
```

从大体逻辑上，也是先实例化一个RegisterForm的对象，然后使用`is_valide()`验证数据，再从`cleaned_data`中获取数据。

重点在于注册逻辑，首先两次输入的密码必须相同，其次不能存在相同用户名和邮箱，最后如果条件都满足，利用ORM的API，创建一个用户实例，然后保存到数据库内。

对于注册的逻辑，不同的生产环境有不同的要求，请跟进实际情况自行完善，这里只是一个基本的注册过程，不能生搬照抄。

让我们看一下注册的页面：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-cd3b51de472fa302.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

你可以尝试用不同的情况进行注册，然后观察错误信息的提示:

![image.png](https://upload-images.jianshu.io/upload_images/2458108-ebdd7a73faee0fad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

最后进行一次成功地注册，会自动跳转到登录页面。我们进入admin后台，查看一下用户列表：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-d21e4ac3e5270ced.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/2458108-3b1bcc162258a758.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 四、密码加密

等等！我们好像忘了什么！我们到现在都还一直在用明文的密码！

对于如何加密密码，有很多不同的途径，其安全程度也高低不等。这里我们使用Python内置的hashlib库，使用哈希值的方式加密密码，可能安全等级不够高，但足够简单，方便使用，不是么？

首先在`login/views.py`中编写一个hash函数：

```
import hashlib

def hash_code(s, salt='mysite'):# 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()
```

使用了sha256算法，加了点盐。具体的内容可以参考站点内的Python教程中hashlib库章节。

然后，我们还要对login()和register()视图进行一下修改：

```python
from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from . import forms
import hashlib
# Create your views here.


def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except :
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())

            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                return redirect('/login/')
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    request.session.flush()
    # del request.session['is_login']
    return redirect("/login/")
```

注意其中关于密码处理的部分！

好了，我们可以来验证一下了!但是，**请先在admin后台里，把我们前面创建的测试用户全部删除！**因为它们的密码没有使用哈希算法加密，已经无效了。

重启服务器，进入注册页面，新建一个用户，然后进入admin后台，查看用户的密码情况：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-95007ac84cdfc2c6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

再使用该用户登录一下，大功告成！

可以看到密码长度根据你哈希算法的不同，已经变得很长了，所以前面model中设置password字段时，不要想当然的将`max_length`设置为16这么小的数字。



# 11.使用Django发送邮件



------

通常而言，我们在用户注册成功，实际登陆之前，会发送一封电子邮件到对方的注册邮箱中，表示欢迎。进一步的还可能要求用户点击邮件中的链接，进行注册确认。

下面就让我们先看看如何在Django中发送邮件吧。

## 一、在Django中发送邮件

其实在Python中已经内置了一个smtp邮件发送模块，Django在此基础上进行了简单地封装。

首先，我们需要在项目的settings文件中配置邮件发送参数，分别如下：

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sina.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'xxx@sina.com'
EMAIL_HOST_PASSWORD = 'xxxxxxxxxxx'
```

- 第一行指定发送邮件的后端模块，大多数情况下照抄！
- 第二行，不用说，发送方的smtp服务器地址，建议使用新浪家的；
- 第三行，smtp服务端口，默认为25；
- 第四行，你在发送服务器的用户名；
- 第五行，对应用户的密码。

特别说明：

- 某些邮件公司可能不开放smtp服务
- 某些公司要求使用ssl安全机制
- 某些smtp服务对主机名格式有要求

这些都是前人踩过的坑。如果你在测试中出现了问题，请不要找Django的麻烦，99%的原因和你的邮件服务有关。

配置好了参数，就可以先测试一下邮件功能了。

在项目根目录下新建一个`send_mail.py`文件，然后写入下面的内容：

```python
import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':   

    send_mail(
        '来自www.liujiangblog.com的测试邮件',
        '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，本站专注于Python、Django和机器学习技术的分享！',
        'xxx@sina.com',
        ['xxx@qq.com'],
    )
```

对于send_mail方法，第一个参数是邮件主题subject；第二个参数是邮件具体内容；第三个参数是邮件发送方，需要和你settings中的一致；第四个参数是接受方的邮件地址列表。请按你自己实际情况修改发送方和接收方的邮箱地址。

另外，由于我们当前是单独运行`send_mail.py`文件，无法自动链接Django环境，需要通过os模块对环境变量进行设置，也就是：

```
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
```

运行`send_mail.py`文件，注意不是运行Django服务器。然后到你的目的地邮箱查看邮件是否收到。

![image.png](https://upload-images.jianshu.io/upload_images/2458108-fb4a21805be13a5d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 二、发送HTML格式的邮件

通常情况下，我们发送的邮件内容都是纯文本格式。但是很多情况下，我们需要发送带有HTML格式的内容，比如说超级链接。一般情况下，为了安全考虑，很多邮件服务提供商都会禁止使用HTML内容，幸运的是对于以`http`和`https`开头的链接还是可以点击的。

下面是发送HTML格式的邮件例子。删除`send_mail.py`原来的所有内容，添加下面的代码：

```python
import os
from django.core.mail import EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自www.liujiangblog.com的测试邮件', 'xxx@sina.com', 'xxx@qq.com'
    text_content = '欢迎访问www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python和Django技术的分享！'
    html_content = '<p>欢迎访问<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>，这里是刘江的博客和教程站点，本站专注于Python、Django和机器学习技术的分享！</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alaternative(html_content, "text/html")
    msg.send()
```

其中的`text_content`是用于当HTML内容无效时的替代txt文本。

打开测试用的接收邮箱，可以看到链接能够正常点击，如下图所示：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-a0acb58dec01d916.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

这个`send_mail.py`文件只是一个测试脚本，使用完毕后可以从项目里删除。

# 12. 邮件注册确认



------

很自然地，我们会想到如果能用邮件确认的方式对新注册用户进行审查，既安全又正式，也是目前很多站点的做法。

## 一、 创建模型

既然要区分通过和未通过邮件确认的用户，那么必须给用户添加一个是否进行过邮件确认的属性。

另外，我们要创建一张新表，用于保存用户的确认码以及注册提交的时间。

全新、完整的`/login/models.py`文件如下：

```python
from django.db import models

# Create your models here.


class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"


class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"
```

说明：

- User模型新增了`has_confirmed`字段，这是个布尔值，默认为False，也就是未进行邮件注册；
- ConfirmString模型保存了用户和注册码之间的关系，一对一的形式；
- code字段是哈希后的注册码；
- user是关联的一对一用户；
- `c_time`是注册的提交时间。

这里有个问题可以讨论一下：是否需要创建ConfirmString新表？可否都放在User表里？我认为如果全都放在User中，不利于管理，查询速度慢，创建新表有利于区分已确认和未确认的用户。最终的选择可以根据你的实际情况具体分析。

模型修改和创建完毕，需要执行migrate命令，一定不要忘了。

顺便修改一下admin.py文件，方便我们在后台修改和观察数据。

```python
# login/admin.py

from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.User)
admin.site.register(models.ConfirmString)
```

## 二、修改视图

首先，要修改我们的`register()`视图的逻辑：

```python
def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                code = make_confirm_string(new_user)
                send_email(email, code)

                message = '请前往邮箱进行确认！'
                return render(request, 'login/confirm.html', locals())
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())
```

关键是多了下面两行：

```python
code = make_confirm_string(new_user)
send_email(email, code)
```

`make_confirm_string()`是创建确认码对象的方法，代码如下：

```python
import datatime

def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    models.ConfirmString.objects.create(code=code, user=user,)
    return code
```

在文件顶部要先导入`datetime`模块。

`make_confirm_string()`方法接收一个用户对象作为参数。首先利用datetime模块生成一个当前时间的字符串now，再调用我们前面编写的`hash_code()`方法以用户名为基础，now为‘盐’，生成一个独一无二的哈希值，再调用ConfirmString模型的create()方法，生成并保存一个确认码对象。最后返回这个哈希值。

`send_email(email, code)`方法接收两个参数，分别是注册的邮箱和前面生成的哈希值，代码如下：

```python
from django.conf import settings

def send_email(email, code):

    from django.core.mail import EmailMultiAlternatives

    subject = '来自www.liujiangblog.com的注册确认邮件'

    text_content = '''感谢注册www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python、Django和机器学习技术的分享！\
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''

    html_content = '''
                    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>www.liujiangblog.com</a>，\
                    这里是刘江的博客和教程站点，专注于Python、Django和机器学习技术的分享！</p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
```

首先我们需要导入settings配置文件`from django.conf import settings`。

邮件内容中的所有字符串都可以根据你的实际情况进行修改。其中关键在于`<a href=''>`中链接地址的格式，我这里使用了硬编码的'127.0.0.1:8000'，请酌情修改，url里的参数名为`code`，它保存了关键的注册确认码，最后的有效期天数为设置在settings中的`CONFIRM_DAYS`。所有的这些都是可以定制的！

下面是邮件相关的settings配置：

```python
# 邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sina.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'xxx@sina.com'
EMAIL_HOST_PASSWORD = 'xxxxxx'

# 注册有效期天数
CONFIRM_DAYS = 7
```

## 三、处理邮件确认请求

首先，在根目录的`urls.py`中添加一条url：

```
path('confirm/', views.user_confirm),
```

其次，在`login/views.py`中添加一个`user_confirm`视图。

```python
def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'login/confirm.html', locals())

    c_time = confirm.c_time
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'login/confirm.html', locals())
```

说明：

- 通过`request.GET.get('code', None)`从请求的url地址中获取确认码;
- 先去数据库内查询是否有对应的确认码;
- 如果没有，返回`confirm.html`页面，并提示;
- 如果有，获取注册的时间`c_time`，加上设置的过期天数，这里是7天，然后与现在时间点进行对比；
- 如果时间已经超期，删除注册的用户，同时注册码也会一并删除，然后返回`confirm.html`页面，并提示;
- 如果未超期，修改用户的`has_confirmed`字段为True，并保存，表示通过确认了。然后删除注册码，但不删除用户本身。最后返回`confirm.html`页面，并提示。

这里需要一个`confirm.html`页面，我们将它创建在`/login/templates/login/`下面：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>注册确认</title>
</head>
<body>


    <h1 style="margin-left: 100px;">{{ message }}</h1>

    <script>
        window.setTimeout("window.location='/login/'",2000);
    </script>

</body>
</html>
```

页面中通过JS代码，设置2秒后自动跳转到登录页面。

confirm.html页面仅仅是个示意的提示页面，你可以根据自己的需要去除或者美化。

## 四、修改登录规则

既然未进行邮件确认的用户不能登录，那么我们就必须修改登录规则，如下所示：

```python
def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except :
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())

            if not user.has_confirmed:
                message = '该用户还未经过邮件确认！'
                return render(request, 'login/login.html', locals())

            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())
```

关键是下面的部分：

```python
if not user.has_confirmed:
    message = '该用户还未经过邮件确认！'
    return render(request, 'login/login.html', locals())
```

最后，贴出view.py的整体代码，供大家参考：

```python
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from . import models
from . import forms
import hashlib
import datetime
# Create your views here.


def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    models.ConfirmString.objects.create(code=code, user=user)
    return code


def send_email(email, code):

    from django.core.mail import EmailMultiAlternatives

    subject = '来自www.liujiangblog.com的注册确认邮件'

    text_content = '''感谢注册www.liujiangblog.com，这里是刘江的博客和教程站点，专注于Python、Django和机器学习技术的分享！\
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''

    html_content = '''
                    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>www.liujiangblog.com</a>，\
                    这里是刘江的博客和教程站点，专注于Python、Django和机器学习技术的分享！</p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def index(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except :
                message = '用户不存在！'
                return render(request, 'login/login.html', locals())

            if not user.has_confirmed:
                message = '该用户还未经过邮件确认！'
                return render(request, 'login/login.html', locals())

            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/index/')
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                code = make_confirm_string(new_user)
                send_email(email, code)

                message = '请前往邮箱进行确认！'
                return render(request, 'login/confirm.html', locals())
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    request.session.flush()
    # del request.session['is_login']
    return redirect("/login/")


def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''

    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求！'
        return render(request, 'login/confirm.html', locals())

    c_time = confirm.c_time
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册！'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'login/confirm.html', locals())
```

## 五、功能展示

首先，通过admin后台删除原来所有的用户。

进入注册页面，如下图所示：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-af80e51bdeb85bde.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

点击注册后，跳转到提示信息页面，2秒后再跳转到登录页面。

尝试登录用户，但提示还未进行邮件确认：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-8c2a232e7b0075ec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

进入admin后台，查看刚才建立的用户，可以看到其处于未确认状态：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-df4c8a5ec184156d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

进入你的测试邮箱，查看注册邮件：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-18bb13274100e592.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

点击链接，自动跳转到确认成功提示页面，2秒后再跳转到登录页面。这个时候再次查看admin后台，可以看到用户已经处于登录确认状态，并且确认码也被自动删除了，不会第二次被使用：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-0f90eef834abf975.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

使用该用户正常登录吧！Very Good！一切都很不错！

## 六、总结说明

关于邮件注册，还有很多内容可以探讨，比如定时删除未在有效期内进行邮件确认的用户，这个可以用Django的celery实现，或者使用Linux的cronb功能。

关于邮件注册的工作逻辑，项目里只是抛砖引玉，做个展示，并不够严谨，也需要你自己根据实际环境去设计。

最后，其实Django生态圈有一个现成的邮件注册模块django-registration，但是这个模块灵活度不高，并且绑定了Auth框架，有兴趣的可以去看看其英文文档，中文资料较少。



# 13. 使用Github管理项目

阅读: 12558

------

项目介绍到这里，基本就结束了，可对于真正的业务开发，还只是刚开始。

不管是对于教程代码免费分享的需要，还是项目开发过程中的版本管理，Github都是我们首选的开源代码仓库，如果你没有私有仓库，并且不用保护代码，那么将项目上传到Github上是最佳的选择。

关于如何使用Git软件请自行学习，或许以后有空我也会写点教程。如何在Pycharm中配合Github，则在站点的博客中有一篇[《在Pycharm中使用GitHub》](http://www.liujiangblog.com/blog/4/)，可供大家参考。

## 一、 创建requirements.txt文件

`requirements.txt`文件是一个项目的依赖文件，可以通过下面的方式自动生成：

进入虚拟环境，切换到项目根目录下，使用pip工具的freeze参数。

```
(venv) D:\work\2019\for_test\mysite>pip freeze > ./requirements.txt
```

打开`requirements.txt`文件，其内容如下：

```python
Django==2.2
django-ranged-response==0.2.0
django-simple-captcha==0.5.11
Pillow==6.0.0
pytz==2018.9
six==1.12.0
sqlparse==0.3.0
```

他人如果拷贝了我们的代码，要安装第三方库依赖的话，只需要：

```
pip install -r requirements.txt
```

就可以一次性安装好所有的库了。

## 二、创建.gitignore文件

在项目代码中，有一些文件是不能上传的，比如密码文件、数据库文件、核心配置文件等等，还有一些是不用上传的，比如临时文件。为了让git自动忽略这些文件，我们需要创建一个忽略名单。

在项目根目录下新建一个`.gitignore`文件，这里可能需要你在Pycharm下安装ignore插件，如下图所示：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-20ec743495ad31f0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

我这里是已经安装好了，新安装的话，要在搜索栏里搜索到插件后再安装。

在`.gitignore`文件里写入下面的内容：

```
.gitignore
venv
.idea
settings.py
db.sqlite3
mysite/__pycache__/
```

这些文件将不会上传到Github中，也不会进行版本管理。

## 三、特殊文件处理

对于settings.py文件有个问题，如果没有这个文件是无法运行Django项目的，但是settings中又可能包含很多关键的不可泄露的部分，比如SECRET_KEY：

```
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b(&6i_$g2%8vh)ruu$)a9pkw+s-e&qj_e_#=@gnbo^48#gp_8a'
```

还有数据库的IP/Port、用户名和密码，邮件发送端的用户名和密码，这些都是绝对不能泄露的。

那怎么办呢？简单！复制settings文件，并重命名为settings.example.py文件，放在同一目录里，把敏感信息、密码等修改或删除。使用者看到这个文件名，自然会明白它的作用。

## 四、添加说明文件和许可文件

通常我们要给Github的仓库添加说明文件和许可文件。

在项目根目录下创建一个`README.md`文件，这是markdown格式的。在文件里写入项目说明，使用方法，注意事项等等所有你认为需要说明的东西。

```
## 这是一个用户登录和注册教学项目
## 这是一个可重用的登录和注册APP
## 该项目教程发布在www.liujiangblog.com

## 简单的使用方法：


创建虚拟环境
使用pip安装第三方依赖
修改settings.example.py文件为settings.py
运行migrate命令，创建数据库和数据表
运行python manage.py runserver启动服务器


路由设置：


from django.contrib import admin
from django.urls import path, include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('confirm/', views.user_confirm),
    path('captcha/', include('captcha.urls'))   # 增加这一行
]
```

对于许可文件`LICENSE`，如果你暂时不想公开授权，或者不知道用哪种授权，可以暂时不提供。

下面是一个APACHE2.0授权的范例：

```
   mysite - User login and register system

   Copyright 2019- www.liujiangblog.com

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## 五、上传代码

这里我们将项目上传到github中，并取名为login-register。

在上传过程中，确认文件列表的时候，一定要注意查看没有保密文件被上传。

![image.png](https://upload-images.jianshu.io/upload_images/2458108-9eb729f02d14afe8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

等待一会，项目文件上传完毕后，进入Github的仓库页面，如下所示：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-8aa5128cc71857b0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

点击进入详细页面：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-d53db17aaedf2e16.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

现在，所有人都可以通过下面的方式，下载和使用本项目的源代码了：

```
git clone https://github.com/feixuelove1009/login-register
```

## 六、使用Github仓库中的源码

如果你不是从教程的开始一步步地实现整个项目，而是直接使用从Github上copy下来的整个源码，那么你可能需要做一些额外的工作，比如：

- 创建虚拟环境
- 使用pip安装第三方依赖
- 修改settings.example.py文件为settings.py
- 运行migrate命令，创建数据库和数据表
- 运行python manage.py runserver启动服务器

而在Pycharm中运行服务器的话，可能还需要做一些额外的工作，比如：

- 配置解释器
- 配置启动参数

因为你本地Pycharm的配置情况，可能会发生不同的问题，需要根据实际情况实际处理，下面给两张配置图，供大家参考：

![image.png](https://upload-images.jianshu.io/upload_images/2458108-132c1e79e53a76c0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![image.png](https://upload-images.jianshu.io/upload_images/2458108-b330586afe212c82.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

以上内容，都经过实际测试，如果你依然不能顺利启动服务器，请详细检查Pycharm的配置。



# 14. 重用app

阅读: 401

------

在开发Django项目的过程中，有一些app是经常需要用到的，比如用户注册和登录app。你每次开发一个新项目，就重新写一个用户系统？不需要的，直接重用先前写好的就行了。有时候，我们需要将自己写的app分发给同事，分享给朋友，或者在互联网上发布，让全世界的用户使用。比如发布到Django官方的app仓库：https://djangopackages.org/ 。这都需要打包、分发和重用我们的app。

Django的子系统重用是基于app级别的。也就是一个项目可以包含多个互相独立的app，不同项目之间没有关系。但是，一个app可以属于多个项目，可以在任何地点、任何时间和任何项目中被重用。

一个app要能被重用，首先在设计和开发它的阶段，就要考虑后期重用的问题。你需要将该app运行时所必须的全部文件、资源、配置、数据等等都封装在一个整体内。如果有任何一部分重要的内容，放置在app之外，比如最初项目的其它目录下，都将引起重用失败。

Django需要使用setuptools和pip来打包我们的app，所以请先安装他们。对于当前的Python3.6，自带了这两个工具，不需要额外安装。

## 一、 打包app

打包的本质，就是封装你的源代码和文件成为一种新的数据包装格式，有利于传输、分发和安装。在Django中打包一个app只需要下面八个步骤：

### 1. 文件准备

在你的Django项目目录外面，为我们的login应用，准备一个父目录，这里取名`django-login-register`。

**额外提醒：**

为你的app选择一个合适的名字：在取名前，去PyPi搜索一下是否有重名或冲突的app（包）已经存在。建议给app的名字加上“django-”的前缀。名字不能和任何Django的`contrib packages`中的app重名，例如auth、admin、messages等等。

### 2. 拷贝文件

将mysite/login目录中的所有内容拷贝到`django-login-register`目录内。将login/migrations目录中，除了`__init__.py`外的文件全部删除，这些被删除的文件是我们先前在本地数据库的操作记录，不应该打包到里面。

### 3. 创建说明文档

创建一个说明文档`django-login-register/README.rst`，写入下面的内容：

```
=====
登录和注册系统
=====
## 这是一个用户登录和注册教学项目
## 这是一个可重用的登录和注册APP
## 该项目教程发布在www.liujiangblog.com

## 简单的使用步骤：

1. 创建虚拟环境
2. 使用pip安装第三方依赖
3. 添加相应的路由
4. 配置settings
5. 运行migrate命令，创建数据库和数据表
6. 链接你的index页面
7. 运行python manage.py runserver启动服务器


## 路由设置：

from django.contrib import admin
from django.urls import path, include
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('confirm/', views.user_confirm),
    path('captcha/', include('captcha.urls'))   
]



## settings配置：

1. 在INSTALLED_APPS中添加‘login’，'captcha'
2. 默认使用Sqlite数据库
3. LANGUAGE_CODE = 'zh-hans'
4. TIME_ZONE = 'Asia/Shanghai'
5. USE_TZ = False

# 邮件服务设置
6. EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
7. EMAIL_HOST = 'smtp.sina.com'
8. EMAIL_PORT = 25
9. EMAIL_HOST_USER = 'xxxx@sina.com'
10. EMAIL_HOST_PASSWORD = 'xxxxx'

# 注册有效期天数
11. CONFIRM_DAYS = 7
```

这其实是一个纯文本文件，内容和格式完全自由，但核心要点是注明你的app功能和简单的使用方法。

### 4. 添加授权声明

创建一个`django-login-register/LICENSE`版权申明文件。大多数Django相关的app都基于BSD版权。如果不是发布到正式场合，可以不写。

### 5. 创建setup.py脚本

创建一个`django-login-register/setup.py`文件，包含了编译和安装app的配置细节。这种配置脚本的具体语法，请前往setuptools的官方文档获取详细的教程。下面是一个范例，大多数情况下，你在此基础上改改就可以了：

```
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-login-register',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='一个通用的用户注册和登录系统',
    long_description=README,
    url='https://www.liujiangblog.com/',
    author='liujiang',
    author_email='yourname@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
```

例子中的配置项看起来有点复杂，实际简单得不要不要的。耐心点，就完全不是问题。

需要注意的是，如果你的readme文件中有中文，那么在setup.py文件的open方法中要指定`encoding='utf-8'`，否则会出现编码错误。

### 6. 创建MANIFEST文件

默认情况下，只有Python的模块和包会被打包进我们的app内。为了包含一些其它的文件，比如静态文件、templates模板等非Python语言编写的文件，需要创建一个`django-login-register/MANIFEST.in`文件，并写入下面的内容：

```
include LICENSE
include README.rst
recursive-include login/static *
recursive-include login/templates *
recursive-include docs *
```

### 7. 添加doc目录

该步骤可选，但是强烈推荐将详细的说明文档一起打包。创建一个空的目录`django-login-register/docs`，用于放置app相关的所有文档。同时确认在`django-login-register/MANIFEST.in`文件内有一行`recursive-include docs *`。需要注意的是，如果docs目录是空的，那么它不会被打包进去。

### 8. 执行打包动作

在`django-login-register`目录内，运行`python setup.py sdist`命令。这将会创建一个dist目录，并生成`django-login-register-1.0.tar.gz`文件。同时生成一个`django_login_register.egg-info`文件夹。

八个步骤完成了，我们的app也就打包好了。

## 二、使用打包好的app

实际使用时，我们只需要使用`django-login-register-1.0.tar.gz`这个文件就可以了。

在安装包的时候，最好是以个人用户的身份安装，而不是全系统范围的身份。这样可以有效减少给别的用户带去的影响或被别的用户影响。当然，最好的方式是在virtualenv环境，这种类似隔离的沙盒环境中使用（此时，不需要`--user`选项）。

**安装：**

```
pip install --user django-login-register-1.0.tar.gz
(venv) D:\work\for_test\dj_test\venv\Scripts>pip install d:\django-login-register-1.0.tar.gz
Processing d:\django-login-register-1.0.tar.gz
Installing collected packages: django-login-register
  Running setup.py install for django-login-register ... done
Successfully installed django-login-register-1.0

(venv) D:\work\for_test\dj_test\venv\Scripts>pip list
Package               Version
--------------------- ---------
certifi               2018.8.13
chardet               3.0.4
Django                2.0.7
django-login-register 1.0
idna                  2.7
Pillow                5.4.1
pip                   10.0.1
pytz                  2018.5
requests              2.19.1
setuptools            39.1.0
urllib3               1.23
```

在windows中使用`--user`选项会将文件安装到你的用户目录，而不是python目录中，所以建议不使用这个选项。另外，windows下使用cmd命令行时候，记得使用管理员权限打开。

在虚拟环境中使用pip安装的时候，一定要注意pip和Python的对应关系，所有的重点都是，你必须确保包被安装在了正确的位置。

最后需要提醒的是，这种方式安装后，app的文件会放在Python环境的site-packages中，而不是以源代码的形式放在我们认为的项目中。我们可以import login，可以在settings中注册‘login’，但要修改login中的源码，则需要去site-packages中。

一定要注意，pip安装的时候，使用的名字是django-login-register-1.0.tar.gz，而不是`pip install login`。实际使用中import的时候是‘import login’，而不是‘import django-login-register’。

安装成功后，再安装依赖包django-simple-captcha等等，然后在新Django项目的`INSTALLED_APPS`设置中注册`login`和captcha，按照使用说明，添加路由，修改settings配置，创建数据表，链接新的index页面，然后启动服务器，就可以使用这个app了。

**卸载方法：**

```
pip uninstall django-login-register
```

对于新手，一定要清楚的是：**以使用一个第三方库的形式来重用这个app**

重用的过程有些细节可能这里没有仔细说明，但都能见招拆招，解决起来并不麻烦，而且都是基本知识。

## 三、发布你的app

可以通过下面的方式发布你的app：

- 通过邮件的形式将app发送给朋友
- 将app上传到你的网站
- 将app推送到一个公开的仓库，例如PyPI，github等。

在https://packaging.python.org/distributing/#uploading-your-project-to-pypi中有如何上传到PyPI的教程。