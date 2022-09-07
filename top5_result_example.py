
import os
from Top5_Result import top5_result

filepath = '/Users/dyson/Desktop/STUDY/CS/CP1/Test_Image/감자조림/Image_10.jpg' # 이미지 경로

model_dir = '/Users/dyson/Desktop/STUDY/CS/CP1/Top5_Result/model/' # 모델 저장 폴더
model_name = os.listdir(model_dir)[0]

# 결과는 dictionary 형태로 반환됩니다.
print(top5_result.image_prediction_result(filepath, model_dir, model_name))