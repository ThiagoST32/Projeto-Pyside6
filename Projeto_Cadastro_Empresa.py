# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Projeto_Cadastro_CursofMMcSB.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from img import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1620, 754)
        MainWindow.setStyleSheet(u"background-color: rgb(104, 104, 104);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"border:none\n"
"}\n"
"\n"
"QLabel{\n"
"color:#fff\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left_Container = QFrame(self.centralwidget)
        self.left_Container.setObjectName(u"left_Container")
        self.left_Container.setMaximumSize(QSize(300, 16777215))
        self.left_Container.setFrameShape(QFrame.StyledPanel)
        self.left_Container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.left_Container)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.frame_2 = QFrame(self.left_Container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(113, 113, 113);\n"
"}\n"
"QToolBox{\n"
"text-align:left;\n"
"	background-color: rgb(228, 254, 255);\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"border-radius:5px;\n"
"background-color:rgb(194,232,255);\n"
"text-align:left;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.toolBox = QToolBox(self.frame_2) ##############
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(65,65,65);\n"
"}\n"
"\n"
"QPushButton{\n"
"color:rgb(255,255,255);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 255, 676))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Btn_Inicio_as = QPushButton(self.page)
        self.Btn_Inicio_as.setObjectName(u"Btn_Inicio_as")
        self.Btn_Inicio_as.setMinimumSize(QSize(0, 30))
        self.Btn_Inicio_as.setSizeIncrement(QSize(0, 0))
        font = QFont()
        font.setPointSize(12)
        self.Btn_Inicio_as.setFont(font)
        self.Btn_Inicio_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.Btn_Inicio_as)

        self.Btn_Cadastrar_as = QPushButton(self.page)
        self.Btn_Cadastrar_as.setObjectName(u"Btn_Cadastrar_as")
        self.Btn_Cadastrar_as.setMinimumSize(QSize(0, 30))
        self.Btn_Cadastrar_as.setSizeIncrement(QSize(0, 0))
        self.Btn_Cadastrar_as.setFont(font)
        self.Btn_Cadastrar_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.Btn_Cadastrar_as)

        self.Btn_Sobre_as = QPushButton(self.page)
        self.Btn_Sobre_as.setObjectName(u"Btn_Sobre_as")
        self.Btn_Sobre_as.setMinimumSize(QSize(0, 30))
        self.Btn_Sobre_as.setSizeIncrement(QSize(0, 0))
        self.Btn_Sobre_as.setFont(font)
        self.Btn_Sobre_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.Btn_Sobre_as)

        self.Btn_Contato_as = QPushButton(self.page)
        self.Btn_Contato_as.setObjectName(u"Btn_Contato_as")
        self.Btn_Contato_as.setMinimumSize(QSize(0, 30))
        self.Btn_Contato_as.setSizeIncrement(QSize(0, 0))
        self.Btn_Contato_as.setFont(font)
        self.Btn_Contato_as.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.Btn_Contato_as)

        self.label_Nome_User = QLabel(self.page)
        self.label_Nome_User.setObjectName(u"label_Nome_User")

        self.verticalLayout_4.addWidget(self.label_Nome_User)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.page_2 = QWidget() ############
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 255, 676))
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_5.addWidget(self.label_4)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.left_Container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.frame)


        self.gridLayout_2.addWidget(self.left_Container, 0, 0, 1, 1)

        self.Main_Container = QFrame(self.centralwidget)
        self.Main_Container.setObjectName(u"Main_Container")
        self.Main_Container.setFrameShape(QFrame.StyledPanel)
        self.Main_Container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Main_Container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.Main_Container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.top_frame)
        self.Btn_Toggle.setObjectName(u"Btn_Toggle")
        self.Btn_Toggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Toggle.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/single-user-icon-png-free--rLHSHx.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.Btn_Toggle, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        self.label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.Main_Container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"background-color: rgb(62,62,62)")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 9, 0, 0)
        self.stackedWidget = QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_sobre = QWidget()
        self.page_sobre.setObjectName(u"page_sobre")
        self.horizontalLayout_6 = QHBoxLayout(self.page_sobre)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_GitHub = QLabel(self.page_sobre)
        self.label_GitHub.setObjectName(u"label_GitHub")

        self.horizontalLayout_6.addWidget(self.label_GitHub)

        self.horizontalSpacer = QSpacerItem(135, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.label_Instagram = QLabel(self.page_sobre)
        self.label_Instagram.setObjectName(u"label_Instagram")

        self.horizontalLayout_6.addWidget(self.label_Instagram)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.label_Email = QLabel(self.page_sobre)
        self.label_Email.setObjectName(u"label_Email")

        self.horizontalLayout_6.addWidget(self.label_Email)

        self.horizontalSpacer_2 = QSpacerItem(135, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.label_LinkeDin = QLabel(self.page_sobre)
        self.label_LinkeDin.setObjectName(u"label_LinkeDin")

        self.horizontalLayout_6.addWidget(self.label_LinkeDin)

        self.verticalSpacer_8 = QSpacerItem(20, 640, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_6.addItem(self.verticalSpacer_8)

        self.stackedWidget.addWidget(self.page_sobre)

        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.label_2 = QLabel(self.page_home)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(9, 9, 471, 591))
        self.label_2.setMinimumSize(QSize(471, 591))
        self.label_2.setMaximumSize(QSize(471, 591))
        self.label_2.setPixmap(QPixmap(u"../../Thiago Codigos/imgengs/Torii City by Michal Kv\u00e1\u010d.png"))
        self.stackedWidget.addWidget(self.page_home)
        self.page_contatos = QWidget()
        self.page_contatos.setObjectName(u"page_contatos")
        self.horizontalLayout_7 = QHBoxLayout(self.page_contatos)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.page_contatos)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.page_contatos)
        self.page_Cadastrar = QWidget()
        self.page_Cadastrar.setObjectName(u"page_Cadastrar")
        self.verticalLayout_8 = QVBoxLayout(self.page_Cadastrar)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 9, 0, 0)
        self.tabWidget = QTabWidget(self.page_Cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.Cadastro = QWidget()
        self.Cadastro.setObjectName(u"Cadastro")
        self.verticalLayout_7 = QVBoxLayout(self.Cadastro)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_5 = QFrame(self.Cadastro)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_Empresas_Cadastro = QLabel(self.frame_5)
        self.label_Empresas_Cadastro.setObjectName(u"label_Empresas_Cadastro")
        self.label_Empresas_Cadastro.setGeometry(QRect(130, 50, 211, 101))

        self.verticalLayout_7.addWidget(self.frame_5)
        self.page_Cadastrar = QWidget()
        self.page_Cadastrar.setObjectName(u"page_Cadastrar")
        self.verticalLayout_8 = QVBoxLayout(self.page_Cadastrar)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 9, 0, 0) ########
        self.tabWidget = QTabWidget(self.page_Cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.Cadastro = QWidget()
        self.Cadastro.setObjectName(u"Cadastro")
        self.verticalLayout_7 = QVBoxLayout(self.Cadastro)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_5 = QFrame(self.Cadastro)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_Empresas_Cadastro = QLabel(self.frame_5)
        self.label_Empresas_Cadastro.setObjectName(u"label_Empresas_Cadastro")
        self.label_Empresas_Cadastro.setGeometry(QRect(130, 50, 211, 101))

        self.verticalLayout_7.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.Cadastro)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(113, 113, 113);\n"
