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
        layout_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        self.solution = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        layout_solution.addRow(self.solution)

        ### 사칙연산 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")

        ### =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_clear = QPushButton("C")
        button_backspace = QPushButton("Backspace")

        ### 소숫점 버튼과 00 버튼 생성
        button_dot = QPushButton(".")
        button_double_zero = QPushButton("00")
        test = 1
        ##3 숫자 버튼 생성
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
        
        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

         ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_clear.clicked.connect(self.button_clear_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### 소숫점 버튼과 00 버튼 클릭시 시그널 설정
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))

        ### 새로운 버튼 생성
        button_remainder = QPushButton("%")
        button_clear_all = QPushButton("CE")
        button_reciprocal = QPushButton("1/x")
        button_square = QPushButton("x^2")
        button_square_root = QPushButton("x^1/2")
        button_plus_minus = QPushButton("+/-")

        ### 새로운 버튼 시그널 설정
        button_remainder.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))
        button_clear_all.clicked.connect(self.button_clear_clicked)
        button_reciprocal.clicked.connect(lambda state, operation = "**-1": self.button_square_clicked(operation))
        button_square.clicked.connect(lambda state, operation = "**2": self.button_square_clicked(operation))
        button_square_root.clicked.connect(lambda state, operation = "**0.5": self.button_square_clicked(operation))

        ### 버튼들 레이아웃에 추가
        layout_operation.addWidget(button_remainder, 0, 0)
        layout_operation.addWidget(button_clear_all, 0, 1)
        layout_operation.addWidget(button_clear, 0, 2)
        layout_operation.addWidget(button_backspace, 0, 3)
        layout_operation.addWidget(button_reciprocal, 1, 0)
        layout_operation.addWidget(button_square, 1, 1)
        layout_operation.addWidget(button_square_root, 1, 2)
        layout_operation.addWidget(button_division, 1, 3)
        layout_operation.addWidget(number_button_dict[7], 2, 0)
        layout_operation.addWidget(number_button_dict[8], 2, 1)
        layout_operation.addWidget(number_button_dict[9], 2, 2)
        layout_operation.addWidget(button_product, 2, 3)
        layout_operation.addWidget(number_button_dict[4], 3, 0)
        layout_operation.addWidget(number_button_dict[5], 3, 1)
        layout_operation.addWidget(number_button_dict[6], 3, 2)
        layout_operation.addWidget(button_minus, 3, 3)
        layout_operation.addWidget(number_button_dict[1], 4, 0)
        layout_operation.addWidget(number_button_dict[2], 4, 1)
        layout_operation.addWidget(number_button_dict[3], 4, 2)
        layout_operation.addWidget(button_plus, 4, 3)
        layout_operation.addWidget(button_plus_minus, 5, 0)
        layout_operation.addWidget(number_button_dict[0], 5, 1)
        layout_operation.addWidget(button_dot, 5, 2)
        layout_operation.addWidget(button_equal, 5, 3)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_solution)
        main_layout.addLayout(layout_operation)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        global temp
        solution = self.solution.text()
        solution += str(num)
        self.solution.setText(solution)
        if temp != "":
            temp += str(num)

    def button_operation_clicked(self, operation):
        global temp
        solution = self.solution.text() 
        temp = solution + operation
        self.solution.setText("")

    def button_equal_clicked(self):
        global temp
        if temp != "":
            solution = eval(temp)
            self.solution.setText(str(solution))

    def button_clear_clicked(self):
        global temp
        self.solution.setText("")
        temp = ""

    def button_backspace_clicked(self):
        global temp
        solution = self.solution.text()
        solution = solution[:-1]
        temp = temp[:-1]
        self.solution.setText(solution)

    def button_square_clicked(self, operation):
        solution = self.solution.text()
        solution += operation
        self.solution.setText(str(eval(solution)))

if __name__ == '__main__':
    ### 이항연산자 연산용 변수
    temp = ""
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())