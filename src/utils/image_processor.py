"""
圖像處理器模塊
定義用於處理圖像的實用工具
"""
from PIL import Image
import io

class ImageProcessor:
    """圖像處理器"""
    
    def __init__(self):
        """初始化圖像處理器"""
        pass
    
    def load_image(self, image_path: str) -> Image.Image:
        """
        加載圖像
        
        Args:
            image_path: 圖像文件路徑
            
        Returns:
            PIL 圖像對象
        """
        return Image.open(image_path)
    
    def resize_image(self, image: Image.Image, size: tuple) -> Image.Image:
        """
        調整圖像大小
        
        Args:
            image: PIL 圖像對象
            size: 目標大小 (寬, 高)
            
        Returns:
            調整大小後的 PIL 圖像對象
        """
        return image.resize(size)
    
    def convert_to_bytes(self, image: Image.Image, format: str = 'PNG') -> bytes:
        """
        將圖像轉換為字節
        
        Args:
            image: PIL 圖像對象
            format: 圖像格式 (例如: PNG, JPEG)
            
        Returns:
            圖像的字節表示
        """
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format=format)
        img_byte_arr = img_byte_arr.getvalue()
        return img_byte_arr