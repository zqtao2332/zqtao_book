# Ubuntu18.04_3_安装和更换国内pip3源

Ubuntu 系统内置了 Python2 和 Python3 两个版本的开发环境，却没有内置相应的 pip3 管理工具，本文将介绍如何在Ubuntu下如何快速安装 pip3 工具，并升级到最新可用版本。

## 安装pip3

```
sudo apt-get install python3-pip
```

运行更新升级指令：

```python
sudo pip3 install --upgrade pip
```

卸载指令

```python
sudo apt-get remove python3-pip
```

## 更换国内源

1. 根目录创建.pip文件：mkdir ~/.pip

2. 创建文件pip.conf：vim .pip/pip.conf

3. 点击“i”键，进入编辑模式，复制信息：
   
   ```
   [global]
   index-url = http://mirrors.aliyun.com/pypi/simple/
   [install]
   trusted-host=mirrors.aliyun.com
   ```
   
   这个更换的是清华的源，清华的源5分钟同步官网一次，建议使用。
   清华大学 <https://pypi.tuna.tsinghua.edu.cn/simple/>
   阿里云 <http://mirrors.aliyun.com/pypi/simple/>
   中国科技大学 <https://pypi.mirrors.ustc.edu.cn/simple/>
   豆瓣(douban) <http://pypi.douban.com/simple/>
   中国科学技术大学 <http://pypi.mirrors.ustc.edu.cn/simple/>
   
4. 点击：“ESC”切换到命令行模式，输入“:wq”保存离开。