"	height:30px;\n"
"	color: rgb(255, 255,255);\n"
"	border-radius: 30px;\n"
"	font-weight:800;\n"
"}\n"
"\n"
"\n"
"QFrame{\n"
"background-color: rgb(62,62,62);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_10.setContentsMargins(9, 0, 9, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)

        self.label_Cadastro_Empresa = QLabel(self.frame_4)
        self.label_Cadastro_Empresa.setObjectName(u"label_Cadastro_Empresa")
        font2 = QFont()
        font2.setPointSize(50)
        self.label_Cadastro_Empresa.setFont(font2)
        self.label_Cadastro_Empresa.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout_10.addWidget(self.label_Cadastro_Empresa, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.lineEdit_Nome_Empresa_Cadastro = QLineEdit(self.frame_4)
        self.lineEdit_Nome_Empresa_Cadastro.setObjectName(u"lineEdit_Nome_Empresa_Cadastro")
        self.lineEdit_Nome_Empresa_Cadastro.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 30px;\n"
"	\n"
"}")

        self.verticalLayout_10.addWidget(self.lineEdit_Nome_Empresa_Cadastro)

        self.lineEdit_CNPJ_Cadastro = QLineEdit(self.frame_4)
        self.lineEdit_CNPJ_Cadastro.setObjectName(u"lineEdit_CNPJ_Cadastro")

        self.verticalLayout_10.addWidget(self.lineEdit_CNPJ_Cadastro)

        self.lineEdit_Logradou_Cadastro = QLineEdit(self.frame_4)
        self.lineEdit_Logradou_Cadastro.setObjectName(u"lineEdit_Logradou_Cadastro")

        self.verticalLayout_10.addWidget(self.lineEdit_Logradou_Cadastro)

        self.lineEdit_Complemento_Cadastro = QLineEdit(self.frame_4)
        self.lineEdit_Complemento_Cadastro.setObjectName(u"lineEdit_Complemento_Cadastro")

        self.verticalLayout_10.addWidget(self.lineEdit_Complemento_Cadastro)

        self.lineEdit_Numero_Cadastro = QLineEdit(self.frame_4)
        self.lineEdit_Numero_Cadastro.setObjectName(u"lineEdit_Numero_Cadastro")

        self.verticalLayout_10.addWidget(self.lineEdit_Numero_Cadastro)

        self.lineEdit_Bairro_Cadastro = QLineEdit(self.frame_4)
        self.lineEdit_Bairro_Cadastro.setObjectName(u"lineEdit_Bairro_Cadastro")

        self.verticalLayout_10.addWidget(self.lineEdit_Bairro_Cadastro)

        self.lineEdit_UF_Cadasdtro = QLineEdit(self.frame_4)
        self.lineEdit_UF_Cadasdtro.setObjectName(u"lineEdit_UF_Cadasdtro")

        self.verticalLayout_10.addWidget(self.lineEdit_UF_Cadasdtro)

        self.lineEdit_Municipio_Cadastro = QLineEdit(self.frame_4)
        self.lineEdit_Municipio_Cadastro.setObjectName(u"lineEdit_Municipio_Cadastro")

        self.verticalLayout_10.addWidget(self.lineEdit_Municipio_Cadastro)

        self.lineEdit_CEP_Cadastro = QLineEdit(self.frame_4)
        self.lineEdit_CEP_Cadastro.setObjectName(u"lineEdit_CEP_Cadastro")

        self.verticalLayout_10.addWidget(self.lineEdit_CEP_Cadastro)

        self.lineEdit_Email_Cadastro = QLineEdit(self.frame_4)
        self.lineEdit_Email_Cadastro.setObjectName(u"lineEdit_Email_Cadastro")

        self.verticalLayout_10.addWidget(self.lineEdit_Email_Cadastro)

        self.lineEdit_Telefone_Cadastro = QLineEdit(self.frame_4)
        self.lineEdit_Telefone_Cadastro.setObjectName(u"lineEdit_Telefone_Cadastro")

        self.verticalLayout_10.addWidget(self.lineEdit_Telefone_Cadastro)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.horizontalSpacer_3 = QSpacerItem(1264, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_7.addItem(self.horizontalSpacer_3)

        self.Btn_Cadastrar_Empresa = QPushButton(self.Cadastro)
        self.Btn_Cadastrar_Empresa.setObjectName(u"Btn_Cadastrar_Empresa")
        self.Btn_Cadastrar_Empresa.setMinimumSize(QSize(120, 30))
        self.Btn_Cadastrar_Empresa.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Cadastrar_Empresa.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(49,147,0);\n"
"\n"
"\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(113, 113, 113);\n"
"}")

        self.verticalLayout_7.addWidget(self.Btn_Cadastrar_Empresa)

        self.tabWidget.addTab(self.Cadastro, "")
        self.Empresas = QWidget()
        self.Empresas.setObjectName(u"Empresas")
        self.verticalLayout_9 = QVBoxLayout(self.Empresas)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_Empresa = QLabel(self.Empresas)
        self.label_Empresa.setObjectName(u"label_Empresa")
        self.label_Empresa.setStyleSheet(u"")
        self.label_Empresa.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_9.addWidget(self.label_Empresa)

        self.label_Buscar_Empresa = QLabel(self.Empresas)
        self.label_Buscar_Empresa.setObjectName(u"label_Buscar_Empresa")
        font3 = QFont()
        font3.setPointSize(25)
        self.label_Buscar_Empresa.setFont(font3)

        self.verticalLayout_9.addWidget(self.label_Buscar_Empresa)

        self.lineEdit_Pesquisar_Empresa = QLineEdit(self.Empresas)
        self.lineEdit_Pesquisar_Empresa.setObjectName(u"lineEdit_Pesquisar_Empresa")
        self.lineEdit_Pesquisar_Empresa.setMaximumSize(QSize(500, 30))
        self.lineEdit_Pesquisar_Empresa.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(113, 113, 113);\n"
