from PyQt6.QtWidgets import*
def menu_window():
    window = QDialog()
    quest_lbl = QLabel("Запитання")
    quest_input = QLineEdit()


    main_line = QVBoxLayout()


    h1 = QHBoxLayout()
    h1.addWidget(quest_lbl)
    h1.addWidget(quest_input)
    main_line.addLayout(h1)


    window.setLayout(main_line)




    window.exec()
