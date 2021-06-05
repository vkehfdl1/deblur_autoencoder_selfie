# Deblurring selfies using convolutional auto encoder
## Kyung Hee Univ. Web/Python term project

### Overview
CCTV 노후화 등으로 인하여 과속 차량이나 흉악범의 얼굴 등이 잘 보이지 않는 경우가 다반사이다. 이렇게 카메라가 흔들리거나 저화질인 경우, 모자이크 처리되어 있는 경우 신원을 파악하기 힘들 수 있다. 이러한 경우, 인공지능을 이용해 사람의 사진을 식별할 수 있을 만큼 복원할 수 있지 않을까 생각했다. 이를 위하여 Convolutional auto encoder 기술을 이용하여 모자이크 처리 되거나 심하게 손상된 사람들의 사진을 복원할 수 있는 인공지능을 제작하고자 한다. 

### notebooks

- [텀프로젝트 제안서](./term_project_proposal.md)
- [텀프로젝트 중간 보고서](./2020103913_term_project_mid_term_report.ipynb)
- [텀프로젝트 최종 보고서](./2020103913_term_project_final_report.ipynb)
- [인스타그램에서 데이터 크롤링](./get_data_insta.ipynb)
- [이미지 visualization 및 얼굴 detection](./preprocess_pics.ipynb)
- [이미지 blur 처리 및 저장](./blurring_img.ipynb)
- [이미지 motion blur 처리](./motion_blurring_img.ipynb)
- [blur - deblur 전체 과정](./deblur_process.py)

### 사용 기술

[본 논문](https://jiaya.me/papers/deblur_cvpr19.pdf)과 [구현 코드](https://github.com/firenxygao/deblur)를 통한 auto encoder 모델을 이용하여 motion blur를 크게 줄이는 네트워크를 실험하였습니다. 해당 코드를 이용하고, 직접 수집한 사진 데이터에 적용하기 쉽게 python 파일로 정리하는 과정을 거쳤습니다. 아래 결과에서 보이는 것처럼 사람 얼굴에 대한 motion blur를 획기적으로 줄일 수 있습니다. 

### 프로젝트 결과



### 참고 문헌

#### 라이브러리

1. [Selenium](https://www.selenium.dev/documentation/ko/)
2. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
3. [imgaug](https://github.com/aleju/imgaug)
4. [keras.preprocessing](https://keras.io/api/preprocessing/image/)
5. [scikit-learn](https://scikit-learn.org/)
6. [Tensorflow](https://www.tensorflow.org/?hl=ko)
7. [OpenCV](https://opencv.org/)
8. [Pillow](https://pillow.readthedocs.io/en/stable/)
9. [Albumentations](https://github.com/albumentations-team/albumentations)

#### 참고 코드
1. [De-blurring images using convolutional auto encoder](https://levelup.gitconnected.com/de-blurring-images-using-convolutional-neural-networks-with-code-51d3f8d7b1d7)
2. [Image Deblurring Auto Encoder Network](https://github.com/AryanSethi/Deblurring_autoencoder)
3. [파이썬으로 인스타그램 이미지 크롤링하여 다운로드하기](https://dahaha.tistory.com/76)
4. [DeblurGAN](https://github.com/KupynOrest/DeblurGAN)
5. [Deblur](https://github.com/firenxygao/deblur)

#### 관련 논문
1. [Image Restoration using Autoencoding Priors](https://www.google.com/url?sa=t&source=web&rct=j&url=https://arxiv.org/pdf/1703.09964&ved=2ahUKEwi0tIGoh5bwAhVVL6YKHW4mATgQFjAAegQIBBAC&usg=AOvVaw0TPO4x4mcIveMqJFVMLPr9)
2. [DeblurGAN: Blind Motion Deblurring Using Conditional Adversarial Networks](https://arxiv.org/abs/1711.07064)
3. [Dynamic Scene Deblurring with Parameter Selective Sharing and Nested Skip Connections](https://jiaya.me/papers/deblur_cvpr19.pdf)

### Contact

질문 등 연락할 사항이 있으면 vkehfdl1@khu.ac.kr로 연락해주세요. 