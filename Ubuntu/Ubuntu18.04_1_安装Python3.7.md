# Ubuntu18.04安装Python3.7

Ubuntu18.04内置Python 3.6.9 (default, Nov  7 2019, 10:44:02) 

## **直接把python3.6升级到3.7行不行？**

dpkg报出一大堆依赖问题，没有卸载成功，进一步搜索发现前辈们的泣血警告：**千万不要卸载ubuntu自带的python版本**，否则会开不了机。

## 安装python3.7

ubuntu下不同版本的python可以共存.

**安装方法**

```
sudo apt install python3.7
```

检查一下安装：

```
tao@ubuntu:/usr/bin$ python3
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
tao@ubuntu:/usr/bin$ python3.7
Python 3.7.5 (default, Nov  7 2019, 10:50:52) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

装成功并且加入到path中了，但问题在于python3仍然指向python3.6而不是3.7

**更改python3指向**

cd到/usr/bin查看一下：

```
cd /usr/bin
ls -l | grep python
```

发现指向是3.6

```
lrwxrwxrwx 1 root root           9 Apr 20 18:44 python3 -> python3.6
-rwxr-xr-x 1 root root     4526456 Nov  7 02:44 python3.6
-rwxr-xr-x 1 root root     4526456 Nov  7 02:44 python3.6m
-rwxr-xr-x 2 root root     4873376 Nov  7 02:50 python3.7
-rwxr-xr-x 2 root root     4873376 Nov  7 02:50 python3.7m
lrwxrwxrwx 1 root root          10 Apr 20 18:44 python3m -> python3.6m

```

### 修改默认python版本号

1、删除原有Python连接文件

> sudo rm /usr/bin/python

2、切换成root账户，建立指向Python3的连接

切换root账户：sudo -s

建立执行Python3的连接

> ln -s /usr/bin/python3.6 /usr/bin/python

以上操作就是完成默认Python版本号设置