# inspired by https://daeudaeu.com/image_rotate/

# standard library
import tkinter
import tkinter.filedialog

# external library


# my module


##################
### View Class ###
##################
class View():

    def __init__(self, app):
        'コンストラクタ'

        # define
        self.master = app

        self.main_frame = MainFrame(self.master, 0, 0)

        self.canvas_frame = CanvasFrame(self.main_frame.frame, 0, 0)
        self.button_frame = ButtonFrame(self.main_frame.frame, 0, 1)

        self.before_canvas = BeforeCanvasWidget(self.canvas_frame.frame, 0, 0)
        self.after_canvas = AfterCanvasWidget(self.canvas_frame.frame, 0, 1)

        self.file_read_button = FileReadButtonWidget(self.button_frame.frame, 0, 0)
        self.invert_button = InvertButtonWidget(self.button_frame.frame, 1, 0)
        self.flip_button = FlipButtonWidget(self.button_frame.frame, 2, 0)


###################
### Frame Class ###
###################
class MainFrame:
    'アプリ全体のUIを管理するクラス'

    def __init__(self, parent=None, row=None, column=None):
        'コンストラクタ'

        self.parent = parent
        self.row = row
        self.column = column

        self.frame = tkinter.Frame(self.parent)
        self.frame.grid(row=self.row, column=self.column)


class CanvasFrame:
    'キャンバスフレームのUIを管理するクラス'

    def __init__(self, parent=None, row=None, column=None):
        'コンストラクタ'

        self.parent = parent
        self.row = row
        self.column = column

        self.frame = tkinter.Frame(self.parent)
        self.frame.grid(row=self.row, column=self.column)


class ButtonFrame:
    'ボタンフレームのUIを管理するクラス'

    def __init__(self, parent=None, row=None, column=None):
        'コンストラクタ'

        self.parent = parent
        self.row = row
        self.column = column

        self.frame = tkinter.Frame(self.parent)
        self.frame.grid(row=self.row, column=self.column)


##############
### Widget ###
##############
class BeforeCanvasWidget:
    '画像処理前の画像を表示するキャンバスUIを管理するクラス'

    def __init__(self, parent=None, row=None, column=None):
        'コンストラクタ'

        self.parent = parent
        self.row = row
        self.column = column

        self.widget = tkinter.Canvas(
            self.parent,
            width=448,
            height=448,
            bg="#FFFFFF"
        )
        self.widget.grid(row=self.row, column=self.column)
        
        
    def draw_image(self, image):
        '画像をキャンバスに描画'

        if image is not None:
            
            # キャンバス上の画像の左上座標を決定
            sx = (self.widget.winfo_width() - image.width()) // 2
            sy = (self.widget.winfo_height() - image.height()) // 2

            # キャンバスに描画済み画像を削除
            objs = self.widget.find_withtag("image")
            for obj in objs:
                self.widget.delete(obj)
            
            # 画像をキャンバスの真ん中に描画
            self.widget.create_image(
                sx, sy,
                image=image,
                anchor=tkinter.NW,
                tag="image"
            )


class AfterCanvasWidget:
    '画像処理後の画像を表示するキャンバスUIを管理するクラス'

    def __init__(self, parent=None, row=None, column=None):
        'コンストラクタ'

        self.parent = parent
        self.row = row
        self.column = column

        self.widget = tkinter.Canvas(
            self.parent,
            width=448,
            height=448,
            bg="#FFFFFF"
        )
        self.widget.grid(row=self.row, column=self.column)


    def draw_image(self, image):
        '画像をキャンバスに描画'

        if image is not None:
            # キャンバス上の画像の左上座標を決定
            sx = (self.widget.winfo_width() - image.width()) // 2
            sy = (self.widget.winfo_height() - image.height()) // 2

            # キャンバスに描画済み画像を削除
            objs = self.widget.find_withtag("image")
            for obj in objs:
                self.widget.delete(obj)

            # 画像をキャンバスの真ん中に描画
            self.widget.create_image(
                sx, sy,
                image=image,
                anchor=tkinter.NW,
                tag="image"
            )

class FileReadButtonWidget:
    '画像ファイル読み込みボタンUIを管理するクラス'

    def __init__(self, parent=None, row=None, column=None):
        'コンストラクタ'

        self.parent = parent
        self.row = row
        self.column = column

        self.widget = tkinter.Button(
            self.parent,
            text="ファイル選択",
            width=10
        )
        self.widget.grid(row=self.row, column=self.column)
        

    def select_file(self):
        'ファイル選択画面を表示'

        file_path = tkinter.filedialog.askopenfilename(
            initialdir = "."
        )
        return file_path


class InvertButtonWidget:
    'ネガポジ処理ボタンUIを管理するクラス'

    def __init__(self, parent=None, row=None, column=None):
        'コンストラクタ'

        self.parent = parent
        self.row = row
        self.column = column

        self.widget = tkinter.Button(
            self.parent,
            text="ネガポジ",
            width=10
        )
        self.widget.grid(row=self.row, column=self.column)


class FlipButtonWidget:
    '左右反転処理ボタンUIを管理するクラス'

    def __init__(self, parent=None, row=None, column=None):
        'コンストラクタ'

        self.parent = parent
        self.row = row
        self.column = column

        self.widget = tkinter.Button(
            self.parent,
            text="左右反転",
            width=10
        )
        self.widget.grid(row=self.row, column=self.column)
    