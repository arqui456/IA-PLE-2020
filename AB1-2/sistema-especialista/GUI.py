from PyQt5.QtWidgets import QMainWindow, QCheckBox, QPushButton, QGroupBox, QTextBrowser, QLabel
from PyQt5 import QtCore
from PyQt5 import QtGui
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.symptoms = [False] * 39

        cb = QCheckBox('Respiração Ofegante', self)
        cb.move(20, 20)
        cb.resize(200, 25)
        cb.stateChanged.connect(self.checklist0)

        cb2 = QCheckBox('Falta de Ar', self)
        cb2.move(20, 40)
        cb2.resize(200, 25)
        cb2.stateChanged.connect(self.checklist1)

        cb3 = QCheckBox('Peito Apertado', self)
        cb3.move(20, 60)
        cb3.resize(200, 25)
        cb3.stateChanged.connect(self.checklist2)

        cb4 = QCheckBox('Tosse', self)
        cb4.move(20, 80)
        cb4.resize(200, 25)
        cb4.stateChanged.connect(self.checklist3)

        cb5 = QCheckBox('Respiração Rápida', self)
        cb5.move(20, 100)
        cb5.resize(200, 25)
        cb5.stateChanged.connect(self.checklist4)

        cb6 = QCheckBox('Sonolência', self)
        cb6.move(20, 120)
        cb6.resize(200, 25)
        cb6.stateChanged.connect(self.checklist5)

        cb7 = QCheckBox('Dores nas articulações', self)
        cb7.move(20, 140)
        cb7.resize(200, 25)
        cb7.stateChanged.connect(self.checklist6)

        cb8 = QCheckBox('Ternura', self)
        cb8.move(20, 160)
        cb8.resize(200, 25)
        cb8.stateChanged.connect(self.checklist7)

        cb9 = QCheckBox('Rigidez', self)
        cb9.move(20, 180)
        cb9.resize(200, 25)
        cb9.stateChanged.connect(self.checklist8)

        cb10 = QCheckBox('Inflamação nas articulações', self)
        cb10.move(20, 200)
        cb10.resize(220, 25)
        cb10.stateChanged.connect(self.checklist9)

        cb11 = QCheckBox('Pele Vermelha', self)
        cb11.move(20, 220)
        cb11.resize(200, 25)
        cb11.stateChanged.connect(self.checklist10)

        cb12 = QCheckBox('Fraqueza', self)
        cb12.move(20, 240)
        cb12.resize(200, 25)
        cb12.stateChanged.connect(self.checklist11)

        cb13 = QCheckBox('Caroço nos Ossos', self)
        cb13.move(20, 260)
        cb13.resize(200, 25)
        cb13.stateChanged.connect(self.checklist12)

        cb14 = QCheckBox('Dor nos ossos', self)
        cb14.move(20, 280)
        cb14.resize(200, 25)
        cb14.stateChanged.connect(self.checklist13)

        cb15 = QCheckBox('Ossos Fracos', self)
        cb15.move(20, 300)
        cb15.resize(200, 25)
        cb15.stateChanged.connect(self.checklist14)

        cb16 = QCheckBox('Fraturas', self)
        cb16.move(20, 320)
        cb16.resize(200, 25)
        cb16.stateChanged.connect(self.checklist15)

        cb17 = QCheckBox('Dor de Cabeça', self)
        cb17.move(20, 340)
        cb17.resize(200, 25)
        cb17.stateChanged.connect(self.checklist16)

        cb18 = QCheckBox('Convulsões', self)
        cb18.move(20, 360)
        cb18.resize(200, 25)
        cb18.stateChanged.connect(self.checklist17)

        cb19 = QCheckBox('Epilepsia', self)
        cb19.move(20, 380)
        cb19.resize(200, 25)
        cb19.stateChanged.connect(self.checklist18)

        cb20 = QCheckBox('Mudanças Mentais', self)
        cb20.move(20, 400)
        cb20.resize(200, 25)
        cb20.stateChanged.connect(self.checklist19)

        cb21 = QCheckBox('Mudanças Comportamentais', self)
        cb21.move(260, 20)
        cb21.resize(220, 25)
        cb21.stateChanged.connect(self.checklist20)

        cb22 = QCheckBox('Problemas de Memória', self)
        cb22.move(260, 40)
        cb22.resize(200, 25)
        cb22.stateChanged.connect(self.checklist21)

        cb23 = QCheckBox('Paralisia de Parte do Corpo', self)
        cb23.move(260, 60)
        cb23.resize(220, 25)
        cb23.stateChanged.connect(self.checklist22)

        cb24 = QCheckBox('Febre', self)
        cb24.move(260, 80)
        cb24.resize(200, 25)
        cb24.stateChanged.connect(self.checklist23)

        cb25 = QCheckBox('Asma', self)
        cb25.move(260, 100)
        cb25.resize(200, 25)
        cb25.stateChanged.connect(self.checklist24)

        cb26 = QCheckBox('Dor no coração', self)
        cb26.move(260, 120)
        cb26.resize(200, 25)
        cb26.stateChanged.connect(self.checklist25)

        cb27 = QCheckBox('Catarro no pulmão', self)
        cb27.move(260, 140)
        cb27.resize(200, 25)
        cb27.stateChanged.connect(self.checklist26)

        cb28 = QCheckBox('Batimento Cardíaco Acelerado', self)
        cb28.move(260, 160)
        cb28.resize(230, 25)
        cb28.stateChanged.connect(self.checklist27)

        cb29 = QCheckBox('Dor no Peito', self)
        cb29.move(260, 180)
        cb29.resize(200, 25)
        cb29.stateChanged.connect(self.checklist28)
    
        cb30 = QCheckBox('Coriza', self)
        cb30.move(260, 200)
        cb30.resize(200, 25)
        cb30.stateChanged.connect(self.checklist29)

        cb31 = QCheckBox('Nariz Entupido', self)
        cb31.move(260, 220)
        cb31.resize(200, 25)
        cb31.stateChanged.connect(self.checklist30)

        cb32 = QCheckBox('Espirrando', self)
        cb32.move(260, 240)
        cb32.resize(200, 25)
        cb32.stateChanged.connect(self.checklist31)

        cb33 = QCheckBox('Garganta Seca', self)
        cb33.move(260, 260)
        cb33.resize(200, 25)
        cb33.stateChanged.connect(self.checklist32)

        cb34 = QCheckBox('Dor de Garganta', self)
        cb34.move(260, 280)
        cb34.resize(200, 25)
        cb34.stateChanged.connect(self.checklist33)

        cb35 = QCheckBox('Estresse', self)
        cb35.move(260, 300)
        cb35.resize(200, 25)
        cb35.stateChanged.connect(self.checklist34)

        cb36 = QCheckBox('Perda de Apetite', self)
        cb36.move(260, 320)
        cb36.resize(200, 25)
        cb36.stateChanged.connect(self.checklist35)

        cb37 = QCheckBox('Insônia', self)
        cb37.move(260, 340)
        cb37.resize(200, 25)
        cb37.stateChanged.connect(self.checklist36)

        cb38 = QCheckBox('Mudança de humor', self)
        cb38.move(260, 360)
        cb38.resize(200, 25)
        cb38.stateChanged.connect(self.checklist37)

        cb39 = QCheckBox('Tontura', self)
        cb39.move(260, 380)
        cb39.resize(200, 25)
        cb39.stateChanged.connect(self.checklist38)

        groubBox = QGroupBox("Resultados", self)
        groubBox.move(500, 50)

        groubBox2 = QGroupBox("Certeza", self)
        groubBox2.move(600, 50)

        self.resultados = QTextBrowser(groubBox)
        self.certeza = QTextBrowser(groubBox2)

        #resultados.setGeometry(QtCore.QRect(10, 90, 100, 100))

        accept_button = QPushButton(self)
        accept_button.setText("Accept")
        accept_button.move(800, 50)
        accept_button.clicked.connect(self.accepted)

        photo = QLabel(self)
        photo.setGeometry(QtCore.QRect(500, 80, 900, 500))
        photo.setPixmap(QtGui.QPixmap("rick.png"))

        self.setGeometry(500,600,1000,500)
        self.setWindowTitle("Sistema Expecialista - Diagnóstico de Doenças")
        self.show()

    def checklist0(self):
        self.symptoms[0] = not self.symptoms[0]

    def checklist1(self):
        self.symptoms[1] = not self.symptoms[1]

    def checklist2(self):
        self.symptoms[0] = not self.symptoms[2]

    def checklist3(self):
        self.symptoms[1] = not self.symptoms[3]

    def checklist4(self):
        self.symptoms[0] = not self.symptoms[4]

    def checklist5(self):
        self.symptoms[1] = not self.symptoms[5]

    def checklist6(self):
        self.symptoms[0] = not self.symptoms[6]

    def checklist7(self):
        self.symptoms[1] = not self.symptoms[7]

    def checklist8(self):
        self.symptoms[0] = not self.symptoms[8]

    def checklist9(self):
        self.symptoms[1] = not self.symptoms[9]

    def checklist10(self):
        self.symptoms[0] = not self.symptoms[10]

    def checklist11(self):
        self.symptoms[1] = not self.symptoms[11]

    def checklist12(self):
        self.symptoms[0] = not self.symptoms[12]

    def checklist13(self):
        self.symptoms[1] = not self.symptoms[13]

    def checklist14(self):
        self.symptoms[0] = not self.symptoms[14]

    def checklist15(self):
        self.symptoms[1] = not self.symptoms[15]

    def checklist16(self):
        self.symptoms[0] = not self.symptoms[16]

    def checklist17(self):
        self.symptoms[1] = not self.symptoms[17]

    def checklist18(self):
        self.symptoms[0] = not self.symptoms[18]

    def checklist19(self):
        self.symptoms[1] = not self.symptoms[19]

    def checklist20(self):
        self.symptoms[0] = not self.symptoms[20]

    def checklist21(self):
        self.symptoms[1] = not self.symptoms[21]

    def checklist22(self):
        self.symptoms[0] = not self.symptoms[22]

    def checklist23(self):
        self.symptoms[1] = not self.symptoms[23]

    def checklist24(self):
        self.symptoms[0] = not self.symptoms[24]

    def checklist25(self):
        self.symptoms[1] = not self.symptoms[25]

    def checklist26(self):
        self.symptoms[0] = not self.symptoms[26]

    def checklist27(self):
        self.symptoms[1] = not self.symptoms[27]

    def checklist28(self):
        self.symptoms[0] = not self.symptoms[28]

    def checklist29(self):
        self.symptoms[1] = not self.symptoms[29]

    def checklist30(self):
        self.symptoms[0] = not self.symptoms[30]

    def checklist31(self):
        self.symptoms[1] = not self.symptoms[31]

    def checklist32(self):
        self.symptoms[0] = not self.symptoms[32]

    def checklist33(self):
        self.symptoms[1] = not self.symptoms[33]

    def checklist34(self):
        self.symptoms[0] = not self.symptoms[34]

    def checklist35(self):
        self.symptoms[1] = not self.symptoms[35]

    def checklist36(self):
        self.symptoms[0] = not self.symptoms[36]

    def checklist37(self):
        self.symptoms[1] = not self.symptoms[37]

    def checklist38(self):
        self.symptoms[0] = not self.symptoms[38]

    def accepted(self):
        print(self.symptoms)
        self.resultados.setText("Glaucoma")
        self.certeza.setText("100%")

