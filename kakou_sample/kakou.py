#!/usr/bin/env python3

# 必要なライブラリをインポート
import cv2

# 2枚の画像を合成して加工する関数
def kakou_image(s_image, e_image):
    g_image = s_image * (1 - e_image[:, :, 3:] / 255) + e_image[:, :, :3] * (e_image[:, :, 3:] / 255)
    return g_image.astype("uint8")

# バナナの画像を読み込む
banana_image = cv2.imread("images/banana.png")

# 合成に使う画像を読み込む
happy_image = cv2.imread("images/happy.png", cv2.IMREAD_UNCHANGED)

# 2枚の画像を合成して加工する
kakou_banana = kakou_image(banana_image, happy_image)

# 画像を保存
cv2.imwrite("kakou_banana.png", kakou_banana)

# 画像を画面に表示
cv2.imshow("kakou Banana Image", kakou_banana)
cv2.waitKey(0)