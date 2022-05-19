# inspired by https://daeudaeu.com/image_rotate/

# standard library
import tkinter

# external library


# my module


#########################
### Contoroller Class ###
#########################
class Controller():

    INTERVAL = 50

    def __init__(self, app, model, view):
        'コンストラクタ'

        # 引数の受け取り
        self.master = app

        self.model = model
        self.view = view


        # ボタンとイベントを紐付け
        self.view.file_read_button.widget['command'] = self.push_load_button
        self.view.invert_button.widget['command'] = self.push_invert_button
        self.view.flip_button.widget['command'] = self.push_flip_button


    #----------------#
    #-- Draw Image --#
    #----------------#
    def draw_before_image(self):
    
        # モデルからTk画像の取得
        before_image = self.model.get_before_tk_image()
        
        # 画像ウィジェットにTK画像を渡して描画
        self.view.before_canvas.draw_image(before_image)
        
        
    def draw_after_image(self):
        
        # モデルからTk画像の取得
        after_image = self.model.get_after_tk_image()
        
        # 画像ウィジェットにTK画像を渡して描画
        self.view.after_canvas.draw_image(after_image)


    #-----------#
    #-- Event --#
    #-----------#
    def push_load_button(self):
        'ファイル選択ボタンが押された時の処理'

        # ファイル選択画面表示してファイルパスを取得
        file_path = self.view.file_read_button.select_file()

        # 画像ファイルの読み込み
        self.model.set_before_pil_image(file_path)

        # 描画
        self.draw_before_image()


    def push_invert_button(self):
        '画像処理ボタンが押されたときの処理'
        
        # ネガポジ処理
        self.model.invert()
        
        # 画像を再描画
        self.draw_after_image()


    def push_flip_button(self):
        '画像処理ボタンが押されたときの処理'
        
        # ネガポジ処理
        self.model.flip()
        
        # 画像を再描画
        self.draw_after_image()

        