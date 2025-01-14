"""
UI 佈局模塊
定義應用程序的用戶界面佈局
"""
import streamlit as st
import asyncio
from src.agents.slogan_agent import SloganAgent
from src.agents.inspect_agent import InspectAgent
from src.agents.score_agent import ScoreAgent
from src.agents.best_slogan_agent import BestSloganAgent

async def process_agents(user_input: str, iteration: int) -> dict:
    """處理一次代理團隊的運行"""
    results = {
        "iteration": iteration,
        "slogan": None,
        "inspection": None,
        "score": None,
        "optimization": None  # 儲存優化建議
    }
    
    try:
        # 創建代理團隊
        slogan_agent = SloganAgent()
        inspect_agent = InspectAgent()
        score_agent = ScoreAgent()
        best_slogan_agent = BestSloganAgent()
        
        # 生成標語
        results["slogan"] = await slogan_agent.process(user_input)
        
        # 檢查標語
        results["inspection"] = await inspect_agent.process(user_input, results["slogan"])
        
        # 評分
        results["score"] = await score_agent.process(results["slogan"], results["inspection"])
        
        # 立即根據評分結果獲取優化建議
        optimization_result = await best_slogan_agent.process([{
            "slogan": results["slogan"],
            "score": results["score"]
        }])
        results["optimization"] = optimization_result["analysis"]
        
        return results
    except Exception as e:
        st.error(f"第 {iteration} 次生成時發生錯誤: {str(e)}")
        return results

def create_ui():
    st.set_page_config(
        page_title="AI 廣告標語生成系統",
        page_icon="🎯",
        layout="wide"
    )
    
    st.title("🎯 AI 廣告標語生成系統")
    
    # 側邊欄：系統說明
    with st.sidebar:
        st.subheader("系統說明")
        st.markdown("""
        ### 🤖 AI 代理團隊
        
        1. **🎨 標語生成代理**
           - 根據產品資訊生成吸引人的廣告標語
        
        2. **🔍 標語檢查代理**
           - 分析標語是否有效參考產品特點
        
        3. **⭐ 評分代理**
           - 為標語提供專業評分和建議
        """)
    
    # 主要內容區域
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("📝 輸入產品資訊")
        user_input = st.text_area(
            "請詳細描述您的產品特點",
            height=150,
            placeholder="例如：這是一款創新的智能手錶，具有心率監測和運動追蹤功能..."
        )
        
        iterations = st.number_input("生成次數", min_value=1, max_value=10, value=3)
        generate_button = st.button("✨ 開始生成", type="primary")
        
    with col2:
        if generate_button and user_input:
            # 創建進度條
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            with st.spinner("🤖 AI 團隊正在協作中..."):
                # 創建一個 tab 列表來顯示所有結果
                tabs = st.tabs([f"第 {i+1} 次" for i in range(iterations)])
                
                # 非同步處理多次生成
                results = []
                for i in range(iterations):
                    # 更新進度顯示
                    current_progress = (i + 1) / iterations
                    progress_bar.progress(current_progress)
                    status_text.markdown(f"### 🔄 正在執行第 {i + 1}/{iterations} 次生成...")
                    
                    result = asyncio.run(process_agents(user_input, i+1))
                    results.append(result)
                    
                    # 在對應的 tab 中顯示結果
                    with tabs[i]:
                        # 標語結果
                        st.markdown(f"### 🎨 第 {i+1} 次標語生成")
                        st.success(f"生成的標語：\n\n{result['slogan']}")
                        
                        # 分析結果
                        st.markdown("### 🔍 標語分析")
                        inspection = result['inspection']
                        if inspection:
                            st.info(inspection["analysis"])
                        
                        # 評分結果與優化建議
                        col1, col2 = st.columns([1, 1])
                        
                        with col1:
                            st.markdown("### ⭐ 最終評分")
                            score_result = result['score']
                            if score_result:
                                st.metric("分數", f"{score_result['score']}/5")
                                st.markdown(score_result["feedback"])
                        
                        with col2:
                            st.markdown("### 💡 優化建議")
                            if result.get("optimization"):
                                st.info(result["optimization"])
                
                # 完成所有生成後
                progress_bar.progress(1.0)
                status_text.markdown("### ✅ 所有標語生成完成！")
                
                # 顯示最佳結果
                st.markdown("---")
                # st.subheader("🏆 最佳標語")
                # best_result = max(results, key=lambda x: x['score']['score'] if x['score'] else 0)
                # st.success(f"推薦標語：\n\n{best_result['slogan']}")
                # st.metric("最終評分", f"{best_result['score']['score']}/5")
        else:
            st.info("👈 請在左側輸入產品資訊並點擊「開始生成」按鈕")
            
    # 頁腳
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center'>
        <p>AI 廣告標語生成系統 | 由RayLin協作技術驅動</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    create_ui()