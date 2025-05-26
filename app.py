import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# 앱 제목
st.title("정규분포 시각화 웹앱")

# 사용자 입력 받기
mean = st.number_input("평균 (μ)", value=0.0)
std_dev = st.number_input("표준편차 (σ)", value=1.0, min_value=0.01)

# x값 범위 설정
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 500)
y = norm.pdf(x, mean, std_dev)

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label=f'μ={mean}, σ={std_dev}')
ax.fill_between(x, y, alpha=0.2)
ax.set_title("정규분포 곡선")
ax.set_xlabel("x")
ax.set_ylabel("확률 밀도")
ax.legend()

st.pyplot(fig)
