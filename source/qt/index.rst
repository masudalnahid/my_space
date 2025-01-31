#########
Qt学习
#########

*******
Book   
*******

Book
------

* `C++ GUI Qt 4编程（第二版） <http://linux.linuxidc.com/index.php?folder=MjAxMsTq18rBzy821MIvNMjVL0Ox4LPMo6i12rb+sOajqSjW0M7EuN/H5VBERsmow+iw5ilAy+bK6dS0wus=>`_ 
* `QmlBook  <https://cwc1987.gitbooks.io/qmlbook-in-chinese/content/>`_
* https://github.com/cwc1987/QmlBook-In-Chinese


* `Qt学习之路 <https://www.devbean.net/2012/08/qt-study-road-2-catelog/>`_
* `Qt开源社区 <http://www.qter.org/>`_
    * `精品教程 <http://www.qter.org/portal.php?mod=list&catid=6>`_
* `QTCN <http://www.qtcn.org/gpq4/>`_
* `Qt 参考文档 <http://www.kuqin.com/qtdocument/index.html>`_
* `Qt Download <http://download.qt.io/>`_

--------

* `图片下载网站  <https://www.flaticon.com/>`_

 www.flaticon.com/Jiangxumin/cjiangxumin@gmain.com/j6m


--------

PyQt4
    `Nullege is a search engine for Python source code <http://nullege.com/>`_

`Qt Style Sheets Examples <https://doc.qt.io/archives/qt-4.8/stylesheet-examples.html>`_

* `QListWidget 布局方向设定 <http://blog.csdn.net/yexiangcsdn/article/details/9932155>`_

* `pyqtSignal  <http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html>`_

* `PyQt4 信号和槽用法总结 <http://blog.csdn.net/jxm_csdn/article/details/51628367>`_


********************
PyQt 学习示例    
********************

* `Python GUI  <https://pythonprogramminglanguage.com/pyqt/>`_

.. code-block:: sh

    git clone --depth 1  https://github.com/pyqt/examples.git


**********
播放器    
**********

QMultimedia
    QCamera

* `SMPlayer <https://sourceforge.net/projects/smplayer/?source=typ_redirect>`_
* `获取SMPlayer <https://www.smplayer.info/zh_TW/downloads>`_

.. code-block:: sh

    $ sudo apt-get install smplayer

QT环境搭建: QT-4.8 在windows下的使用
    http://blog.csdn.net/qq_22122811/article/details/63684008

*************
跨平台编译   
*************

* `Linux下编译静态MinGW环境,编译windows平台Qt程序 <https://yjdwbj.github.io/2016/09/13/Linux%E4%B8%8B%E7%BC%96%E8%AF%91%E9%9D%99%E6%80%81MinGW%E7%8E%AF%E5%A2%83-%E7%BC%96%E8%AF%91windows%E5%B9%B3%E5%8F%B0Qt%E7%A8%8B%E5%BA%8F/>`_

* `MXE <http://mxe.cc/>`_   

********
打包    
********

*  `QT程序打包成EXE <https://blog.csdn.net/weixin_39568531/article/details/79606105>`_

***********
知识点     
***********

.. code-block:: cpp

    // QTableWidget
    this->ui->tablewidget->setSelectionBehavior(QAbstractItemView::SelectRows);  //单击选择一行  
    this->ui->tablewidget->setSelectionMode(QAbstractItemView::SingleSelection); //设置只能选择一行，不能多行选中  
    this->ui->tablewidget->setEditTriggers(QAbstractItemView::NoEditTriggers);   //设置每行内容不可更改  
    this->ui->tablewidget->setAlternatingRowColors(true);                        //设置隔一行变一颜色，即：一灰一白 


.. code-block:: bash

    # install qt4
    $ sudo apt-get install qt4-dev-tools qt4-doc qt4-qtconfig qt4-demos qt4-designer -y --force-yes

    # qtcreator-3.5.1 depends
    $ sudo apt-get install libgstreamer-plugins-base0.10-0


************
NextCloud   
************

* `Git Client <https://github.com/nextcloud/client>`_
* `Build the Client <https://github.com/nextcloud/client_theming>`_


************
StyleSheet   
************

.. code::  

        /************************ 
        *   横向 Slider 
        ************************/
        QSlider::groove:horizontal {
                border: 1px solid #4A708B;
                background: #C0C0C0;
                height: 5px;
                border-radius: 1px;
                padding-left:-1px;
                padding-right:-1px;
        }
         
        QSlider::sub-page:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #B1B1B1, stop:1 #c4c4c4);
                background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
                    stop: 0 #5DCCFF, stop: 1 #1874CD);
                border: 1px solid #4A708B;
                height: 10px;
                border-radius: 2px;
        }
         
        QSlider::add-page:horizontal {
                background: #575757;
                border: 0px solid #777;
                height: 10px;
                border-radius: 2px;
        }
         
        QSlider::handle:horizontal {
            background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, 
            stop:0.6 #45ADED, stop:0.778409 rgba(255, 255, 255, 255));
         
            width: 11px;
            margin-top: -3px;
            margin-bottom: -3px;
            border-radius: 5px;
        }
         
        QSlider::handle:horizontal:hover {
            background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 #2A8BDA, 
            stop:0.778409 rgba(255, 255, 255, 255));
         
            width: 11px;
            margin-top: -3px;
            margin-bottom: -3px;
            border-radius: 5px;
        }
         
        QSlider::sub-page:horizontal:disabled {
                background: #00009C;
                border-color: #999;
        }
         
        QSlider::add-page:horizontal:disabled {
                background: #eee;
                border-color: #999;
        }
         
        QSlider::handle:horizontal:disabled {
                background: #eee;
                border: 1px solid #aaa;
                border-radius: 4px;
        }


        /************************ 
        *   纵向 Slider 
        ************************/

        QSlider::groove:vertical {
                border: 1px solid #4A708B;
                background: #C0C0C0;
                width: 5px;
                border-radius: 1px;
                padding-left:-1px;
                padding-right:-1px;
                padding-top:-1px;
                padding-bottom:-1px;
        }
         
        QSlider::sub-page:vertical {
                background: #575757;
                border: 1px solid #4A708B;
                border-radius: 2px;
        }
         
        QSlider::add-page:vertical {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
                    stop:0 #c4c4c4, stop:1 #B1B1B1);
                background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
                    stop: 0 #5DCCFF, stop: 1 #1874CD);
                border: 0px solid #777;
                width: 10px;
                border-radius: 2px;
        }
         
        QSlider::handle:vertical 
        {
                background: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.6 #45ADED, 
                stop:0.778409 rgba(255, 255, 255, 255));
         
                height: 11px;
                margin-left: -3px;
                margin-right: -3px;
                border-radius: 5px;
        }
         
        QSlider::sub-page:vertical:disabled {
                background: #00009C;
                border-color: #999;
        }
         
        QSlider::add-page:vertical:disabled {
                background: #eee;
                border-color: #999;
        }
         
        QSlider::handle:vertical:disabled {
                background: #eee;
                border: 1px solid #aaa;
                border-radius: 4px;
        }

..
 Music 命运守护夜

.. raw:: html

    <iframe frameborder="no" border="0" marginwidth="0" marginheight="0" width=330 height=300 
    src="https://music.163.com/outchain/player?type=0&id=821701962&auto=1&height=430">
    </iframe>


