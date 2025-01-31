其他
================


::

    windows 计算 MD5 SHA1  SHA256
    > certutil -hashfile D:\filename.txt MD5
    > certutil -hashfile D:\filename.txt SHA1
    > certutil -hashfile D:\filename.txt SHA256


.. code-block:: bash

    # ubuntu install protobuf
    sudo apt-get install  libprotobuf-dev
    sudo apt-get install protobuf-compiler

    #
    g++ write.cpp addressbook.pb.cc  -o write `pkg-config --cflags --lib    s protobuf`
    g++ read.cpp addressbook.pb.cc  -o read `pkg-config --cflags --libs     protobuf`



JRebel激活
-----------------

* http://blog.lanyus.com/archives/174.html
* `撸了个反代工具, 可用于激活JRebel <http://blog.lanyus.com/archives/317.html>`_

.. code-block:: sh

        docker pull ilanyu/golang-reverseproxy
        docker run -d -p 8888:8888 ilanyu/golang-reverseproxy
        # 1. 浏览器打开 http://127.0.0.1:8888/
        # 2. 点击"获取注册码"
                                                                      

http://blog.lanyus.com/archives/317.html

Windows镜像下载地址
    https://msdn.itellyou.cn/

qbittorrent
    http://www.qbittorrent.org/

OBS Studio
-----------------

官网
    https://obsproject.com/

搭建RTMP服务器

**Docker**

.. code-block:: bash

    # https://hub.docker.com/r/jasonrivers/nginx-rtmp/
    $ sudo docker run -d  -p 1935:1935 -p 8088:8080  --rm  jasonrivers/nginx-rtmp

    # or 
    # https://github.com/alfg/docker-nginx-rtmp
    $ sudo docker run -d -p 1935:1935 -p 8080:80 --rm alfg/nginx-rtmp

**windows**

    http://bbs.ngacn.cc/read.php?tid=10021940&rand=854
    https://obsproject.com/forum/resources/how-to-set-up-your-own-private-rtmfp-server-using-monaserver.153/


http://www.hangge.com/blog/cache/detail_1325.html


开源许可证
-----------

http://www.ruanyifeng.com/blog/2011/05/how_to_choose_free_software_licenses.html

http://www.ruanyifeng.com/blog/2011/05/how_to_choose_free_software_licenses.html

ceph
    * `英文文档 <http://docs.ceph.com/docs/master/rados/>`_
    * `中文文档 <http://docs.ceph.org.cn/>`_

`FreeNAS+廉价主机：搭建低成本家庭多媒体共享方案 <https://post.smzdm.com/p/27048/>`_

流程图
--------------

* `ProcessOn <https://www.processon.com/>`_
* `yEd <https://www.yworks.com/products/yed/download>`_

---------------

* `mobaxterm <https://mobaxterm.mobatek.net/download.html>`_

--------------

* `协作工具 leangoo <https://www.leangoo.com>`_


other
--------------

mingw编译gtk
^^^^^^^^^^^^

`Hello World program using GTK+ <http://mingw-cross.sourceforge.net/hello_gtk.html>`_

------------------------

`不要这样学习JavaScript <http://blog.crimx.com/2014/05/15/how-to-learn-javascript-properly/#不要这样学习JavaScript>`_

------------------------

* `快速建立工程模板cookiecutter <https://pypi.python.org/pypi/cookiecutter/1.5.1>`_
* `virtualenv搭建虚拟环境 <http://www.cnblogs.com/kym/archive/2011/12/29/2306428.html>`_


patch
-----

* `linux patch 命令小结 <http://blog.csdn.net/wh_19910525/article/details/7515540>`_
* `patch 命令用法详解 <http://blog.csdn.net/clozxy/article/details/5830880>`_
* `二进制patch工具xdelta的使用方法 <http://blog.csdn.net/panda_bear/article/details/8191859/>`_



SPAW 分区
-------------

`Linux系统swappiness参数在内存与交换分区之间优化作用 <http://blog.csdn.net/lufeisan/article/details/53339991>`_

Linux VPS的使用过程中，SWAP交换分区是一个很重要系统缓存分区。他是在内存不够用的情况下，从硬盘中临时分出一部分空间系统当做内存使用。但是，如果SWAP的占用超过30%的时候，系统的性能就会受到影响，这时候就要刷新SWAP。

.. code-block:: sh

    # 可以执行命令刷新一次SWAP（将SWAP里的数据转储回内存，并清空SWAP里的数据）
    $ sudo swapoff -a && sudo swapon -a

    
    $ cat /proc/sys/vm/swappiness  # 查看
    $ sysctl -q vm.swappiness      # 查看当前设置

    # 临时设置
    $ sudo sysctl vm.swappiness=10

    # 永久设置
    $ sudo echo "vm.swappiness=10" >> /etc/sysctl.conf
    $ sysctl -p  # 激活




