from phi.agent import Agent
from phi.model.google import Gemini
import os
from dotenv import load_dotenv

class SloganAgent:
    def __init__(self):
        try:
            # 確保環境變數已載入
            load_dotenv()
            
            # 從環境變數獲取 API KEY
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                raise ValueError("GOOGLE_API_KEY not found in environment variables")
            
            # 初始化 model
            model = Gemini(id="gemini-pro", api_key=api_key)
            
            # 初始化 agent
            self.agent = Agent(
                model=model,
                instructions=[
                    "You are a creative advertising slogan expert that:",
                    "1. Creates catchy and memorable slogans",
                    "2. Highlights key product features",
                    "3. Uses concise and impactful language",
                    "4. Ensures slogans are under 40 characters",
                    "Be specific and focused on the product's unique selling points"
                ],
                markdown=True
            )
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
            # 使用同步方式調用
            response = self.agent.run(message=prompt)
            # return "這是個錯誤" 
            return response.content.strip()
        except Exception as e:
            raise Exception(f"Error generating slogan: {str(e)}")

    def get_response(self) -> str:
        return self.response