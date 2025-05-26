import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import matplotlib.font_manager as fm

# 폰트 경로 지정 (프로젝트 내 경로)
font_path = "fonts/NanumGothic.ttf"
font_prop = fm.FontProperties(fname=font_path)

# 사용자 입력 받기
st.title("정규분포 시각화 웹앱")

mean = st.number_input("평균 (μ)", value=0.0)
std_dev = st.number_input("표준편차 (σ)", value=1.0, min_value=0.01)

x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 500)
y = norm.pdf(x, mean, std_dev)

fig, ax = plt.subplots()
ax.plot(x, y, label=f'μ={mean}, σ={std_dev}')
ax.fill_between(x, y, alpha=0.2)
ax.set_title("정규분포 곡선", fontproperties=font_prop)
ax.set_xlabel("x", fontproperties=font_prop)
ax.set_ylabel("확률 밀도", fontproperties=font_prop)
ax.legend(prop=font_prop)

st.pyplot(fig)
