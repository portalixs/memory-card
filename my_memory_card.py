from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout, QGroupBox
from random import shuffle

app = QApplication([])
mainWindow = QWidget()
mainWindow.setWindowTitle('Memory Card')
mainWindow.cur_question = -1
questionLabel = QLabel('Какой национальности не существует?')
Button = QPushButton('Ответить')

LayoutMain = QVBoxLayout()

RadioGroupBox1 = QGroupBox('Варианты ответов')
qbtn1 = QRadioButton('вар1')
qbtn2 = QRadioButton('вар2')
qbtn3 = QRadioButton('вар3')
qbtn4 = QRadioButton('вар4')
Layout1 = QVBoxLayout()
Layout2 = QVBoxLayout()
Layout3 = QHBoxLayout()

class question():
    def __init__(self, Question, Right_answer, Wrong_answer1, Wrong_answer2, Wrong_answer3):
        self.Question = Question
        self.Right_answer = Right_answer
        self.Wrong_answer1 = Wrong_answer1
        self.Wrong_answer2 = Wrong_answer2
        self.Wrong_answer3 = Wrong_answer3

questionsList = []
questionsList.append(question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questionsList.append(question('2+2?','4','5','3','6'))
questionsList.append(question('Какой национальности не существует?','Энцы','Смурфы','Чулымцы','Алеуты'))
Layout1.addWidget(qbtn1, alignment=Qt.AlignHCenter)
Layout1.addWidget(qbtn2, alignment=Qt.AlignHCenter) 
Layout2.addWidget(qbtn3, alignment=Qt.AlignHCenter)
Layout2.addWidget(qbtn4, alignment=Qt.AlignHCenter)
Layout3.addLayout(Layout1)
Layout3.addLayout(Layout2)

RadioGroupBox1.setLayout(Layout3)

RadioGroupBox2 = QGroupBox('Результат')
labelGroupBox21 = QLabel('Правильно/Неправильно')
labelGroupBox22 = QLabel('Правильный ответ')
LayoutGroupBox2 = QVBoxLayout()
LayoutGroupBox2.addWidget(labelGroupBox21, alignment=Qt.AlignLeft)
LayoutGroupBox2.addWidget(labelGroupBox22, alignment=Qt.AlignHCenter)

RadioGroupBox2.setLayout(LayoutGroupBox2)

RadioGroupBox2.hide()

Answers = [qbtn1, qbtn2, qbtn3, qbtn4]

def showAnswer():
    RadioGroupBox1.hide()
    RadioGroupBox2.show()
    Button.setText('Закрыть')
    if qbtn1.isChecked() == True:
        labelGroupBox21.setText('Правильно')
    else:
        labelGroupBox21.setText('Неправильно')
    labelGroupBox22.setText('Правильный ответ: '+qbtn1.text())
def showQuestion():
    RadioGroupBox1.show()
    RadioGroupBox2.hide()
    Button.setText('Ответить') 
    qbtn1.setChecked(False)
    qbtn2.setChecked(False)
    qbtn3.setChecked(False)
    qbtn4.setChecked(False)
def ask(Question, Right_answer, Wrong_answer1, Wrong_answer2, Wrong_answer3):
    shuffle(Answers)
    questionLabel.setText(Question)
    Answers[0].setText(Right_answer)
    Answers[1].setText(Wrong_answer1)
    Answers[2].setText(Wrong_answer2)
    Answers[3].setText(Wrong_answer3)
    showQuestion()
def testTextButton():
    if Button.text() == 'Ответить':
        showAnswer()
    else:
        next_question()
def next_question():
    mainWindow.cur_question = mainWindow.cur_question + 1
    if mainWindow.cur_question >= len(questionsList):
        mainWindow.cur_question = 0
    q = questionsList[mainWindow.cur_question]
    ask(q)

Button.clicked.connect(testTextButton)

LayoutMain.addWidget(questionLabel, alignment=Qt.AlignHCenter)
LayoutMain.addWidget(RadioGroupBox1)
LayoutMain.addWidget(RadioGroupBox2)
LayoutMain.addWidget(Button, alignment=Qt.AlignHCenter)

mainWindow.setLayout(LayoutMain)
mainWindow.show()
app.exec_()
#создай приложение для запоминания информации