# Ubuntu18.04_6_python版本升级后apt_pkg缺失问题

今天升级了系统的Python版本，然后`python3`的软链接也被我改成指向最新版本python3.7了, 运行一些内容出现了，**ModuleNotFoundError: No module named 'apt_pkg' 错误**

## 解决方法

在把Python3.6升级到Python3.7之后就会出现Python apt的一个混乱，所以我们需要重新为系统设置一个我们Python3.7的专属模块。

