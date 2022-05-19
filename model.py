# inspired by https://daeudaeu.com/image_rotate/

# standard library
import tkinter

# external library
from PIL import Image, ImageOps, ImageTk
import cv2 
import numpy as np

# my module


###################
### Model Class ###
###################
class Model:
    
    def __init__(self):
        'コンストラクタ'
        
        """
        Tk <= PIL <=> openCV 
        """
        
        # PIL画像オブジェクト参照（画像の状態を管理）
        self.before_pil_image = None
        self.after_pil_image = None
        
        # # Tkinter画像オブジェクト参照（画像の表示用）
        self.before_tk_image = None
        self.after_tk_image = None
        
        
    def set_before_pil_image(self, file_path):
        '画像ファイルのパスを指定してPIL画像として読み込む'

        if len(file_path) != 0:
            
            self.before_tk_image = None
            self.after_tk_image = None

            self.before_pil_image = Image.open(file_path).convert('RGB')
            self.after_pil_image = Image.open(file_path).convert('RGB')
            
            
    def get_before_tk_image(self):
        'GUI上で表示するためにTkinter画像を返す'

        if self.before_pil_image is not None:

            # GUI上で表示したいタイミングのみでpil->tkに変換すると間違いが少なそう
            self.before_tk_image = self.pil_to_tk(self.before_pil_image)
            
            return self.before_tk_image
        
    
    def get_after_tk_image(self):
        'GUI上で表示するためにTkinter画像を返す'

        if self.after_pil_image is not None:

            # GUI上で表示したいタイミングのみでpil->tkに変換すると間違いが少なそう
            self.after_tk_image = self.pil_to_tk(self.after_pil_image)

            return self.after_tk_image


    #-----------------------#
    #-- Convert Data Type --#
    #-----------------------#
    def pil_to_tk(self, pil_image):
        'PIL画像オブジェクト -> Tkinter画像オブジェクト'

        if pil_image is not None:

            # PIL画像オブジェクトをTkinter画像オブジェクトに変換
            tk_image = ImageTk.PhotoImage(pil_image)

            return tk_image
        

    def pil_to_cv2(self, pil_image):
        'PIL画像オブジェクト -> OpenCV画像オブジェクト'

        if pil_image is not None:

            # PIL画像オブジェクトをNumpy配列に変換
            pil_image_array = np.array(pil_image)

            # RGB -> BGR
            cv2_image = cv2.cvtColor(pil_image_array, cv2.COLOR_RGB2BGR)

            return cv2_image


    def cv2_to_pil(self, cv2_image):
        'OpenCV画像オブジェクト -> PIL画像オブジェクト'

        if cv2_image is not None:

            # BGR -> RGB
            rgb_cv2_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)

            # Numpy配列をPIL画像オブジェクトに変換
            pil_image = Image.fromarray(rgb_cv2_image)

            return pil_image


    #--------------------------#
    #-- PIL Image Processing --#
    #--------------------------#
    def invert(self):
        
        if self.after_pil_image is not None:
            
            self.after_pil_image = ImageOps.invert(self.after_pil_image)    # PILの関数適用

    
    #-----------------------------#
    #-- OpenCV Image Processing --#
    #-----------------------------#
    def flip(self):

        if self.after_pil_image is not None:

            src = self.pil_to_cv2(self.after_pil_image) # PIL -> OpenCV

            dst = cv2.flip(src, 1)  # OpenCVの関数適用

            self.after_pil_image = self.cv2_to_pil(dst) # OpenCV -> PIL

