import sys

from PyQt5.QtWidgets import QWidget, QApplication  # QtWidgets包含一整套UI元素控件,

# QWidget所有用户界面对象的基类。QApplication用于管理用户界面应用程序的控制流和主要设置。

if __name__ == "__main__":
    # 创建QApplication类的实例
    app = QApplication(sys.argv)  # sys.argv用于识别命令行，
    # 创建一个窗口
    w = QWidget()
    # 设置窗口的尺寸
    w.resize(400, 200)
    # 移动窗口
    w.move(300, 300)
    # 设置窗口的标题
    w.setWindowTitle("第一个基于PyQt5的桌面应用")
    # 显示窗口
    w.show()

    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())