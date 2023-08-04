from typing import Optional, TYPE_CHECKING
from PySide6.QtWidgets import(
    QWidget, 
    QHBoxLayout, 
    QPushButton
)
from PySide6.QtCore import (
    QSize, 
    QEvent
)
from PySide6.QtGui import (
    Qt,
    QPixmap,
    QColor,
    QPaintEvent, 
    QPainter, 
    QEnterEvent,
    QMouseEvent
)

from .utils import change_theme_color
from .menu_index import MenuLeftSideFirst

if TYPE_CHECKING:
    from mainsindow import MainWindow


class TitlePushButtonMax(QPushButton):
    """最大化按钮

    参数:
        parent (MainWindow): MainWindow窗口, 用于控制其是否最大化\n
        theme_color (Optional[QColor], optional): 停靠时颜色. Defaults to QColor(30, 204, 148, 255).
    """
    def __init__(
        self, 
        parent: "MainWindow",
        theme_color: Optional[QColor] = QColor(30, 204, 148, 255)
    ) -> None:
        super().__init__()
        self.setFixedSize(24, 24)
        self._size = QSize(16, 16)
        icon = QPixmap(":/image/max.png")
        self._icon = icon.scaled(self._size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self._icon_press = change_theme_color(icon, theme_color).scaled(self._size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_max = QPixmap(":/image/max_press.png")
        self._icon_max = icon_max.scaled(self._size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self._icon_max_press = change_theme_color(icon_max, theme_color).scaled(self._size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self._parent = parent
        self._falg = False
        
        self.clicked.connect(self._MaxState)
    
    def _MaxState(self):
        """设置MainWindow窗口窗口最大化状态
        """
        if self._parent.isMaximized():
            self._parent.showNormal()
        else:
            self._parent.showMaximized()
      
    def paintEvent(self, event: QPaintEvent) -> None: 
        """重绘事件

        参数:
            event (QPaintEvent): _description_
        """
        painter = QPainter(self) 
        painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        
        if self._parent.isMaximized():
            if self._falg:
                self.draw(event, painter, self._icon_max_press)
            else:
                self.draw(event, painter, self._icon_max)
        else:
            if self._falg:
                self.draw(event, painter, self._icon_press)
            else:
                self.draw(event, painter, self._icon)
            
    def draw(self, event: QPaintEvent, painter: QPainter, icon: QPixmap) -> None:
        """重绘事件 paintEvent 的方法

        参数:
            event (QPaintEvent): QPaintEvent\n
            painter (QPainter): QPainter\n
            icon (QPixmap): 按钮图标
        """
        painter.drawPixmap(
            (self.width() - self._size.width()) // 2,
            (self.height() - self._size.height()) // 2, 
            self._size.width(), 
            self._size.height(), 
            icon
        )   
    
    def enterEvent(self, event: QEnterEvent) -> None:
        """鼠标进入事件

        参数:
            event (QEnterEvent): QEnterEvent

        返回:
            _type_: super().enterEvent(event)
        """
        self._falg = True
        return super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        """鼠标离开事件

        参数:
            event (QEvent): QEvent

        返回:
            _type_: super().leaveEvent(event)
        """
        self._falg = False
        return super().leaveEvent(event)

class TitlePushButtonMin(QPushButton):
    """最小化按钮

    参数:
        parent (QWidget): MainWindowc窗口, 用于控制其是否最小化\n
        theme_color (Optional[QColor], optional): 停靠时颜色. Defaults to QColor(30, 204, 148, 255).
    """
    def __init__(
        self, 
        parent: "MainWindow",
        theme_color: Optional[QColor] = QColor(30, 204, 148, 255)
    ) -> None:
        super().__init__()
        self.setFixedSize(24, 24)
        self._size = QSize(16, 16)
        icon = QPixmap(":/image/min.png")
        self._icon = icon.scaled(self._size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self._icon_press = change_theme_color(icon, theme_color).scaled(self._size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self._falg = False
        
        self.clicked.connect(lambda: parent.showMinimized())
        
    def paintEvent(self, event: QPaintEvent) -> None: 
        """重绘事件

        参数:
            event (QPaintEvent): _description_
        """
        painter = QPainter(self) 
        painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        if self._falg:
            self.draw(event, painter, self._icon_press)
        else:
            self.draw(event, painter, self._icon)
            
    def draw(self, event: QPaintEvent, painter: QPainter, icon: QPixmap) -> None:
        """重绘事件方法

        参数:
            event (QPaintEvent): QPaintEvent\n
            painter (QPainter): QPainter\n
            icon (QPixmap): 按钮图标
        """
        painter.drawPixmap(
            (self.width() - self._size.width()) // 2,
            (self.height() - self._size.height()) // 2, 
            self._size.width(), 
            self._size.height(), 
            icon
        )    
    
    def enterEvent(self, event: QEnterEvent) -> None:
        """鼠标进入事件

        参数:
            event (QEnterEvent): QEnterEvent

        返回:
            _type_: super().enterEvent(event)
        """
        self._falg = True
        return super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        """鼠标离开事件

        参数:
            event (QEvent): QEvent

        返回:
            _type_: super().leaveEvent(event)
        """
        self._falg = False
        return super().leaveEvent(event)

class TitlePushButtonExit(QPushButton):
    """关闭退出按钮

    参数:
        parent (QWidget): MainWindowc窗口, 用于控制其是否关闭退出\n
        theme_color (Optional[QColor], optional): 停靠时颜色. Defaults to QColor(30, 204, 148, 255).
    """
    def __init__(
        self, 
        parent: "MainWindow",
        theme_color: Optional[QColor] = QColor(30, 204, 148, 255)
    ) -> None:
        super().__init__()
        self.setFixedSize(24, 24)
        self._size = QSize(16, 16)
        icon = QPixmap(":/image/exit.png")
        self._icon = icon.scaled(self._size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self._icon_press = change_theme_color(icon, theme_color).scaled(self._size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self._falg = False
        
        self.clicked.connect(lambda: parent.close())
      
    def paintEvent(self, event: QPaintEvent) -> None: 
        """重绘事件

        参数:
            event (QPaintEvent): _description_
        """
        painter = QPainter(self) 
        painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        if self._falg:
            self.draw(event, painter, self._icon_press)
        else:
            self.draw(event, painter, self._icon)
            
    def draw(self, event: QPaintEvent, painter: QPainter, icon: QPixmap) -> None:
        """重绘事件方法

        参数:
            event (QPaintEvent): QPaintEvent\n
            painter (QPainter): QPainter\n
            icon (QPixmap): 按钮图标
        """
        painter.drawPixmap(
            (self.width() - self._size.width()) // 2,
            (self.height() - self._size.height()) // 2, 
            self._size.width(), 
            self._size.height(), 
            icon
        )                             
    
    def enterEvent(self, event: QEnterEvent) -> None:
        """鼠标进入事件

        参数:
            event (QEnterEvent): QEnterEvent

        返回:
            _type_: super().enterEvent(event)
        """
        self._falg = True
        return super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        """鼠标离开事件

        参数:
            event (QEvent): QEvent

        返回:
            _type_: super().leaveEvent(event)
        """
        self._falg = False
        return super().leaveEvent(event)
   
class MyTip(QWidget):
    """MainWindow上方标题栏

    参数:
        parent (MainWindow): MainWindow窗口
    """
    _h = 36
    
    def __init__(
        self,
        parent: "MainWindow"
    ) -> None:
        super().__init__()
        self.setFixedHeight(MyTip._h)
        self.moveFlag = False
        self._parent = parent
        self._logo = QPixmap(":/image/logo.png")
        self.layout = QHBoxLayout(self)
        self.layout.addStretch(1)
        self.layout.addWidget(TitlePushButtonMin(parent))
        self.max_button = TitlePushButtonMax(parent)
        self.layout.addWidget(self.max_button)
        self.layout.addWidget(TitlePushButtonExit(parent))
        self.layout.addSpacing(10)
        
    def paintEvent(self, event: QPaintEvent) -> None:
        """重绘事件

        参数:
            event (QPaintEvent): _description_
        """    
        painter = QPainter(self) 
        painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        self.draw(event, painter)
        
    def draw(self, event: QPaintEvent, painter: QPainter) -> None:
        """重绘事件方法

        参数:
            event (QPaintEvent): QPaintEvent\n
            painter (QPainter): QPainter
        """
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor("#f0f0f0"))
        w = MenuLeftSideFirst._w + 10
        h = self.height()
        painter.drawRect(0, 0, w, h)
        painter.drawPixmap(
            (w - self._logo.width()) // 2,
            (h - self._logo.height()) // 2, 
            self._logo.width(), 
            self._logo.height(),
            self._logo
        )
        
    def mousePressEvent(self, event: QMouseEvent) -> None:
        """鼠标按下事件

        参数:
            event (QMouseEvent): QMouseEvent
        """
        if self._parent.isMaximized():
            self._parent._showNormal(event.globalPosition().toPoint())
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.pos_star = event.globalPosition().toPoint()
            self.win_pos = self._parent.pos()
   
    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """鼠标移动事件

        参数:
            event (QMouseEvent): QMouseEvent
        """
        if self.moveFlag:
            self._parent.move(self.win_pos + event.globalPosition().toPoint() - self.pos_star)
            
    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        """鼠标释放事件

        参数:
            event (QMouseEvent): QMouseEvent
        """
        self.moveFlag = False
    