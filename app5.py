import streamlit as st
import pandas as pd
# 이미지 처리를 위한 라이브러리
from PIL import Image



def main():

    img = Image.open('data/image_03.jpg')
    print(img)
    st.image(img)
    
    st.image(img, use_column_width=True) # 가로로 꽉차게

    # 이미지 url 복사해도됨
    st.image('https://coinpan.com/files/attach/images/198/714/226/258/e423348281ef542957b9315d5bf5fa6b.jpg')

    video_file = open('data/Seoul.mp4', 'rb') # rb = 읽기,바이너리
    st.video(video_file)

    # audio_file = open( 'data/song.mp3', 'rb' )
    # st.audio( audio_file.read(), format = 'audio/mp3' )


if __name__ == '__main__' :
    main()
