from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, \
    QHBoxLayout, QVBoxLayout, QFormLayout




class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        self.result = '0'
        self.cal_res = QLabel(self.result, objectName='cal_res')
        
        self.btn01 = QPushButton('standart', objectName='btn01')
        self.btn00 = QPushButton('length', objectName='btn00')
        self.btn_0 = QPushButton('0', objectName='btn_0')
        self.btn_1 = QPushButton('1', objectName='btn_1')
        self.btn_2 = QPushButton('2', objectName='btn_2')
        self.btn_3 = QPushButton('3', objectName='btn_3')
        self.btn_4 = QPushButton('4', objectName='btn_4')
        self.btn_5 = QPushButton('5', objectName='btn_5')
        self.btn_6 = QPushButton('6', objectName='btn_6')
        self.btn_7 = QPushButton('7', objectName='btn_7')
        self.btn_8 = QPushButton('8', objectName='btn_8')
        self.btn_9 = QPushButton('9', objectName='btn_9')
        
        self.btn_neg = QPushButton('+/-', objectName='btn_neg')
        self.btn_сom = QPushButton('.', objectName='btn_сom')
        self.btn_equal = QPushButton('=', objectName='btn_equal')
        
        self.btn_minus = QPushButton('-', objectName='btn_minus')
        self.btn_plus = QPushButton('+', objectName='btn_plus')
        self.btn_incr = QPushButton('×', objectName='btn_incr')
        self.btn_div = QPushButton('/', objectName='btn_div')
        self.btn_del = QPushButton('←', objectName='btn_del')
        self.btn_clear = QPushButton('C', objectName='btn_clear')
        self.btn_per = QPushButton('%', objectName='btn_per')

        h_1 = QHBoxLayout()
        h_1.addWidget(self.cal_res, alignment=Qt.AlignRight)        
        
        h_0 = QHBoxLayout()
        h_0.addWidget(self.btn00)
        h_0.addWidget(self.btn01)

        h_2 = QHBoxLayout()
        h_2.addWidget(self.btn_per)
        h_2.addWidget(self.btn_clear)
        h_2.addWidget(self.btn_del)
        h_2.addWidget(self.btn_div)
        
        h_3 = QHBoxLayout()
        h_3.addWidget(self.btn_7)
        h_3.addWidget(self.btn_8)
        h_3.addWidget(self.btn_9)
        h_3.addWidget(self.btn_incr)
        
        h_4 = QHBoxLayout()
        h_4.addWidget(self.btn_4)
        h_4.addWidget(self.btn_5)
        h_4.addWidget(self.btn_6)
        h_4.addWidget(self.btn_minus)
        
        h_5 = QHBoxLayout()
        h_5.addWidget(self.btn_1)
        h_5.addWidget(self.btn_2)
        h_5.addWidget(self.btn_3)
        h_5.addWidget(self.btn_plus)
        
        h_6 = QHBoxLayout()
        h_6.addWidget(self.btn_neg)        
        h_6.addWidget(self.btn_0)   
        h_6.addWidget(self.btn_сom)
        h_6.addWidget(self.btn_equal)        

        #events
        self.btn_0.clicked.connect(lambda: self.press_it('0'))
        self.btn_1.clicked.connect(lambda: self.press_it('1'))
        self.btn_2.clicked.connect(lambda: self.press_it('2'))
        self.btn_3.clicked.connect(lambda: self.press_it('3'))
        self.btn_4.clicked.connect(lambda: self.press_it('4'))
        self.btn_5.clicked.connect(lambda: self.press_it('5'))
        self.btn_6.clicked.connect(lambda: self.press_it('6'))
        self.btn_7.clicked.connect(lambda: self.press_it('7'))
        self.btn_8.clicked.connect(lambda: self.press_it('8'))
        self.btn_9.clicked.connect(lambda: self.press_it('9'))
        
        self.btn_del.clicked.connect(lambda: self.remove_it())
        self.btn_neg.clicked.connect(lambda: self.plus_minus_it())
        self.btn_сom.clicked.connect(lambda: self.dot_it())
        self.btn_clear.clicked.connect(lambda: self.press_it("C"))

        self.btn_minus.clicked.connect(lambda: self.press_it('-'))
        self.btn_plus.clicked.connect(lambda: self.press_it('+'))
        self.btn_incr.clicked.connect(lambda: self.press_it('*'))
        self.btn_div.clicked.connect(lambda: self.press_it('/'))
        self.btn_per.clicked.connect(lambda: self.press_it('%')) 

        self.btn_equal.clicked.connect(lambda: self.math_it()) 
        
        self.btn00.clicked.connect(lambda: self.show_window_2())  
        self.btn00.clicked.connect(lambda: w.close())
       
        v = QVBoxLayout(self)
        v.addLayout(h_0) 
        v.addLayout(h_1)   
        v.addLayout(h_2)
        v.addLayout(h_3)
        v.addLayout(h_4)
        v.addLayout(h_5)
        v.addLayout(h_6) 
        
        
    
    def math_it(self):
        screen = self.cal_res.text()
        try:
            
            answer = eval(screen)
            
            self.cal_res.setText(str(answer))
        except:
            
            self.cal_res.setText("ERROR")
            
    def press_it(self, pressed):
        if pressed == "C":
            self.cal_res.setText("0")
        else:
            if self.cal_res.text() == "0":
                self.cal_res.setText("")    
            self.cal_res.setText(f'{self.cal_res.text()}{pressed}')        
             
    # Удалить символ
    def remove_it(self):
        # Возьмите то, что уже есть на экране
        screen = self.cal_res.text()
        # Удалить последний элемент в строке
        screen = screen[:-1]
        # Вывод обратно на экран
        self.cal_res.setText(screen)        

    # Изменение с положительного / отрицательного
    def plus_minus_it(self):
        screen = self.cal_res.text()
        if "-" in screen:
            self.cal_res.setText(screen.replace("-", ""))
        else:
            self.cal_res.setText(f'-{screen}')

    # Добавить десятичную дробь
    def dot_it(self):
        screen = self.cal_res.text()
        if screen[-1] == ".":
            pass
        else:
            self.cal_res.setText(f'{screen}.') 
    



