from langchain_openai import ChatOpenAI
from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from dotenv import load_dotenv
import os
from pathlib import Path
import asyncio

# 環境変数のロード
load_dotenv()

# ブラウザ設定
browser = Browser(
    config=BrowserConfig(
        chrome_instance_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
    )
)

# コントローラの初期化
controller = Controller()

# プロンプトを読み込む関数
def load_prompt(file_path):
    with Path(file_path).open('r', encoding='utf-8') as file:
        return file.read()

# 任意のタスクを実行する関数
def create_and_run_agent(file_path, agent):
    prompt_content = load_prompt(file_path)
    agent.task = prompt_content
    return agent.run()

# エージェントのメイン処理
async def main():
    agent = Agent(
        task="",  # 初期タスクは空で設定
        llm=ChatOpenAI(model="gpt-4o"),
        controller=controller,
        browser=browser,
    )

    # タスク1の実行
    result1 = await create_and_run_agent('C:/Develop/Browser Use/Prompt/X_search_LLMInfo_summary_Prompt.txt', agent)
    print("タスク1の結果:", result1)

    # タスク2の実行
    result2 = await create_and_run_agent('C:/Develop/Browser Use/Prompt/X_search_LLMInfo_summary_Prompt2.txt', agent)
    print("タスク2の結果:", result2)

# 非同期処理の実行
if __name__ == "__main__":
    asyncio.run(main())
