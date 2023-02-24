from PyQt5 import uic, QtWidgets
import sys
import os #importa a biblioteca necessária para manipulação do S.O.
import mysql.connector #Importa o conector para o python se comunicar com o BD
import datetime

os.system("pip install mysql-connector-python") #Faz a instalação do conector MySQL

def conectarBD(host, usuario, senha, DB):
    connection = mysql.connector.connect( #Informando os dados para conexão com o BD
        host = host, #ip do servidor do BD
        user= usuario, #Usuário do MySQL 
        password=senha, #Senha do usuário do MySQL
        database=DB  #nome do DB criado
    ) #Define o banco de dados usado

    return connection

#INSERT
def insert_BD():
    connection = conectarBD("localhost","root", #adicione sua senha do banco de dados, "projeto") #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco[]
    nome = telaCliente.txtnomecliente.text()
    cpf = telaCliente.txtcpf.text()
    email = telaCliente.txtemail.text()
    telefone = telaCliente.txttelefone.text()
    endereco =  telaCliente.txtendereco.text() + " " + telaCliente.txtnumero.text() 
    id_animal = telaCliente.txtidanimal.text() 
    



    
    sql = "INSERT INTO clientes (nome, cpf,email,telefone, endereco, id_animal) VALUES (%s, %s,%s,%s, %s, %s)"
    data = (
    nome,
    cpf,
    email,
    telefone,
    endereco,
    id_animal
    )

    

    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit() #Efetua as modificações

    

    userid = cursor.lastrowid #Obtém o último ID cadastrado

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o BD

    QtWidgets.QMessageBox.about( telaCliente, 'SUCESSO!',"Foi cadastrado o novo Cliente de ID:  " + str(userid))


def insert_BD2():
    connection = conectarBD("localhost","root", " #adicione sua senha do banco de dados", "projeto") #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    nome = telaAnimal.txtnomeanimal.text()
    data_nasc= telaAnimal.txtdataanimal.text()
    peso = telaAnimal.txtpeso.text()
    cor = telaAnimal.txtcor.text()
    id_especies = telaAnimal.txtidespecie.text()
       

    sql2 = "INSERT INTO Animais (nome,data_nasc,peso,cor,id_especies) values (%s,%s,%s,%s,%s)"
    data2 = (
    nome,
    data_nasc,
    peso,
    cor,
    id_especies

    ) 

    cursor.execute(sql2,data2)
    connection.commit() 
  
    userid = cursor.lastrowid #Obtém o último ID cadastrado

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o BD

    QtWidgets.QMessageBox.about(telaAnimal , 'SUCESSO!',"Foi cadastrado o novo Animal de ID: " + str(userid))      

def read_BD():
    connection = conectarBD("localhost","root", " #adicione sua senha do banco de dados", "projeto") #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    



    sql = "SELECT clientes.CPF, clientes.nome,clientes.telefone,clientes.email, clientes.endereco, Animais.nome,Animais.id   FROM clientes , Animais where clientes.CPF =" + telaConsultaCliente.txtcpfconsulta.text()#Realizando um select para mostrar todas as linhas e colunas da tabela
    

    cursor.execute(sql) #Executa o comando SQL
    results = cursor.fetchall() #Obtém todas as linhas no conjunto de resultados da consulta
    for row in results:
        telaConsultaCliente.txtcpfconsulta.setText(row[0])
        telaConsultaCliente.txtNomeconsulta.setText(row[1])
        telaConsultaCliente.txttelefone.setText(row[2])
        telaConsultaCliente.txtemail.setText(row[3])
        telaConsultaCliente.txtenderecoconsulta.setText(row[4])
        telaConsultaCliente.txtnomeanimal2.setText((row[5]))
        telaConsultaCliente.txtidanimal2.setText(str(row[6]))


   
    cursor.close() #fecha o cursor
    connection.close() #Fecha a conexão com o banco

def read_BD2():
    connection = conectarBD("localhost","root", " #adicione sua senha do banco de dados", "projeto") #Recebe a conexão estabelecida com o banco
    cursor = connection.cursor() #Cursor para comunicação com o banco

    

    sql2 = "SELECT Animais.nome, Animais.data_nasc, Animais.peso, Animais.cor, especies.nome, clientes.nome, clientes.cpf  FROM  clientes ,  animais, especies where Animais.id =" + telaConsultaAnimal.txtid.text() + " and Animais.id_especies = especies.id and clientes.id_animal = Animais.id" #Realizando um select para mostrar todas as linhas e colunas da tabela
    
    
    cursor.execute(sql2)
    results2 = cursor.fetchall()
    for row in results2:
        telaConsultaAnimal.txtnomeconsultar.setText(row[0])
        telaConsultaAnimal.txtdataconsultar.setText(row[1])  
        telaConsultaAnimal.txtpesoconsultar.setText(str(row[2]))
        telaConsultaAnimal.txtcorconsultar.setText(row[3])
        telaConsultaAnimal.txtespecie.setText(row[4])
        telaConsultaAnimal.txtresponsavel.setText(row[5])
        telaConsultaAnimal.txtcpfresponsavel.setText(row[6])
     

    cursor.close() #fecha o cursor
    connection.close() #Fecha a conexão com o banco





def Delete_DB():
    connection = conectarBD("localhost","root", " #adicione sua senha do banco de dados", "projeto")
    cursor = connection.cursor()

    id = telaConsultaAnimal.txtid.text()

    sql = "DELETE FROM Animais WHERE id = %s " 

    data = (id,)

    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit() #Efetua as modificações

    recordsaffected = cursor.rowcount #Obtém o número de linhas afetadas

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    print(recordsaffected, " registros excluídos")
    QtWidgets.QMessageBox.about( telaConsultaAnimal, 'SUCESSO!'," Registros deletados!!")


def Delete_DB2():
    connection = conectarBD("localhost","root", " #adicione sua senha do banco de dados", "projeto")
    cursor = connection.cursor()

    CPF = telaConsultaCliente.txtcpfconsulta.text()

    

    sql2 = "DELETE FROM clientes WHERE CPF = %s " 

    data2 = (CPF,)

    cursor.execute(sql2,data2) #Executa o comando SQL
    connection.commit() #Efetua as modificações

    recordsaffected = cursor.rowcount #Obtém o número de linhas afetadas

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    print(recordsaffected, " registros excluídos")
    QtWidgets.QMessageBox.about( telaConsultaCliente, 'SUCESSO!'," Registros deletados!!")


def Update_DB ():
    connection = conectarBD("localhost","root", " #adicione sua senha do banco de dados", "projeto")
    cursor = connection.cursor()
    nome = telaAnimal.txtnomeanimal.text()
    data_nasc = telaAnimal.txtdataanimal.text()
    peso = telaAnimal.txtpeso.text()
    cor = telaAnimal.txtcor.text()
    id_especies = telaAnimal.txtidespecie.text()
    
    sql2 = "UPDATE Animais SET nome = %s, data_nasc = %s, peso = %s, cor = %s, id_especies = %s WHERE nome = %s "
   
    data2 = (nome,data_nasc,peso,cor, id_especies,nome)
    
    cursor.execute(sql2, data2) #Executa o comando SQL
    connection.commit()  #Efetua as modificações

    recordsaffected = cursor.rowcount #Obtém o número de linhas afetadas

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    print(recordsaffected, " registros alterados")
    QtWidgets.QMessageBox.about( telaAnimal,"Sucesso!!", " Registros alterados!!")     

def Update_DB2 ():
    connection = conectarBD("localhost","root", " #adicione sua senha do banco de dados", "projeto")
    cursor = connection.cursor()
    
    nome = telaCliente.txtnomecliente.text()
    CPF = telaCliente.txtcpf.text()
    telefone = telaCliente.txttelefone.text()
    email = telaCliente.txtemail.text()
    endereco = telaCliente.txtendereco.text()+" "+telaCliente.txtnumero.text()
    id_animal = telaCliente.txtidanimal.text()


    sql = "UPDATE clientes SET nome = %s, CPF = %s, telefone = %s, email = %s, endereco = %s, id_animal = %s  WHERE CPF = %s " 
   
    data = (nome,CPF,telefone,email,endereco,id_animal,CPF)
    
    cursor.execute(sql, data) #Executa o comando SQL
    connection.commit()  #Efetua as modificações

    recordsaffected = cursor.rowcount #Obtém o número de linhas afetadas

    cursor.close() #Fecha o cursor
    connection.close() #Fecha a conexão com o banco

    print(recordsaffected, " registros alterados") 
    QtWidgets.QMessageBox.about( telaCliente,"Sucesso!!" ," Registros alterados!!")      




   




def Limpar(): #Função usada para limpar o texto das caixas de texto
    telaCliente.txtnomecliente.setText("")
    telaCliente.txtcpf.setText("")
    telaCliente.txtemail.setText("")
    telaConsultaCliente.txtemail.setText("")
    telaCliente.txttelefone.setText("")
    telaConsultaCliente.txttelefone.setText("")
    telaCliente.txtendereco.setText("")
    telaCliente.txtnumero.setText("")
    telaAnimal.txtnomeanimal.setText("")
    telaAnimal.txtdataanimal.setText("")
    telaAnimal.txtpeso.setText("")
    telaAnimal.txtcor.setText("")
    telaConsultaCliente.txtcpfconsulta.setText("")
    telaConsultaCliente.txtNomeconsulta.setText("")
    telaConsultaCliente.txtenderecoconsulta.setText("")
    telaConsultaCliente.txtnomeanimal2.setText("")
    telaConsultaCliente.txtidanimal2.setText("")
    telaConsultaAnimal.txtid.setText("")
    telaConsultaAnimal.txtnomeconsultar.setText("")
    telaConsultaAnimal.txtdataconsultar.setText("")
    telaConsultaAnimal.txtpesoconsultar.setText("")
    telaConsultaAnimal.txtcorconsultar.setText("")
    telaConsultaAnimal.txtespecie.setText("")
    telaConsultaAnimal.txtresponsavel.setText("")
    telaConsultaAnimal.txtcpfresponsavel.setText("")
    telaCliente.txtidanimal.setText("")
    telaAnimal.txtidespecie.setText("")
  



def AbrirMenuAnimal():
    telaMenuAnimal.show()
    telaMenuPrincipal.close()

def AbrirMenuCliente():
    telaMenuCliente.show()
    telaMenuPrincipal.close()

def AbrirMenuCadastroCliente():
    telaCliente.show()
    telaMenuCliente.close()


def AbrirMenuCadastroAnimal():
    telaAnimal.show()
    telaMenuAnimal.close()


def AbriMenuConsultaAnimal():
    telaConsultaAnimal.show()
    telaMenuAnimal.close()

def AbrirMenuConsultaCliente():
    telaConsultaCliente.show()
    telaMenuCliente.close()

def VoltarMenuPrincipal():

    telaMenuPrincipal.show()
    telaMenuAnimal.close()
    telaMenuCliente.close()



def VoltarTelaMenuCliente():

    telaMenuCliente.show()
    telaConsultaCliente.close()
    telaCliente.close()



def VoltarTelaMenuAnimal():

    telaMenuAnimal.show()
    telaConsultaAnimal.close()
    telaAnimal.close()



        

    


app = QtWidgets.QApplication(sys.argv)
telaCliente = uic.loadUi('TelaCadastroCliente.ui')
telaAnimal = uic.loadUi('TelaCadastroAnimais.ui')
telaConsultaCliente = uic.loadUi('TelaConsultaCliente.ui')
telaConsultaAnimal = uic.loadUi('TelaConsultarAnimal.ui')
telaMenuPrincipal = uic.loadUi('TelaMenuPrincipal.ui')
telaMenuCliente = uic.loadUi('TelaMenuCliente.ui')
telaMenuAnimal = uic.loadUi('TelaMenuAnimal.ui')



telaMenuPrincipal.show()
telaMenuPrincipal.btnAnimal.clicked.connect(AbrirMenuAnimal)
telaMenuPrincipal.btnCliente.clicked.connect(AbrirMenuCliente)

telaMenuCliente.btncadastroclientemenu_2.clicked.connect(AbrirMenuCadastroCliente)
telaMenuCliente.btnconsultarclientemenu_2.clicked.connect(AbrirMenuConsultaCliente)
telaMenuAnimal.btncadastroanimalmenu.clicked.connect(AbrirMenuCadastroAnimal)
telaMenuAnimal.btnconsultaranimalmenu.clicked.connect(AbriMenuConsultaAnimal)

telaMenuCliente.btnvoltarmenuprincipal.clicked.connect(VoltarMenuPrincipal)
telaMenuAnimal.btnvoltarmenuprincipal.clicked.connect(VoltarMenuPrincipal)



telaCliente.btnvoltarmenucliente.clicked.connect(VoltarTelaMenuCliente)
telaConsultaCliente.btnvoltarmenucliente.clicked.connect(VoltarTelaMenuCliente)



telaAnimal.btnvoltarmenuanimal.clicked.connect(VoltarTelaMenuAnimal)
telaConsultaAnimal.btnvoltarmenuanimal.clicked.connect(VoltarTelaMenuAnimal)



telaCliente.btnlimpar.clicked.connect(Limpar) #Vinculado a função limpar ao botão
telaAnimal.btnlimpar.clicked.connect(Limpar)
telaConsultaCliente.btnlimpar.clicked.connect(Limpar)
telaConsultaAnimal.btnlimpar.clicked.connect(Limpar)


telaConsultaAnimal.btnconsultaranimal.clicked.connect(read_BD2)
telaConsultaCliente.btnConsultarcliente.clicked.connect(read_BD)

telaConsultaAnimal.btndeletaranimal.clicked.connect(Delete_DB)
telaConsultaCliente.btndeletarcliente.clicked.connect(Delete_DB2)

telaAnimal.btnAtualizarAnimal.clicked.connect(Update_DB)
telaCliente.btnAtualizarCliente.clicked.connect(Update_DB2)

telaAnimal.btncadastraranimal.clicked.connect(insert_BD2)
telaCliente.btnCadastrarCliente.clicked.connect(insert_BD)
app.exec()
