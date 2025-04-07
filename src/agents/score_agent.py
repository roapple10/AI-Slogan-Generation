from google import genai
import os
import re
from dotenv import load_dotenv

class ScoreAgent:
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
            raise Exception(f"Error initializing ScoreAgent: {str(e)}")

    def extract_score(self, feedback: str) -> int or None:
        """從回應中提取分數"""
        score_patterns = [
            r'分數：(\d+)分',  # 標準格式
            r'分數:(\d+)分',   # 冒號無空格
            r'分數：(\d+)',    # 無"分"字
            r'分數:(\d+)',     # 無空格無"分"字
        ]
        
        for pattern in score_patterns:
            match = re.search(pattern, feedback)
            if match:
                score = int(match.group(1))
                if 1 <= score <= 5:
                    return score
        return None

    async def process(self, slogan: str, inspection_result: dict) -> dict:
        """根據標語和檢查結果給出評分"""
        prompt = f"""
        請使用繁體中文，為以下廣告標語評分。
        注意：必須以「分數：X分」格式開始回答，其中X必須是1到5的整數。

        廣告標語：
        {slogan}

        檢查結果：
        {inspection_result['analysis']}

        評分要求：
        1. 必須使用繁體中文回答
        2. 必須以「分數：X分」開始回答
        3. X必須是1-5之間的整數
        4. 5分：標語完全符合要求，明確參考產品特點
        5. 1分：標語完全未參考產品特點
        
        回答格式：
        分數：X分
        
        評分理由：
        （請說明評分理由）
        
        改進建議：
        （如有需要請提供改進建議）
        """
        
        max_retries = 3
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                response = self.client.models.generate_content(
                    model=self.model_name,
                    contents=prompt
                )
                feedback = response.text.strip()
                
                # 提取分數
                score = self.extract_score(feedback)
                
                if score is not None:
                    return {
                        "score": score,
                        "feedback": feedback
                    }
                
                # 如果沒有得到有效分數，添加更明確的提示重試
                prompt = f"""
                上次回答未包含正確格式的分數。請嚴格按照以下格式重新評分：

                1. 必須以「分數：X分」開始（X是1-5之間的整數）
                2. 接著提供評分理由
                3. 最後提供改進建議

                廣告標語：
                {slogan}

                請重新評分：
                """
                retry_count += 1
                
            except Exception as e:
                raise Exception(f"Error scoring slogan: {str(e)}")
        
        raise Exception("無法獲得有效的評分結果，請重試")

    def get_response(self) -> str:
        return self.response 