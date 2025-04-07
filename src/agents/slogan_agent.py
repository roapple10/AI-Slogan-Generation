from google import genai
import os
from dotenv import load_dotenv

class SloganAgent:
    def __init__(self):
        try:
            # 確保環境變數已載入
            load_dotenv()
            
            # 從環境變數獲取 API KEY 和 MODEL NAME
            api_key = os.getenv("GOOGLE_API_KEY")
            model_name = os.getenv("MODEL_NAME")
            
            if not api_key:
                raise ValueError("GOOGLE_API_KEY not found in environment variables")
            if not model_name:
                raise ValueError("MODEL_NAME not found in environment variables")
                
            # 初始化 client
            self.client = genai.Client(api_key=api_key)
            self.model_name = model_name
            
        except Exception as e:
            raise Exception(f"Error initializing SloganAgent: {str(e)}")

    async def process(self, user_input: str) -> str:
        """根據使用者輸入生成廣告標語"""
        prompt = f"""
        請使用繁體中文，根據以下產品資訊，生成一個吸引人的廣告標語：

        產品資訊：
        {user_input}

        要求：
        1. 必須使用繁體中文回答
        2. 標語字數限制在40字以內
        3. 需要突出產品的主要特點和優勢
        4. 使用簡潔有力的語言
        5. 標語需要具有吸引力和記憶點
        6. 必須要包含產品的關鍵特點（如：零手續費、專家管理等）
        
        請直接輸出標語，不需要其他解釋。
        """
        
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            return response.text.strip()
        except Exception as e:
            raise Exception(f"Error generating slogan: {str(e)}")

    def get_response(self) -> str:
        return self.response