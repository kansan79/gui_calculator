# 기능 구현
import sys
from PyQt5.QtWidgets import *

class Main(QDialog):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        layout_operation = QGridLayout()
        layout_clear_equal = QGridLayout()
        layout_number = QGridLayout()
        layout_equation_solution = QFormLayout()


        self.equation = QLineEdit("")

        layout_equation_solution.addRow(self.equation)

        button_transnegative = QPushButton("+/-")
        button_transnegative.clicked.connect(self.button_transnegative_clicked)
        layout_number.addWidget(button_transnegative, 3, 0)

        button_clearentry = QPushButton("CE")
        button_clearentry.clicked.connect(self.button_clearentry_clicked)
        layout_operation.addWidget(button_clearentry,0,1)

        button_clear = QPushButton("Clear")
        button_clear.clicked.connect(self.button_clear_clicked)
        layout_operation.addWidget(button_clear,0,2)

        button_backspace = QPushButton("Backspace")
        button_backspace.clicked.connect(self.button_backspace_clicked)
        layout_operation.addWidget(button_backspace,0,3)

        button_denominator = QPushButton("1/x")
        button_denominator.clicked.connect(self.button_denominator_clicked)
        layout_operation.addWidget(button_denominator,1,0)
        button_square = QPushButton("x^2")
        button_square.clicked.connect(self.button_square_clicked)
        layout_operation.addWidget(button_square,1,1)
        button_root = QPushButton("√x")
        button_root.clicked.connect(self.button_root_clicked)
        layout_operation.addWidget(button_root,1,2)
        button_division = QPushButton("/")
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))
        layout_operation.addWidget(button_division,1,3)
       
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_number.addWidget(number_button_dict[number], 2-x, y)
            elif number==0:
                layout_number.addWidget(number_button_dict[number], 3, 1)

        button_equal = QPushButton("=")
        button_equal.clicked.connect(self.button_equal_clicked)
        layout_number.addWidget(button_equal,3,3)

        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_number.addWidget(button_dot, 3, 2)

        button_plus = QPushButton("+")
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        layout_number.addWidget(button_plus,2,3)

        button_minus = QPushButton("-")
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        layout_number.addWidget(button_minus,1,3)

        button_product = QPushButton("x")
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        layout_number.addWidget(button_product,0,3)
        
        button_remainder = QPushButton("%")
        button_remainder.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))
        layout_operation.addWidget(button_remainder,0,0)


        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_operation)
        main_layout.addLayout(layout_clear_equal)
        main_layout.addLayout(layout_number)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################

    global tmp_number
    global tmp_operation
    tmp_number = 0
    tmp_operation = ""

    def number_button_clicked(self, num):
        
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    def button_operation_clicked(self, operation):
        global tmp_number
        global tmp_operation
        equation = self.equation.text()
        tmp_number = float(equation)
        tmp_operation = operation
        self.equation.setText("")

    def button_equal_clicked(self):
        global tmp_number
        global tmp_operation
        equation = self.equation.text()

        if tmp_operation == "" :
            solution = equation
        elif tmp_operation == "+" :
            solution = str(tmp_number + float(equation))
        elif tmp_operation == "-" :
            solution = str(tmp_number - float(equation))
        elif tmp_operation == "*" :
            solution = str(tmp_number * float(equation))
        elif tmp_operation == "/" :
            solution = str(tmp_number / float(equation))
        elif tmp_operation == "%" :
            solution = str(tmp_number % float(equation))

        self.equation.setText(solution)
        tmp_number = 0
        tmp_operation = ""

    def button_square_clicked(self):
        equation = self.equation.text()
        solution = float (equation)**2
        self.equation.setText(str(solution))

    def button_transnegative_clicked(self):
        equation = self.equation.text()
        solution = float (equation) * -1 
        self.equation.setText(str(solution))

    def button_denominator_clicked(self):
        equation = self.equation.text()
        solution = 1/float (equation)
        self.equation.setText(str(solution))

    def button_root_clicked(self):
        equation = self.equation.text()
        solution = str (float(equation) ** 0.5)
        self.equation.setText(solution)

    def button_clear_clicked(self):
        self.equation.setText("")
        global tmp_operation
        global tmp_number
        tmp_number = 0
        tmp_operation = ""

    def button_clearentry_clicked(self):
        self.equation.setText("")
   
    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())