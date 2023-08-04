from typing import List, Callable, Optional
from PySide6.QtCore import (
    QSize, 
    QPoint
)
from PySide6.QtGui import (
    QPixmap,
    Qt
)
from PySide6.QtWidgets import (
    QWidget,
    QApplication, 
    QHBoxLayout, 
    QVBoxLayout,
    QMainWindow,
    QApplication
)

from .dialog import DialogOver
from .title import MyTip
from .wecome import WecomeWidget
from .menu_index import(
    MenuLeftSideFirst,
    MenuLeftSideSecondaryList,
    MenuLeftList,
    StackedWidget
)

class MainWindow(QMainWindow):
    """晓楠QT 菜单控件

    添加菜单方法:
        self.addMuen("菜单",QPixmap(":/img/menu/produce_data"),["我是菜单1","我是菜单2","我是菜单3","我是菜单4"])
    添加子页面方法 - 按类名添加
        self.addWidget(QLabel, "我是菜单1")
    添加子页面方法 - 按实例添加
        self.addWidgetInstance(QLabel(), "我是菜单2")
    """
    _w = 1020
    _h = 690
    _widget = dict()
    
    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("MainWindow")
        self.setStyleSheet(
            """QWidget#MainWindow
            {
                background-color: #f6f6f6;
            }
        """)
        self._initUI_()
        
    def _initUI_(self) -> None:
        """初始化控件
        """
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.stat = self.statusBar()                        # 开启状态栏
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.layout = QVBoxLayout(self.widget)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)          # 消除主布局间隙
        
        self.tip = MyTip(self)
        self.layout.addWidget(self.tip)
        
        self.layout_two = QHBoxLayout()                     # 添加二级布局
        self.layout.addLayout(self.layout_two)
        
        self.left_menu = MenuLeftList()                     # 初始化菜单
        self.left_menu.setFixedWidth(MenuLeftSideFirst._w + 10)  
        self.layout_two.addWidget(self.left_menu)
        # self.layout_two.addSpacing(10)
        self.right_widget = StackedWidget(WecomeWidget())   # 初始化窗口
        self.layout_two.addWidget(self.right_widget)
    
        self._move()
    
    def addMuen(
            self,
            first_menu: str,
            first_menu_img: QPixmap, 
            second_menu: List[str],
        ) -> None:
        """添加左侧菜单

        参数:
            first_menu (str): 一级菜单名称\n
            first_menu_img (QPixmap): 一级菜单图标\n
            second_menu (List[str]): 二级菜单名称
        """
        menu = MenuLeftSideFirst(first_menu, first_menu_img)
        MenuLeftSideSecondaryList(
            self.left_menu,
            menu,
            second_menu,
            self.display
        )  
    
    def display(self, name: str) -> None:
        """窗口控件添加函数

        参数:
            name (str): 窗口名字
        """
        self.add_message(name)
        self.add_popup(name)
        if name in MainWindow._widget:
            widget = MainWindow._widget[name]
            self.right_widget.addWidget(widget, name)
            
    @classmethod
    def addWidget(
        cls, 
        widget: Callable, 
        name: str
    ) -> None:
        """添加右侧窗口控件

        参数:
            widget (Callable): 窗口类名\n
            name (str): 窗口名字，应与二级菜单名字对应\n
        """
        cls._widget[name] = widget
    
    @classmethod
    def addWidgetInstance(
        cls,
        widget: QWidget, 
        name: str
    ) -> None:
        """添加右侧窗口控件

        参数:
            widget (QWidget): 窗口实例\n
            name (str): 窗口名字，应与二级菜单名字对应\n
        """
        cls._widget[name] = widget
    
    def _showNormal(self, pos: QPoint) -> None:
        """最大化下点击还原函数

        参数:
            pos (QPoint): 鼠标坐标
        """
        self.showNormal()
        self.move(
            pos.x() - MainWindow._w // 2,
            pos.y() - MyTip._h // 2
        )
        
    def _move(self):
        """初始化居中
        """
        self.resize(QSize(MainWindow._w, MainWindow._h))
        desktop = QApplication.instance().screens()[0].size()
        self.move((desktop.width() - self.width()) // 2, (desktop.height() - self.height()) // 2)

    def add_message(self, text: str) -> None:
        """状态栏添加信息

        参数:
            text (str): 信息内容
        """
        self.stat.showMessage(text)
    
    def add_popup(
        self, 
        text: str, 
        title : Optional[str] = "",
        flag: Optional[str] = "success"
    ) -> None:
        """弹窗控件

        参数:
            text (str): 弹窗类容\n
            title (Optional[str], optional): 弹窗标题. Defaults to "".\n
            flag (Optional[str], optional): 弹窗类型. Defaults to "success".
        """
        DialogOver(self, text, title, flag)
            