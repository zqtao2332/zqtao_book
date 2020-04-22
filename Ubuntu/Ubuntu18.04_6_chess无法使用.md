# **Ubuntu18.04_6_chess摄像头的调用失败解决办法**

Ubuntu18.04安装在VMware中，Ubuntu调用相机，调用的其实是本机的驱动，想要成功调用，首先需要检查驱动是否已经挂载到虚拟机上。

![](https://img-blog.csdn.net/20180123093802838?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGlhb3ppMDIyMQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

未挂载则，连接。

如以上操作都正常，应该可以看到摄像头灯点亮并且cheese窗口显示视频。

但是如上操作都正常，cheese出来的视频窗口是黑屏的，怎么回事？

在Vmware Workstation的“虚拟机”->“虚拟机设置”->“USB控制器”下，查看“USB兼容性”，如果当前是“USB2.0”就修改为“USB3.0”，反之就修改为“USB2.0”。然后再在“虚拟机”->“可移动设备”下重新连接Camera，cheese就可以正常出视频了！
![](https://img-blog.csdn.net/20180123093835706?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQveGlhb3ppMDIyMQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)