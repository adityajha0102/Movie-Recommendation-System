import streamlit as st
import base64


def header(url):
    st.markdown(f'<p style="color:#DC143C;font-size:45px;">{url}</p>',
                unsafe_allow_html=True)


def header2(url):
    st.markdown(f'<p style="color:#DC143C;font-size:30px;">{url}</p>',
                unsafe_allow_html=True)


def header3(url):
    st.markdown(f'<p style="color:#DC143C;font-size:22px;">{url}</p>',
                unsafe_allow_html=True)


def header4(url):
    st.markdown(
        f'<p style="color:#DC143C;font-size:18px;border: 2px solid #e6e9ef; border-radius: 1rem;padding: 0.5rem ;">{url}</p>',
        unsafe_allow_html=True)


def header5(url):
    st.markdown(f'<p style=text-align:center;"color:#DC143C;font-size:40px;">{url}</p>',
                unsafe_allow_html=True)


def main_movie_name(url):
    st.markdown(f'<p style=text-align:center;"color:#DC143C;font-size:28px;">{url}</p>',
                unsafe_allow_html=True)


def movie_name(url):
    st.markdown(f'<p style=text-align:center;"color:#DC143C;font-size:20px;">{url}</p>',
                unsafe_allow_html=True)


def background_image():
    main_bg = "image.jpg"
    main_bg_ext = "jpg"
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
