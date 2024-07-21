import streamlit as st
import re
import pandas as pd

print("start")
st.set_page_config(
    page_title="Mate"
    #page_icon=
)

if 'page' not in st.session_state:
    st.session_state.page = 'main'

def switch_page(page):
    st.session_state.page = page
    st.experimental_rerun()

def extract_urls(text, max_urls=3):
    # URL 추출을 위한 정규 표현식 패턴
    url_pattern = re.compile(r'(https?://\S+)')
    urls = url_pattern.findall(text)
    # 최대 max_urls 개수만큼 URL 추출
    return urls[:max_urls]

st.markdown(
    """
    <style>
    .fixed-width-container {
        width: 1910px;
        background-color: #f0f0f0;
        margin: 0 auto;  /* 가운데 정렬을 위해 */
    }
    
    [data-testid="stMarkdownContainer"] {
    }
    
    </style>
    """,
    unsafe_allow_html=True
)

youtube_physical=[
    "https://www.youtube.com/watch?v=Cmt82yiNtQo",
    "https://www.youtube.com/watch?v=EcFVv-Ktj-U",
    "https://www.youtube.com/watch?v=IFnU3sYNs1U",
    "https://www.youtube.com/watch?v=28kn2IQEWRk",
    "https://www.youtube.com/watch?v=jIxspQ2Z2zo",
    "https://www.youtube.com/watch?v=os8Vym4xQwM"
]

youtube_mental=[
    "https://www.youtube.com/watch?v=mxq81tdtPXA",
    "https://www.youtube.com/watch?v=uvy9T_coMYw",
    "https://www.youtube.com/watch?v=iKPK99hQAJk",
    "https://www.youtube.com/watch?v=ULWUxxhzlo8",
    "https://www.youtube.com/watch?v=2u3G-vHNWLs",
    "https://www.youtube.com/watch?v=jpN8YqQV1N0"
]

def chat(inputs):
    st.session_state.input = inputs
    #여기에 코랩 연결 필요합니다.
    output="코랩연결 https://www.youtube.com/watch?v=Cmt82yiNtQo https://www.youtube.com/watch?v=jIxspQ2Z2zo https://www.youtube.com/watch?v=os8Vym4xQwM"
    #여기에 코랩 연결 필요합니다.
    st.session_state.answer = extract_urls(output, 3)
    print("gpt 실행")
    switch_page("result")

@st.experimental_dialog("추천 영상입니다.")    
def movie(url):
    st.video(url)
#=================[ 함수 / 작동 부분 ]===============
if st.button("Mate"):
    print("메인으로 넘어가기")
    switch_page("main")

if st.session_state.page == 'main':
    st.subheader("장애 아동에게 꼭 필요한 학습 컨텐츠를 쉽고 간편하게 제공합니다.")
    
    if st.button("컨텐츠 추천받기"):
        print("챗봇으로 넘어가기")
        switch_page("search")
    
    st.subheader("몸이 불편한 아동을 위한 추천 컨텐츠")
    with st.container(height=220, border=1):
        psc=st.columns(6)
        for i in range(6):
            with psc[i]:
                if st.button(youtube_physical[i]):
                    movie(youtube_physical[i])
    st.subheader("마음이 불편한 아동을 위한 추천 컨텐츠")
    with st.container(height=220, border=1):
        mtl=st.columns(6)
        for i in range(6):
            with mtl[i]:
                if st.button(youtube_mental[i]):
                    movie(youtube_mental[i])
    

elif st.session_state.page == 'search':
    st.markdown("원하시는 컨텐츠가 있나요?")
    st.markdown("AI가 원하시는 학습 컨텐츠를 찾아드릴게요.")
    col0, col1 = st.columns([1, 12])
    with col0:
        with st.popover(""):
            st.subheader("추천해드려요")
            if st.button("추천 1"):
                chat("추천 1")
            if st.button("추천 2"):
                chat("추천 2")
            if st.button("추천 3"):
                chat("추천 3")
    with col1:
        input_text = st.chat_input("여기에 입력해주세요.")
        if input_text:
            chat(input_text)     
                    
elif st.session_state.page == 'result':
    col0, col1 = st.columns([1, 12])
    with col0:
        with st.popover(""):
            st.subheader("추천해드려요")
            if st.button("추천 1"):
                chat("추천 1")
            if st.button("추천 2"):
                chat("추천 2")
            if st.button("추천 3"):
                chat("추천 3")
    with col1:
        input_text = st.chat_input("여기에 입력해주세요.")
        if input_text:
            chat(input_text)
    st.title(f"'{st.session_state.input}' 검색 결과")
    ytv = st.columns(3)
    for i in range(3):
        with ytv[i]:
            print(st.session_state.answer[i])
            st.video(st.session_state.answer[i])