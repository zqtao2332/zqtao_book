# Ubuntu18.04更换国内apt源

Ubuntu本身自带的apt-ge数据源是国外的，使用起来很慢，最好把apt-get的数据源更换成国内的。更新数据源为国内，是为了加速安装包的增加速度。

## 更换apt-get数据源

1. 输入：sudo -s切换为root超级管理员；
2. 执行命令：vim /etc/apt/sources.list；
3. 使用命令：%d 清空所有内容；
4. 阿里数据源地址：

```
https://developer.aliyun.com/mirror/ubuntu
```

选择相应的版本复制内容，点击“i”键进入编辑文本模式，粘贴内容到vim编辑窗体，点击“ESC”键进入编辑模式，输入“:wq”保存离开；

比如我使用的是Ubuntu 18.04

```
deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse

deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse

```

## 更新

1. 更新源：`sudo apt-get update`

2. 更新软件：`sudo apt-get upgrade`

## 其他源

清华大学 https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/
阿里云 https://developer.aliyun.com/mirror/ubuntu
中国科技大学 https://mirrors.mirrors.ustc.edu.cn/help/ubuntu/
豆瓣(douban) https://mirrors.douban.com/help/ubuntu/
中国科学技术大学 https://mirrors.mirrors.ustc.edu.cn/help/ubuntu/