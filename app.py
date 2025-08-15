from dotenv import load_dotenv
load_dotenv()


from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

import os
import streamlit as st

# ChatOpenAIインスタンスを有効化
llm = ChatOpenAI(model_name="gpt-4o", temperature=0.5)

st.title("Lesson21: Chapter6: LLM機能を搭載したWebアプリ開発")

st.write("##### 動作モード1: 健康専門家")
st.write("入力フォームにテキストを入力してください。健康専門家の回答が得られます。")
st.write("##### 動作モード2: 料理専門家")
st.write("入力フォームにテキストを入力してください。料理専門家の回答が得られます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["健康専門家", "料理専門家"]
)

st.divider()

# 入力値を先に取得
if selected_item == "健康専門家":
    input_message = st.text_input(label="健康専門家に聞きたい質問を入力してください。")
    system_prompt = "あなたは健康に関するアドバイザーです。健康関連のアドバイスを提供してください。"
else:
    input_message = st.text_input(label="料理専門家に聞きたい質問を入力してください。")
    system_prompt = "あなたは料理に関するアドバイザーです。料理関連のアドバイスを提供してください。"

# 実行ボタンが押されたときのみAPIを呼び出す
if st.button("実行"):
    st.divider()
    if input_message:
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=input_message)
        ]
        result = llm(messages)
        st.write(f"回答: **{result.content}**")
    else:
        st.error(f"{selected_item}に聞きたい質問を入力してから「実行」ボタンを押してください。")