屏幕录像gif
---------------

* `LICEcap(支持Windows Mac) <http://www.cockos.com/licecap/>`_
* `byzanz-gui(支持Linux) <https://git.oschina.net/mc_space/byzanz-gui>`_


检查端口通不通
----------------


查看端口占用
^^^^^^^^^^^^^

    .. code-block:: sh

        $ sudo netstat -anp | grep ":80\ "


检查端口通不通
^^^^^^^^^^^^^^^^

#. python 检查端口通不通

    .. code-block:: python

        #!/usr/bin/env python
        #coding=utf8

        ip = '192.168.5.204'
        port  = 5900

        import socket
         
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         
        sk.settimeout(1)
         
        try:
            sk.connect((ip,port))
            print 'Server %s:%s  OK!' % (ip,port)
        except Exception:
            print 'Server %s:%s not connect!' % (ip,port) 
        sk.close()




#. nc命令检查端口通不通

    .. code-block:: sh

        $ nc  -vz 192.168.5.204 5904


#. telnet 命令检查端口通不通

    
    .. code-block:: sh

        $ telnet 192.168.5.204 5900 

#. 查看当前使用的端口

    .. code-block:: sh

       $ netstat -anlp | grep -w LISTEN
       $ netstat -aunp      # udp


CenterOS
------------

#. 检查某服务是否开机启动

    .. code-block:: sh

            # chkconfig dnsmasq 
	

#. 开启/禁止 某服务开机启动

    .. code-block:: sh

            # chkconfig dnsmasq on/off
            # systemctl enable/disable  dnsmasq 
	

#. 启动/停止/重启 某服务

    .. code-block:: sh

            # systemctl start/stop/restart dnsmasq 


amixer
---------

* `Ubuntu14.04使能root用户音频系统 <http://blog.163.com/ljf_gzhu/blog/static/13155344020156513446281/>`_

`amixer的用法(音频编码音量控制) <http://blog.sina.com.cn/s/blog_8795b0970101ig2p.html>`_

#. 查看:

.. code-block:: sh

    $ sudo alsamixer
    $ sudo amixer -D pulse
    $ sudo amixer scontrols   # 查看,哪些选择可以控制

#. 声音设置

.. code-block:: sh

    $ amixer -D pulse sset "Master" on
    $ amixer -D pulse sset "Master" off    // 静音
    $ amixer set "Master" 100%

    $ amixer set "PCM" 94%    #  6100u 华科 噪音

#. 录音设置

.. code-block:: sh

    $ amixer set "Capture" 100%

    $ amixer set "Front Mic Boost" 53%
    $ amixer set "Rear Mic Boost"  53%


`alsamixer设置默认声卡及调节音量保存配置 <http://www.it165.net/os/html/201212/4118.html>`_


.. code-block:: bash

    $ sudo apt-get install alsa-base alsa-utils alsa-oss alsa-tools

    # 1. 如果默认声卡不是需要的
    # 在home目录添加.asoundrc文件

    $ sudo tee $HOME/.asoundrc <<-'EOF'
    defaults.ctl.card 1 defaults.pcm.card 1
    EOF

    # 数字1代表声卡序号
    # 可以通过以下指令查看

    $ cat /proc/asound/cards

    # 2. alsamixer调节声音
    # Master和PCM是必须打开的。
    # Master和PCM声道默认是静音的，标记是MM，用左右方向键选择，按M来修改为OO就是开启，上下键调节音量大小。 
    # 配置好之后执行：
    $ alsactl store # 保存配置, 配置会保存在/var/lib/alsa/asound.state


nmcli命令
-----------

`2.3.使用 NETWORKMANAGER 命令行工具 NMCLI <https://access.redhat.com/documentation/zh-CN/Red_Hat_Enterprise_Linux/7/html/Networking_Guide/sec-Using_the_NetworkManager_Command_Line_Tool_nmcli.html>`_


.. code:: sh

    $ nmcli help
    $ nmcli c help

    $ nmcli con show
    $ nmcli dev show eth0

*  `工具Valgrind,检测内存泄露 <https://www.cnblogs.com/wangkangluo1/archive/2011/07/20/2111248.html>`_


rmp and yum   
--------------

* `RPM包的制作* <https://blog.csdn.net/samxx8/article/details/71945726>`_


查询含有 *\*rdma.so* 的rpm 包
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: sh

    yum provides *rdma.so


