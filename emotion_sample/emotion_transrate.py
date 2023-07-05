#!/usr/bin/env python3

# 必要なライブラリをインポート
import cv2
import boto3

# カメラの設定
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# AWSを使う準備
rekognition_client = boto3.client(service_name="rekognition")
translate_client = boto3.client(service_name="translate")


while True:
    success, image = cap.read()

    # 画像の表示
    cv2.imshow("USB Camera", image)
    key = cv2.waitKey(1)

    if key == ord("s"):
         # OpenCVで画像をPNG形式の画像データ（バイトデータ）に変換
        byte_image = cv2.imencode(".PNG", image)[1].tobytes()
        
        # AWSで顔の情報を調べる
        detect_faces_response = rekognition_client.detect_faces(
            Image={"Bytes": byte_image},
            Attributes=["ALL"]
        )["FaceDetails"]

        # 1個以上、認識できていたら処理を実行
        if len(detect_faces_response) > 0:
            # 表情のデータを取り出す
            emotion = detect_faces_response[0]["Emotions"][0]["Type"]

            # 表情データは英語で返ってくるので、日本語に翻訳
            translated_emotion = translate_client.translate_text(
                Text=emotion, SourceLanguageCode="en", TargetLanguageCode="ja"
            )["TranslatedText"]

            # 結果を画面に表示
            print("表情認識の結果: {}".format(translated_emotion)) 