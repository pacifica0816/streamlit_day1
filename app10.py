import streamlit as st
# 다른 파일에 있는 함수를 사용하기 위해서 import 한다.
from eda_app import run_eda_app
from ml_app import run_ml_app

 
def main():
    st.title('파일 분리 앱')
    
    menu = ['Home', 'EDA', 'ML', "About"]

    choice = st.sidebar.selectbox('메뉴', menu)
    
    if choice == 'Home' :
        st.subheader('홈 화면입니다.')

    elif choice == 'EDA' :
        run_eda_app()

    elif choice == 'ML' :
        run_ml_app()

    else :
        st.subheader('앱 소개 화면입니다.')


if __name__ == '__main__' :
    main()