class Window2(QWidget):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Window2')


class MainWindow(MainWindow):
    
    def __init__(self):

        super(MainWindow, self).__init__()
        self.setWindowTitle('MainWindow')

    def show_window(self):
        self.w = Window1()
        
        self.w.show()

    def show_window_2(self):
        self.w2 = Window2()
        self.w2.resize(400, 900)
        self.w2.show()
        self.app = QApplication(sys.argv)
        self.app.setStyleSheet(style) 
    def interface(self):
        self.result = '0'
        self.cal_res = QLabel(self.result, objectName='cal_res')
        
        self.btn01 = QPushButton('standart', objectName='btn01')
        self.btn00 = QPushButton('length', objectName='btn00')
        self.btn_0 = QPushButton('0', objectName='btn_0')
        self.btn_1 = QPushButton('1', objectName='btn_1')
        self.btn_2 = QPushButton('2', objectName='btn_2')
        self.btn_3 = QPushButton('3', objectName='btn_3')
        self.btn_4 = QPushButton('4', objectName='btn_4')
        self.btn_5 = QPushButton('5', objectName='btn_5')
        self.btn_6 = QPushButton('6', objectName='btn_6')
        self.btn_7 = QPushButton('7', objectName='btn_7')
        self.btn_8 = QPushButton('8', objectName='btn_8')
        self.btn_9 = QPushButton('9', objectName='btn_9')
        
        self.btn_neg = QPushButton('+/-', objectName='btn_neg')
        self.btn_сom = QPushButton('.', objectName='btn_сom')
        self.btn_equal = QPushButton('=', objectName='btn_equal')
        
        self.btn_minus = QPushButton('-', objectName='btn_minus')
        self.btn_plus = QPushButton('+', objectName='btn_plus')
        self.btn_incr = QPushButton('×', objectName='btn_incr')
        self.btn_div = QPushButton('/', objectName='btn_div')
        self.btn_del = QPushButton('←', objectName='btn_del')
        self.btn_clear = QPushButton('C', objectName='btn_clear')
        self.btn_per = QPushButton('%', objectName='btn_per')

        h_1 = QHBoxLayout()
        h_1.addWidget(self.cal_res, alignment=Qt.AlignRight)        
        
        h_0 = QHBoxLayout()
        h_0.addWidget(self.btn00)
        h_0.addWidget(self.btn01)

        h_2 = QHBoxLayout()
        h_2.addWidget(self.btn_per)
        h_2.addWidget(self.btn_clear)
        h_2.addWidget(self.btn_del)
        h_2.addWidget(self.btn_div)
        
        h_3 = QHBoxLayout()
        h_3.addWidget(self.btn_7)
        h_3.addWidget(self.btn_8)
        h_3.addWidget(self.btn_9)
        h_3.addWidget(self.btn_incr)
        
        h_4 = QHBoxLayout()
        h_4.addWidget(self.btn_4)
        h_4.addWidget(self.btn_5)
        h_4.addWidget(self.btn_6)
        h_4.addWidget(self.btn_minus)
        
        h_5 = QHBoxLayout()
        h_5.addWidget(self.btn_1)
        h_5.addWidget(self.btn_2)
        h_5.addWidget(self.btn_3)
        h_5.addWidget(self.btn_plus)
        
        h_6 = QHBoxLayout()
        h_6.addWidget(self.btn_neg)        
        h_6.addWidget(self.btn_0)   
        h_6.addWidget(self.btn_сom)
        h_6.addWidget(self.btn_equal)        

        #events
        self.btn_0.clicked.connect(lambda: self.press_it('0'))
        self.btn_1.clicked.connect(lambda: self.press_it('1'))
        self.btn_2.clicked.connect(lambda: self.press_it('2'))
        self.btn_3.clicked.connect(lambda: self.press_it('3'))
        self.btn_4.clicked.connect(lambda: self.press_it('4'))
        self.btn_5.clicked.connect(lambda: self.press_it('5'))
        self.btn_6.clicked.connect(lambda: self.press_it('6'))
        self.btn_7.clicked.connect(lambda: self.press_it('7'))
        self.btn_8.clicked.connect(lambda: self.press_it('8'))
        self.btn_9.clicked.connect(lambda: self.press_it('9'))
        
        self.btn_del.clicked.connect(lambda: self.remove_it())
        self.btn_neg.clicked.connect(lambda: self.plus_minus_it())
        self.btn_сom.clicked.connect(lambda: self.dot_it())
        self.btn_clear.clicked.connect(lambda: self.press_it("C"))

        self.btn_minus.clicked.connect(lambda: self.press_it('-'))
        self.btn_plus.clicked.connect(lambda: self.press_it('+'))
        self.btn_incr.clicked.connect(lambda: self.press_it('*'))
        self.btn_div.clicked.connect(lambda: self.press_it('/'))
        self.btn_per.clicked.connect(lambda: self.press_it('%')) 

        self.btn_equal.clicked.connect(lambda: self.math_it()) 
        
        self.btn00.clicked.connect(lambda: self.show_window_2())  
        self.btn00.clicked.connect(lambda: w.close())
       
        v = QVBoxLayout(self)
        v.addLayout(h_0) 
        v.addLayout(h_1)   
        v.addLayout(h_2)
        v.addLayout(h_3)
        v.addLayout(h_4)
        v.addLayout(h_5)
        v.addLayout(h_6) 

    
    

        

style = '''
QWidget {
    color: white;
	background-color: #121212;
	font-family: Rubik;
	font-size: 16pt;
	font-weight: 600;
}



QPushButton {
    height: 70px;
    font-size: 30px;
    background-color: transperent;
    border: none;
}
#btn00 btn_0, #btn_1, #btn_2, #btn_3, #btn_4, #btn_5, 
#btn_6, #btn_7, #btn_8, #btn_9 {
    background-color: #121252;
    color: white;
}
#btn_neg, #btn_сom, #btn_equal, #btn_minus, #btn_plus, 
#btn_incr, #btn_div, #btn_del, #btn_clear, #btn_per {
    background-color: #121252;
    color: white;
}
#btn_equal {
    background-color: grey;
    color: white;
}


'''
        

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyleSheet(style)                     # +++   
    
    
    w = MainWindow()
    w.setWindowTitle('Калькулятор')
    w.resize(400, 900)
    w.show()
    app.exec_()
