import cv2
import numpy as np


# 문제 1.
#
# BGR 이미지를 HSV 이미지로 변환하세요.
#
# OpenCV 함수를 활용하세요.
def convert_to_hsv(image):
    raise NotImplementedError


# 문제 2.
#
# BGR 이미지를 LAB 이미지로 변환하세요.
#
# OpenCV 함수를 활용하세요.
def convert_to_lab(image):
    raise NotImplementedError


# 문제 3.
#
# 지정한 채널의 평균값을 계산하세요.
#
# channel_index는 사용할 채널 번호입니다.
#
# 예시
# BGR
# 0 -> B
# 1 -> G
# 2 -> R
#
# HSV
# 0 -> H
# 1 -> S
# 2 -> V
#
# LAB
# 0 -> L
# 1 -> A
# 2 -> B
def calculate_channel_mean(
    image,
    channel_index,
):
    raise NotImplementedError


# 문제 4.
#
# Color Mask를 생성하세요.
#
# image는 HSV 또는 LAB 이미지입니다.
#
# lower와 upper는 각각
# 색상 범위의 하한과 상한입니다.
#
# OpenCV 함수를 활용하세요.
def create_color_mask(
    image,
    lower,
    upper,
):
    raise NotImplementedError


# 문제 5.
#
# Binary Mask에서 활성 픽셀 개수를 계산하세요.
#
# 활성 픽셀은 값이 255인 픽셀입니다.
#
# 반환값은 픽셀 개수입니다.
def count_mask_pixels(mask):
    raise NotImplementedError