Fedora 开启SSH服务
   https://my.oschina.net/atttx123/blog/58100 

* `Nextcloud+Collabora Office文档在线协作 <https://www.orgleaf.com/2280.html>`_

vmware 问题
-----------

http://www.jianshu.com/p/df30c0c3889b

https://communities.vmware.com/thread/552232

`Download VMware-Player-12.5.2-4638234_Linux-4.9_patch.sh <https://communities.vmware.com/servlet/JiveServlet/download/2647089-168790/VMware-Player-12.5.2-4638234_Linux-4.9_patch.sh>`_

* `最新版本 vmware workstation <https://www.vmware.com/cn/products/workstation/workstation-evaluation.html>`_
	

nginx
------

* `nginx简易教程 <http://www.cnblogs.com/jingmoxukong/p/5945200.html>`_


* BurnInTest - 电脑系统稳定性与可靠性测试工具

----------

* `Ubuntu 14.04安装teamviewer 远程桌面 <https://blog.csdn.net/love_xiaozhao/article/details/52704197>`_

ubutnu 源制作
---------------

.. code-block:: sh

    # 1、
    mkdir -p /var/www/soft
    mkdir -p /var/www/dists/lucid/main

    # 2、 
    cp *.deb /var/www/soft/

    # 3、
    # 如果是arm的deb包把命令行中的amd改成arm ，如果说是32位操作系统安装的包同理把64改成32,
    # 不过32位就是32位，64位的制作64位的，不要混要不然装的时候报错
    dpkg-scanpackages soft/ /dev/null | gzip > /var/www/dists/lucid/main/binary-amd64/Packages.gz

    # 4、
    cp http_file_server.py /var/www/soft               

    # 5、（命令行）
    python http_file_server.py
    #ok 本地安装源制作完成。

    # 6、本地测试：
    mv  /etc/apt/sources.list   /etc/apt/sources.list.bak
    #添加如下，内容
    tee  /etc/apt/sources.list <<-"EOF"
    deb http://127.0.0.1:8008 lucid main
    EOF
    # 
    apt-get update
    apt-cache search  "deb包“

ubuntu 好用的工具
------------------

.. code-block:: sh

	# Indicator Stickynotes - Ubuntu 桌面便签小工具 
	sudo add-apt-repository ppa:umang/indicator-stickynotes
	sudo apt-get update 
	sudo apt-get install indicator-stickynotes 

问题
------

``Apache2``
^^^^^^^^^^^^^

.. code::

    重启Apache2出现：
    Could not reliably determine the server's fully qualified domain name, using 127.0.1.1 for ServerName.问题
    在/etc/apache2/apache2.conf文件最后加上：
    # Server Name
    ServerName localhost

.. code-block:: bash

    # centos 目录或文件名中文显示 
    # vim /etc/httpd/conf/httpd.conf
    AddDefaultCharset UTF-8
    IndexOptions Charset=GBK


.. raw:: html

    <iframe width="400" height="225" frameborder="0" src="http://127.0.0.1:3080/media/adding-a-video-in-mediadrop/embed_player"></iframe>

------

.. raw:: html

    <iframe src="http://www.google.cn/maps/embed?pb=!1m14!1m12!1m3!1d11676.277536269174!2d117.22922223214272!3d36.730209801497175!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e1!3m2!1szh-CN!2scn!4v1501312245008" width="600" height="450" frameborder="0" style="border:0" allowfullscreen></iframe>

插入youku视频

.. raw:: html

    <object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,19,0" width="550" height="325"><param name="movie" value="http://v.ifeng.com/include/exterior.swf?guid=95a6f52b-89d1-4e61-8f17-faecb03b809b&pageurl=http://www.ifeng.com&fromweb=other&AutoPlay=false" /><param name="quality" value="high" /><param name="allowScriptAccess" value="always" /><embed src="http://v.ifeng.com/include/exterior.swf?guid=95a6f52b-89d1-4e61-8f17-faecb03b809b&pageurl=http://www.ifeng.com&fromweb=other&AutoPlay=false" quality="high"  allowScriptAccess="always" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" width="550" height="325"></embed></object>

.. raw:: html

    <embed src='http://player.youku.com/player.php/sid/XMjYyMjk4MDYwMA==/v.swf' allowFullScreen='true' quality='high' width='480' height='400' align='middle' allowScriptAccess='always' type='application/x-shockwave-flash'></embed>

.. raw:: html

    <embed src='http://player.youku.com/player.php/sid/XMjc2ODQzNTcwMA==/v.swf' allowFullScreen='true' quality='high' width='480' height='400' align='middle' allowScriptAccess='always' type='application/x-shockwave-flash'></embed>