"	height:20px;\n"
"	color: rgb(255, 255,255);\n"
"	border-radius: 30px;\n"
"	font-weight:800;\n"
"}")

        self.verticalLayout_9.addWidget(self.lineEdit_Pesquisar_Empresa)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 0, -1)
        self.tableWidget = QTableWidget(self.Empresas)
        if (self.tableWidget.columnCount() < 12):
            self.tableWidget.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"background-color:rgb(148,148,148);\n"
"color:rgb(255,255,255);\n"
"}\n"
"\n"
"QTableWidget{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(62,62,62);\n"
"}")

        self.horizontalLayout_5.addWidget(self.tableWidget)

        self.frame_3 = QFrame(self.Empresas)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(199, 360))
        self.frame_3.setMaximumSize(QSize(199, 360))
        self.frame_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"border-radius:15px;\n"
"background-color: rgb(113, 113, 113);\n"
"color:rgb(0,24,74);\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgb(62,62,62);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Btn_Gerar_Excel = QPushButton(self.frame_3)
        self.Btn_Gerar_Excel.setObjectName(u"Btn_Gerar_Excel")
        self.Btn_Gerar_Excel.setMinimumSize(QSize(120, 30))
        self.Btn_Gerar_Excel.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(49,147,0);\n"
"}")

        self.verticalLayout_2.addWidget(self.Btn_Gerar_Excel)

        self.Btn_Alterar = QPushButton(self.frame_3)
        self.Btn_Alterar.setObjectName(u"Btn_Alterar")
        self.Btn_Alterar.setMinimumSize(QSize(120, 30))
        self.Btn_Alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Alterar.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(49,147,0);\n"
