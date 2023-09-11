from PyQt5.QtWidgets import *
# from PyQt5.Qt import *
from PyQt5.Qsci import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from pathlib import Path
import sys
import os
import keyword
import pkgutil

import argparse
from antlr4 import *
from antlr4.tree.Trees import Trees
from antlr4 import FileStream, CommonTokenStream

from gramar_generated.YALPLexer import YALPLexer
from gramar_generated.YALPParser import YALPParser
from util.generate_tree import generate_parse_tree
from compiler_files.custom_visitor import CustomVisitor
from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def __init__(self, error_callback):
        super().__init__()
        self.error_callback = error_callback

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_message = f"Line {line}:{column} -> {msg}"
        self.error_callback(error_message)


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.side_bar_crl = "#2d2d2d" #282c34
        self.init_ui()

        self.current_file = None
        self.current_side_bar = None

    def init_ui(self):
        self.setWindowTitle('Code Editor')
        self.resize(1300, 900)

        self.setStyleSheet(open('gui/css/style.qss', 'r').read())

        self.window_font = QFont('Consolas', 12)
        # self.window_font.setPointSize(16)
        self.setFont(self.window_font)

        self.set_up_menu()
        self.set_up_body()

        self.show()

    def get_editor(self) -> QsciScintilla:
        
        editor = QsciScintilla()
        editor.setUtf8(True)
        editor.setFont(self.window_font)

        editor.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        editor.setIndentationGuides(True)
        editor.setTabWidth(4)
        editor.setIndentationsUseTabs(False)
        editor.setAutoIndent(True)

        editor.setAutoCompletionSource(QsciScintilla.AcsAll)
        editor.setAutoCompletionThreshold(1)
        editor.setAutoCompletionCaseSensitivity(False)
        editor.setAutoCompletionUseSingle(QsciScintilla.AcusNever)


        editor.setCaretForegroundColor(QColor('#000000'))
        editor.setCaretLineVisible(True)
        editor.setCaretWidth(2)
        editor.setCaretLineBackgroundColor(QColor('#DDDCDC'))

        editor.setEolMode(QsciScintilla.EolWindows)
        editor.setEolVisibility(False)

        # lexer for COOL language
        self.lexer = QsciLexerPython()
        self.lexer.setDefaultFont(self.window_font)

        self.api = QsciAPIs(self.lexer)
        for key in keyword.kwlist + dir(__builtins__):
            self.api.add(key)
        
        for _, name, _ in pkgutil.iter_modules():
            self.api.add(name)

        # self.api.add("addition a: int, b: int")
        
        editor.setLexer(self.lexer)

        # line numbers
        editor.setMarginType(0, QsciScintilla.NumberMargin)
        editor.setMarginWidth(0, '000')
        editor.setMarginsForegroundColor(QColor('#ffffff'))
        editor.setMarginsBackgroundColor(QColor('#848484'))
        editor.setMarginsFont(self.window_font)

        # key press
        editor.keyPressEvent = self.key_press_event


        return editor
    
    def key_press_event(self, event: QKeyEvent):
        editor: QsciScintilla = self.tab_view.currentWidget()
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Space:
            editor.autoCompleteFromAll()

        else:
            QsciScintilla.keyPressEvent(editor, event)
    
    def is_binary(self, path: Path) -> bool:
        with open(path, 'rb') as f:
            for byte in f.read(1024):
                if byte == 0:
                    return True
        return False
    
    def set_new_tab(self, path: Path, is_new_file = False):
        editor = self.get_editor()
        if is_new_file:
            self.tab_view.addTab(editor, 'Untitled')
            self.setWindowTitle('Untitled')
            self.statusBar().showMessage('New file created', 2000)
            self.tab_view.setCurrentIndex(self.tab_view.count() - 1)
            self.current_file = None
            return
        
        if not path.is_file():
            return
        
        if not is_new_file and self.is_binary(path):
            self.statusBar().showMessage('Cannot open binary file')
            return
        
        #check if file is already open
        
        for i in range(self.tab_view.count()):
            # if self.tab_view.widget(i).path == path:
            #     self.tab_view.setCurrentIndex(i)
            #     return
            if self.tab_view.tabText(i) == path.name:
                self.tab_view.setCurrentIndex(i)
                return
        
        #create new tab
        

        self.tab_view.addTab(editor, path.name)

        # if not is_new_file:
        editor.setText(path.read_text())
        self.setWindowTitle(path.name)
        self.current_file = path
        self.tab_view.setCurrentIndex(self.tab_view.count() - 1)
        self.statusBar().showMessage(f'File opened {path.name}', 2000)

    def set_up_menu(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('File')

        new_file = file_menu.addAction('New')
        new_file.setShortcut('Ctrl+N')
        new_file.triggered.connect(self.new_file)

        open_file = file_menu.addAction('Open File')
        open_file.setShortcut('Ctrl+O')
        open_file.triggered.connect(self.open_file)

        open_folder = file_menu.addAction('Open Folder')
        open_folder.setShortcut('Ctrl+K')
        open_folder.triggered.connect(self.open_folder)

        file_menu.addSeparator()

        save_file = file_menu.addAction('Save')
        save_file.setShortcut('Ctrl+S')
        save_file.triggered.connect(self.save_file)

        save_file_as = file_menu.addAction('Save As')
        save_file_as.setShortcut('Ctrl+Shift+S')
        save_file_as.triggered.connect(self.save_file_as)

        # Edit menu
        edit_menu = menu_bar.addMenu('Edit')

        undo = edit_menu.addAction('Undo')
        undo.setShortcut('Ctrl+Z')
        undo.triggered.connect(self.undo)

        redo = edit_menu.addAction('Redo')
        redo.setShortcut('Ctrl+Shift+Z')
        redo.triggered.connect(self.redo)

        edit_menu.addSeparator()

        copy = edit_menu.addAction('Copy')
        copy.setShortcut('Ctrl+C')
        copy.triggered.connect(self.copy)

        cut = edit_menu.addAction('Cut')
        cut.setShortcut('Ctrl+X')
        cut.triggered.connect(self.cut)

        paste = edit_menu.addAction('Paste')
        paste.setShortcut('Ctrl+V')
        paste.triggered.connect(self.paste)



        # Run menu
        run_menu = menu_bar.addMenu('Run')

        run = run_menu.addAction('Run')
        run.setShortcut('Ctrl+R')
        run.triggered.connect(self.run)

    def new_file(self):
        self.set_new_tab(None, is_new_file=True)

    def open_file(self):
        openf = QFileDialog.Options()
        openf |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open File', os.getcwd(), 'All Files (*);;Python Files (*.py);;COOL/YAPL Files(*.cl)', options=openf)

        if file_path == '':
            self.statusBar().showMessage('File not opened', 2000)
            return

        file = Path(file_path)
        self.set_new_tab(file)



    def open_folder(self):
        openf = QFileDialog.Options()
        openf |= QFileDialog.DontUseNativeDialog

        folder_path = QFileDialog.getExistingDirectory(self, 'Open Folder', os.getcwd(), options=openf)
        if folder_path:
            self.model.setRootPath(folder_path)
            self.tree_view.setRootIndex(self.model.index(folder_path))
            self.statusBar().showMessage(f'Folder opened {folder_path}', 2000)

    def copy(self):
        editor = self.tab_view.currentWidget()
        if editor is not None:
            editor.copy()

    def cut(self):
        editor = self.tab_view.currentWidget()
        if editor is not None:
            editor.cut()

    def paste(self):
        editor = self.tab_view.currentWidget()
        if editor is not None:
            editor.paste()

    def undo(self):
        editor = self.tab_view.currentWidget()
        if editor is not None:
            editor.undo()

    def redo(self):
        editor = self.tab_view.currentWidget()
        if editor is not None:
            editor.redo()


#-------------------Run Function-------------------
    # def on_tree_view_clicked(self, index: QModelIndex):
    #     path = self.model.filePath(index)
    #     # print(path)
    #     self.set_new_tab(Path(path))
    
    def error_callback(self, x):
        print('error_callback', x)
        # change to terminal tab if not already
        if not (self.terminal_frame in self.hsplit.children()):
            self.hsplit.replaceWidget(0, self.terminal_frame)
        # self.terminal_text.setText(f"Error_callback {x}")
        
        # append error to terminal GUI
        self.terminal_text.append(f"> {x}")

    def run(self):
        self.terminal_text.setText("")
        
        editor = self.tab_view.currentWidget()
        if editor is not None:
            # guardar archivo
            self.save_file()
            # correr archivo
            self.statusBar().showMessage('Running...', 2000)
            code = editor.text()
            index = self.tree_view.currentIndex()
            path = self.model.filePath(index)
            # print(path)
            input_stream = FileStream(path)
            lexer = YALPLexer(input_stream)
            lexer.addErrorListener(CustomErrorListener(self.error_callback))
            
            token_stream = CommonTokenStream(lexer)
            token_stream.fill()
            parser = YALPParser(token_stream)
            parser.addErrorListener(CustomErrorListener(self.error_callback))
            
            tree = parser.program()

            visitor = CustomVisitor(self.error_callback)
    
            try:
                visitor.visit(tree)
                if not (self.terminal_frame in self.hsplit.children()):
                    self.hsplit.replaceWidget(0, self.terminal_frame)
                self.terminal_text.setText("> Compilation successful")
            except:
                pass

            # show text in output in terminal GUI
            # self.terminal_text.setText(code)
            # print(text)
            self.statusBar().showMessage('Done', 2000)


#--------------------------------------------------

    def save_file(self):
        if self.current_file is None and self.tab_view.count() > 0:
            self.save_file_as()
            return
        
        editor = self.tab_view.currentWidget()
        self.current_file.write_text(editor.text())
        self.statusBar().showMessage(f'File saved {self.current_file.name}', 2000)

    def save_file_as(self):
        editor = self.tab_view.currentWidget()
        if editor is None:
            return
        
        file_path = QFileDialog.getSaveFileName(self, 'Save File', os.getcwd())[0]
        if file_path == '':
            self.statusBar().showMessage('File not saved', 2000)
            return
        path = Path(file_path)
        path.write_text(editor.text())
        self.tab_view.setTabText(self.tab_view.currentIndex(), path.name)
        self.statusBar().showMessage(f'File saved {path.name}', 2000)
        self.current_file = path
    
    def set_cursor_pointer(self, event):
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def set_cursor_arrow(self, event):
        self.setCursor(Qt.CursorShape.ArrowCursor)

    def get_side_bar_label(self, path, name):
        label = QLabel()
        label.setPixmap(QPixmap(path).scaled(QSize(25, 25)))
        label.setAlignment(Qt.AlignmentFlag.AlignTop)
        label.setFont(self.window_font)
        label.mousePressEvent = lambda event: self.show_hide_tab(event, name)
        # cursor shape change
        label.enterEvent = self.set_cursor_pointer
        label.leaveEvent = self.set_cursor_arrow
        return label

    def get_frame(self) -> QFrame:
        frame = QFrame()
        frame.setFrameShape(QFrame.NoFrame)
        frame.setFrameShadow(QFrame.Plain)
        frame.setContentsMargins(0, 0, 0, 0)
        frame.setStyleSheet('''
                                      QFrame {
                                            background-color: #21252b;
                                            border-radius: 5px;
                                            border: none;
                                            padding: 5px;
                                            color: #D3D3D3;
                                      }
                                      QFrame:hover {
                                            color: white;
                                        }
                                        ''')
        return frame


    def set_up_body(self):
        body_frame = QFrame()
        body_frame.setFrameShape(QFrame.NoFrame)
        body_frame.setFrameShadow(QFrame.Plain)
        body_frame.setLineWidth(0)
        body_frame.setMidLineWidth(0)
        body_frame.setContentsMargins(0, 0, 0, 0)
        body_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        body = QHBoxLayout()
        body.setContentsMargins(0, 0, 0, 0)
        body.setSpacing(0)
        body_frame.setLayout(body)

        # sidebar
        self.side_bar = QFrame()
        self.side_bar.setFrameShape(QFrame.StyledPanel)
        self.side_bar.setFrameShadow(QFrame.Plain)
        self.side_bar.setStyleSheet(f'''
                                        background-color: {self.side_bar_crl};
                                    ''')
        side_bar_layout = QVBoxLayout()
        side_bar_layout.setContentsMargins(5, 10, 5, 0)
        side_bar_layout.setSpacing(0)
        side_bar_layout.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        #set lables
        folder_label = self.get_side_bar_label('gui/icons/folder.svg', 'Folder')
        side_bar_layout.addWidget(folder_label)
        self.side_bar.setLayout(side_bar_layout)
        terminal_label = self.get_side_bar_label('gui/icons/terminal.svg', 'Terminal')
        side_bar_layout.addWidget(terminal_label)

        self.side_bar.setLayout(side_bar_layout)

        body.addWidget(self.side_bar)

        self.hsplit = QSplitter(Qt.Horizontal)

        self.tree_frame = QFrame()
        self.tree_frame.setLineWidth(1)
        self.tree_frame.setMaximumWidth(400)
        self.tree_frame.setMinimumWidth(200)
        self.tree_frame.setBaseSize(100, 0)
        self.tree_frame.setContentsMargins(0, 0, 0, 0)

        tree_frame_layout = QVBoxLayout()
        tree_frame_layout.setContentsMargins(0, 0, 0, 0)
        tree_frame_layout.setSpacing(0)
        self.tree_frame.setStyleSheet('''
                                      QFrame {
                                            background-color: #21252b;
                                            border-radius: 5px;
                                            border: none;
                                            padding: 5px;
                                            color: #D3D3D3;
                                      }
                                      QFrame:hover {
                                            color: white;
                                        }
                                        ''')
        
        # create file system model to show in tree view
        self.model = QFileSystemModel()
        self.model.setRootPath(os.getcwd())
        # File system filter
        self.model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs | QDir.Files)

        # tree view
        self.tree_view = QTreeView()
        self.tree_view.setFont(QFont('Consolas', 13))
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(os.getcwd()))
        self.tree_view.setSelectionMode(QTreeView.SingleSelection)
        self.tree_view.setSelectionBehavior(QTreeView.SelectRows)
        self.tree_view.setEditTriggers(QTreeView.NoEditTriggers)

        #add custom context menu
        self.tree_view.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree_view.customContextMenuRequested.connect(self.open_menu)
        #handling click
        self.tree_view.clicked.connect(self.on_tree_view_clicked)
        self.tree_view.setIndentation(10)
        self.tree_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # hide header and hide other columns except name
        self.tree_view.setHeaderHidden(True)
        self.tree_view.setColumnHidden(1, True)
        self.tree_view.setColumnHidden(2, True)
        self.tree_view.setColumnHidden(3, True)


        # Terminal view
        self.terminal_frame = self.get_frame()
        self.terminal_frame.setMaximumWidth(400)
        self.terminal_frame.setMinimumWidth(200)

        terminal_frame_layout = QVBoxLayout()
        terminal_frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        terminal_frame_layout.setContentsMargins(0, 10, 0, 0)
        terminal_frame_layout.setSpacing(0)
        

        self.terminal_text = QTextEdit()
        self.terminal_text.setReadOnly(True)
        self.terminal_text.setFont(self.window_font)
        self.terminal_text.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.terminal_text.setStyleSheet('''
                                        background-color: #21252b;
                                        border-radius: 5px;
                                        border: none;
                                        padding: 5px;
                                        color: #D3D3D3;
                                        ''')
        terminal_frame_layout.addWidget(self.terminal_text)
        self.terminal_frame.setLayout(terminal_frame_layout)

        # setup layout
        tree_frame_layout.addWidget(self.tree_view)
        self.tree_frame.setLayout(tree_frame_layout)

        # tab widget to add editor to
        self.tab_view = QTabWidget()
        self.tab_view.setContentsMargins(0, 0, 0, 0)
        self.tab_view.setTabsClosable(True)
        self.tab_view.setMovable(True)
        self.tab_view.setDocumentMode(True)
        self.tab_view.tabCloseRequested.connect(self.close_tab)


        # add tree view and tab view
        self.hsplit.addWidget(self.tree_frame)
        self.hsplit.addWidget(self.tab_view)

        body.addWidget(self.hsplit)
        body_frame.setLayout(body)

        self.setCentralWidget(body_frame)



        # add new frame to show output of the code
        # self.output_frame = QFrame()
        # self.output_frame.setFrameShape(QFrame.StyledPanel)
        # self.output_frame.setFrameShadow(QFrame.Plain)
        # self.output_frame.setStyleSheet('''
        #                                 background-color: #21252b;
        #                                 border-radius: 5px;
        #                                 border: none;
        #                                 padding: 5px;
        #                                 color: #D3D3D3;
        #                                 ''')
        # output_frame_layout = QVBoxLayout()
        # output_frame_layout.setContentsMargins(0, 0, 0, 0)
        # output_frame_layout.setSpacing(0)
        # self.output_frame.setLayout(output_frame_layout)

        # self.output_text = QTextEdit()
        # self.output_text.setReadOnly(True)
        # self.output_text.setFont(QFont('Consolas', 13))
        # self.output_text.setStyleSheet('''
        #                                 background-color: #21252b;
        #                                 border-radius: 5px;
        #                                 border: none;
        #                                 padding: 5px;
        #                                 color: #D3D3D3;
        #                                 ''')
        # output_frame_layout.addWidget(self.output_text)

        # self.hsplit.addWidget(self.output_frame)



    def close_tab(self, index):
        self.tab_view.removeTab(index)

    def show_hide_tab(self, event, type):
        if type == 'Folder':
            if not (self.tree_frame in self.hsplit.children()):
                self.hsplit.replaceWidget(0, self.tree_frame)
        elif type == 'Terminal':
            if not (self.terminal_frame in self.hsplit.children()):
                self.hsplit.replaceWidget(0, self.terminal_frame)
        
        if self.current_side_bar == type:
            frame = self.hsplit.children()[0]
            if frame.isHidden():
                frame.show()
            else:
                frame.hide()

        self.current_side_bar = type

    def tree_view_context_menu(self,pos):
        pass

    def on_tree_view_clicked(self, index: QModelIndex):
        path = self.model.filePath(index)
        # print(path)
        self.set_new_tab(Path(path))


    def open_menu(self, position):
        pass

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec_())