.. raw:: html

    <iframe height=498 width=510 src='http://player.youku.com/embed/XMzcyNzAyODAw' frameborder=0 'allowfullscreen'></iframe>

.. raw:: html

    <iframe height=498 width=510 src="http://player.youku.com/embed/XMjgzODg5NzYwNA==?client_id=undefined" frameborder=0 allowfullscreen></iframe>

------

插入github 视频

.. raw:: html

    <video width="638" height="478" controls>
        <source src="http://github.liaoxuefeng.com/sinaweibopy/video/git-apt-install.mp4">
    </video>


------

插入gitliab 视频

.. raw:: html

    <video width="638" height="478" controls>
        <source src="http://58.56.27.130:800/jiang_xmin/videos/raw/master/test/LakePowell_Thunderstorms_nimiaRM_4471864_062_1080_HD_ZH-CN.mp4">
    </video>


    <video width="638" height="478" controls>
        <source src="http://58.56.27.130:800/jiang_xmin/videos/raw/master/mcserver/creat_course.mp4">
    </video>



-------

插入百度云盘

.. raw:: html

    <video width="638" height="478" controls>
        <source src="https://d11.baidupcs.com/file/c3f114b8af0538d6115cb999c203bc5f?bkt=p3-0000704efb1fbe3f09ed4973db1154656483&xcode=818c9e935f798db6570eaae746598dd0bfa3efe48b5ae2b70b2977702d3e6764&fid=705205442-250528-55740032843716&time=1498015007&sign=FDTAXGERLBHS-DCb740ccc5511e5e8fedcff06b081203-2E7ZycCw1sxqN%2FzX%2BiT%2BOeA9IUQ%3D&to=d11&size=452161518&sta_dx=452161518&sta_cs=5604&sta_ft=mp4&sta_ct=7&sta_mt=5&fm2=MH,Yangquan,Netizen-anywhere,,shandong,ct&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=0000704efb1fbe3f09ed4973db1154656483&sl=83099727&expires=8h&rt=sh&r=376250870&mlogid=3976873212576580908&vuk=705205442&vbdid=2939017377&fin=%E5%93%88%E5%B0%94%E7%9A%84%E7%A7%BB%E5%8A%A8%E5%9F%8E%E5%A0%A1.mp4&fn=%E5%93%88%E5%B0%94%E7%9A%84%E7%A7%BB%E5%8A%A8%E5%9F%8E%E5%A0%A1.mp4&rtype=1&iv=0&dp-logid=3976873212576580908&dp-callid=0.1.1&hps=1&csl=299&csign=aH32eCyhXT%2FyKiSSRhPc3C7xP2o%3D&by=themis">
    </video>

    <video width="638" height="478" controls>
        <source src="https://nbct01.baidupcs.com/file/9d2bdcb775c417ba82e5001aced243b7?bkt=p3-00003ba7ed0850b8b6036fd520787b5e1e39&fid=705205442-250528-230870834788841&time=1498016729&sign=FDTAXGERLBHS-DCb740ccc5511e5e8fedcff06b081203-vXKmCJCb3EMkQOHUYeMdUoNMb6o%3D&to=67&size=45713742&sta_dx=45713742&sta_cs=3&sta_ft=mp4&sta_ct=7&sta_mt=5&fm2=MH,Ningbo,Netizen-anywhere,,shandong,ct&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=00003ba7ed0850b8b6036fd520787b5e1e39&sl=79888463&expires=8h&rt=sh&r=318596121&mlogid=3977335580399524366&vuk=705205442&vbdid=2939017377&fin=%E7%AC%AC01%E7%AB%A001+%E5%AD%A6%E4%B9%A0%E8%AE%BE%E5%A4%87%E5%87%86%E5%A4%87%E5%8F%8A%E5%AD%A6%E4%B9%A0%E8%AE%BA%E5%9D%9B.mp4&fn=%E7%AC%AC01%E7%AB%A001+%E5%AD%A6%E4%B9%A0%E8%AE%BE%E5%A4%87%E5%87%86%E5%A4%87%E5%8F%8A%E5%AD%A6%E4%B9%A0%E8%AE%BA%E5%9D%9B.mp4&rtype=1&iv=0&dp-logid=3977335580399524366&dp-callid=0.1.1&hps=1&csl=284&csign=i3P%2FclMK%2FwgOYQR3g9DYv8cgku8%3D&by=themis">
    </video>


remote-viewer
    https://www.systutorials.com/docs/linux/man/1-remote-viewer/

   --hotkeys=release-cursor=""   # 屏蔽 ctrl+alt
   
   
