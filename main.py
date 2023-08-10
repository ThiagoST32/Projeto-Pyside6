from qtcore import *
from Projeto_Cadastro_Empresa import *
from Banco_Projeto import *
import sys
from img import *
import re
import pandas as pd


# from Banco_Dados import *
class MainWindow(QMainWindow):    
    
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.db = DataBase()
        self.ui.setupUi(self)
    ########################################################
    ########################################################

    #########################################################################################################################

        #Paginas Botoes
        self.ui.Btn_Inicio_as.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_home))
        self.ui.Btn_Cadastrar_as.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_Cadastrar))
        self.ui.Btn_Contato_as.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_contatos))
        self.ui.Btn_Sobre_as.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_sobre))

    #########################################################################################################################

        self.ui.Btn_Cadastrar_Empresa.clicked.connect(self.cadastro_mensagem)
        self.ui.Btn_Cadastrar_Empresa.clicked.connect(self.limparCamposCadastroEmpresa)
        self.ui.Btn_Alterar.clicked.connect(self.update_cadastro)
        self.ui.Btn_Excluir_Empresa.clicked.connect(self.delete_empresa)
        self.ui.Btn_Gerar_Excel.clicked.connect(self.gerar_execl)
        self.ui.lineEdit_Pesquisar_Empresa.textChanged.connect(self.buscar_empresa)

        self.mostrar_empresa()
    #########################################################################################################################
        #Cadastro de empresa
    def cadastro(self):
        cpnj = self.ui.lineEdit_CNPJ_Cadastro.text()
        nome = self.ui.lineEdit_Nome_Empresa_Cadastro.text()
        logradouro = self.ui.lineEdit_Logradou_Cadastro.text()
        numero = self.ui.lineEdit_Numero_Cadastro.text()
        complemento = self.ui.lineEdit_Complemento_Cadastro.text()
        bairro = self.ui.lineEdit_Bairro_Cadastro.text()
        municipio = self.ui.lineEdit_Municipio_Cadastro.text()
        uf = self.ui.lineEdit_UF_Cadasdtro.text()
        cep = self.ui.lineEdit_CEP_Cadastro.text()
        telefone = self.ui.lineEdit_Telefone_Cadastro.text()
        email = self.ui.lineEdit_Email_Cadastro.text()


        if len(cpnj) < 9 and len(nome) < 3 and len(telefone) < 10:
            result = 'erro','CNPJ,NOME,FONE'
            self.msg(result[0],result[1])
        elif len(email) < 5 and len(logradouro) < 5 and len(municipio) < 3:
            result = 'erro','EMAIL, ENDERECO,CIDADE'
            self.msg(result[0],result[1])
        else:
            qntd = (cpnj,nome,logradouro,numero,complemento,bairro,municipio,uf,cep,telefone,email)
            result = self.db.register_company(qntd)
            print(result,qntd)
        self.buscar_empresa()
    

    def cadastro_mensagem(self):
        msg = QMessageBox()
        msg.setWindowTitle("Cadastrar Empresa!!")
        msg.setText("Essa empresa será cadastrada!!")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            id = self.ui.tableWidget.selectionModel().currentIndex().siblingAtColumn(0).data()
            res = self.db.register_company(id)
            self.msg(res[0],res[1])
            self.cadastro()


    def mostrar_empresa(self):
        result = self.db.consulta_empresas()

        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.ui.tableWidget.setItem(row,column, QTableWidgetItem(str(data)))

    def buscar_empresa(self):
        txt = re.sub('[\W_]+','',self.ui.lineEdit_Pesquisar_Empresa.text())
        res = self.db.buscar_empresas(txt)

        self.ui.tableWidget.setRowCount(len(res))

        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(len(res))

        for row, text in enumerate(res):
            for column, data in enumerate(text):
                self.ui.tableWidget.setItem(row,column, QTableWidgetItem(str(data)))
        

    def alterar_empresa(self,campo):

        campo = []
        update_dados = []

        for row in range(self.ui.tableWidget.rowCount()):
            for column in range(self.ui.tableWidget.columnCount()):
                campo.append(self.ui.tableWidget.item(row, column).text())
            update_dados.append(campo)
            campo = []

        for emp in update_dados:
           res = self.db.alterar_empresa(tuple(emp))

        self.msg(res[0],res[1])

    def update_cadastro(self, campo):
        msg = QMessageBox()
        msg.setWindowTitle("Alterar Cadastro")
        msg.setText("Este Cadastro será Alterado!")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            id = self.ui.tableWidget.selectionModel().currentIndex().siblingAtColumn(0).data()
            res = self.db.alterar_empresa(id)
            self.msg(res[0],res[1])
            self.alterar_empresa(campo)



    def delete_empresa(self):
        msg = QMessageBox()
        msg.setWindowTitle("Deletar Cadastro")
        msg.setText("Este Cadastro será Deletado!")
        msg.setInformativeText("Você tem certeza que deseja continuar?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            id = self.ui.tableWidget.selectionModel().currentIndex().siblingAtColumn(0).data()
            res = self.db.delete_empresa(id)
            self.msg(res[0],res[1])
            self.buscar_empresa()
















    def msg(self,tipo,mensagem):
        msg = QMessageBox()
        if tipo.lower() == 'Tudo OK!!!':
            msg.setIcon(QMessageBox.Information)
        elif tipo.lower() == 'Um erro foi encontrado!!!!':
            msg.setIcon(QMessageBox.Critical)
        elif tipo.lower() == 'Algo está errado (aviso)!!!!':
            msg.setIcon(QMessageBox.Warning)
        
        msg.setText(mensagem)
        msg.exec()
        # self.clean()


    def gerar_execl(self):

        dados = []
        all_dados = []

        for row in range (self.ui.tableWidget.rowCount()):
            for column in range (self.ui.tableWidget.columnCount()):
                dados.append(self.ui.tableWidget.item(row,column).text())

            all_dados.append(dados)
            dados = []
        columns = ['id_empresa','cnpj','nome','logradouro','numero','complemento','bairro','municipio','uf','cep','telefone','email']


        empresas = pd.DataFrame(all_dados, columns= columns)
        empresas.to_excel("Empresas.xlsx",sheet_name='empresas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Exel")
        msg.setText("Relatorio gerado com sucesso!!")
        msg.exec()

    def limparCamposCadastroEmpresa(self):
        self.ui.lineEdit_CNPJ_Cadastro.setText("")
        self.ui.lineEdit_Nome_Empresa_Cadastro.setText("")
        self.ui.lineEdit_Logradou_Cadastro.setText("")
        self.ui.lineEdit_Numero_Cadastro.setText("")
        self.ui.lineEdit_Complemento_Cadastro.setText("")
        self.ui.lineEdit_Bairro_Cadastro.setText("")
        self.ui.lineEdit_Municipio_Cadastro.setText("")
        self.ui.lineEdit_UF_Cadasdtro.setText("")
        self.ui.lineEdit_CEP_Cadastro.setText("")
        self.ui.lineEdit_Telefone_Cadastro.setText("")
        self.ui.lineEdit_Email_Cadastro.setText("")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() 
    app.exec()