"}")

        self.verticalLayout_2.addWidget(self.Btn_Alterar)

        self.Btn_Excluir_Empresa = QPushButton(self.frame_3)
        self.Btn_Excluir_Empresa.setObjectName(u"Btn_Excluir_Empresa")
        self.Btn_Excluir_Empresa.setMinimumSize(QSize(120, 30))
        self.Btn_Excluir_Empresa.setCursor(QCursor(Qt.PointingHandCursor))
        self.Btn_Excluir_Empresa.setStyleSheet(u"QPushButton:hover{\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(49,147,0);\n"
"}")

        self.verticalLayout_2.addWidget(self.Btn_Excluir_Empresa)

        self.verticalSpacer_2 = QSpacerItem(20, 231, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.Empresas, "")
        self.lineEdit_Pesquisar_Empresa.raise_()
        self.label_Empresa.raise_()
        self.label_Buscar_Empresa.raise_()

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.stackedWidget.addWidget(self.page_Cadastrar)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.Main_Container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_User_Footer = QLabel(self.footer_frame)
        self.label_User_Footer.setObjectName(u"label_User_Footer")

        self.horizontalLayout_3.addWidget(self.label_User_Footer, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.footer_frame)


        self.gridLayout_2.addWidget(self.Main_Container, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Btn_Inicio_as.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.Btn_Cadastrar_as.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.Btn_Sobre_as.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.Btn_Contato_as.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Botões Sistema", None))
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Usuario: Thiago</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Sistema: Cadastro</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Status:Ativo</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Venc:12/12/3000</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Usuario: Root</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Sistema: Cadastro</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Status: Ativo</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Venc: 12/12/3000</span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"User", None))
        self.Btn_Toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sistema de Cadastro", None))
        self.label_GitHub.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">GitHub</span></p><p align=\"center\"><a href=\"https://github.com/ThiagoST32\"><span style=\" font-size:18pt; color:#ffffff;\">ThiagoST32</span></a></p></body></html>", None))
        self.label_Instagram.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Instagram</span></p><p align=\"center\"><a href=\"https://www.instagram.com/thyago6554/?hl=pt-br\"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">@thyago6554</span></a></p></body></html>", None))
        self.label_Email.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Email</span></p><p align=\"center\"><span style=\" font-size:18pt;\">thiago.sandre.trevisan@gmail.com</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.label_LinkeDin.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">LinkeDin</span></p><p align=\"center\"><a href=\"www.linkedin.com/in/thiago-sandre-840a23270  \"><span style=\" font-size:18pt; text-decoration: underline; color:#ffffff;\">Perfil LinkeDin</span></a></p></body></html>", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Projeto Feito em Pyside6 juntamente com</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Python e Mysql<br/>Onde o objetivo do sistema \u00e9 o basico</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Cadastrar</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Editar </span></p><p align=\"center\"><span style=\" font-size:18pt;\">Excluir</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Listar </span></p><p align=\"center\"><span style=\" font-size:18pt;\">Procurar</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Feito por Thiago Sandre Trevisan</span><br/></p></body></html>", None))
        self.label_Cadastro_Empresa.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Cadastro Empresa</p></body></html>", None))
        self.lineEdit_Nome_Empresa_Cadastro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome Empresarial", None))
        self.lineEdit_Bairro_Cadastro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.lineEdit_CNPJ_Cadastro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.lineEdit_CEP_Cadastro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.lineEdit_Complemento_Cadastro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.lineEdit_Logradou_Cadastro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.lineEdit_Numero_Cadastro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Numero", None))
        self.lineEdit_Email_Cadastro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit_Municipio_Cadastro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Municipio", None))
        self.lineEdit_UF_Cadasdtro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.lineEdit_Telefone_Cadastro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.Btn_Cadastrar_Empresa.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Cadastro), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_Empresa.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:18pt;\">Empresas</span></p></body></html>", None))
        self.label_Buscar_Empresa.setText(QCoreApplication.translate("MainWindow", u"Buscar Empresa ", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_Pesquisar_Empresa.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_Pesquisar_Empresa.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID Empresa", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"MUNICIPIO", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        self.Btn_Gerar_Excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.Btn_Alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.Btn_Excluir_Empresa.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Empresas), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.label_User_Footer.setText(QCoreApplication.translate("MainWindow", u"Cadastro Empresas!!!!!!!!!!!!!", None))
    # retranslateUi


