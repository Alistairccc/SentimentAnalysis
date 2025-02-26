import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QListWidget
from PyQt5.QtGui import QPalette, QColor


class GitHubLikeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.is_dark_mode = False
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setWindowTitle('GitHub首页')
        self.setGeometry(100, 100, 600, 400)

        # 创建主垂直布局
        main_layout = QVBoxLayout()
        # 设置主布局背景颜色（初始为浅色）
        self.setStyleSheet("background-color: #303030;")

        # 创建标题
        title_label = QLabel('欢迎来到类似 GitHub 的界面')
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; margin: 20px; color: #333333;")
        main_layout.addWidget(title_label)

        # 创建按钮和列表的水平布局
        button_list_layout = QHBoxLayout()

        # 创建添加项目按钮
        add_button = QPushButton('添加项目')
        add_button.setStyleSheet("""
            background-color: #f0f0f0;
            color: #333333;
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
        """)
        add_button.clicked.connect(self.add_project)
        button_list_layout.addWidget(add_button)

        # 创建切换深色模式按钮
        dark_mode_button = QPushButton('切换深色模式')
        dark_mode_button.setStyleSheet("""
            background-color: #f0f0f0;
            color: #333333;
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
        """)
        dark_mode_button.clicked.connect(self.toggle_dark_mode)
        button_list_layout.addWidget(dark_mode_button)

        # 创建列表
        self.project_list = QListWidget()
        self.project_list.setStyleSheet("""
            background-color: #ffffff;
            color: #333333;
        """)
        button_list_layout.addWidget(self.project_list)

        # 将水平布局添加到主垂直布局中
        main_layout.addLayout(button_list_layout)

        # 设置主布局
        self.setLayout(main_layout)

    def add_project(self):
        # 获取当前列表中的项目数量
        item_count = self.project_list.count()
        # 生成新的项目名称
        new_project = f'项目 {item_count + 1}'
        # 将新项目添加到列表中
        self.project_list.addItem(new_project)

    def toggle_dark_mode(self):
        if self.is_dark_mode:
            # 切换到浅色模式
            self.setStyleSheet("background-color: #ffffff;")
            self.setWindowTitle('类似 GitHub 首页示例 - 浅色模式')
            self.update_stylesheet_to_light()
        else:
            # 切换到深色模式
            self.setStyleSheet("background-color: #303030;")
            self.setWindowTitle('类似 GitHub 首页示例 - 深色模式')
            self.update_stylesheet_to_dark()
        self.is_dark_mode = not self.is_dark_mode

    def update_stylesheet_to_dark(self):
        title_style = "font-size: 24px; font-weight: bold; margin: 20px; color: #cccccc;"
        button_style = """
            background-color: #444444;
            color: #cccccc;
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
        """
        list_style = """
            background-color: #333333;
            color: #cccccc;
        """
        self.findChild(QLabel).setStyleSheet(title_style)
        buttons = self.findChildren(QPushButton)
        for button in buttons:
            button.setStyleSheet(button_style)
        self.findChild(QListWidget).setStyleSheet(list_style)

    def update_stylesheet_to_light(self):
        title_style = "font-size: 24px; font-weight: bold; margin: 20px; color: #333333;"
        button_style = """
            background-color: #f0f0f0;
            color: #333333;
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
        """
        list_style = """
            background-color: #ffffff;
            color: #333333;
        """
        self.findChild(QLabel).setStyleSheet(title_style)
        buttons = self.findChildren(QPushButton)
        for button in buttons:
            button.setStyleSheet(button_style)
        self.findChild(QListWidget).setStyleSheet(list_style)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GitHubLikeWindow()
    window.show()
    sys.exit(app.exec_())