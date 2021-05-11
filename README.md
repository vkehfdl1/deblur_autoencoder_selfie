# Deblurring selfies using convolutional auto encoder
## Kyung Hee Univ. Web/Python term project

### Overview
CCTV 노후화 등으로 인하여 과속 차량이나 흉악범의 얼굴 등이 잘 보이지 않는 경우가 다반사이다. 이렇게 카메라가 흔들리거나 저화질인 경우, 모자이크 처리되어 있는 경우 신원을 파악하기 힘들 수 있다. 이러한 경우, 인공지능을 이용해 사람의 사진을 식별할 수 있을 만큼 복원할 수 있지 않을까 생각했다. 이를 위하여 Convolutional auto encoder 기술을 이용하여 모자이크 처리 되거나 심하게 손상된 사람들의 사진을 복원할 수 있는 인공지능을 제작하고자 한다. 

### notebooks

- [텀프로젝트 제안서](./2020103913_term_project_proposal_submission.ipynb)
- [인스타그램에서 데이터 크롤링](./get_data_insta.ipynb)
- [이미지 visualization 및 얼굴 detection](./visualize_pics.ipynb)

### 추가설명

#### auto encoder에 대하여

<img src="https://www.compthree.com/images/blog/ae/ae.png" width=500 height=500>


auto encoder는 기본적으로 input 값과 output 값이 동일한 뉴럴 네트워크를 의미한다. 인풋 데이터를 압축시키고 그것을 복원시키는 네트워크를 학습한다. 
위의 사진은 가장 기본적인 auto encoder의 형태를 보여주고 있다. Input data를 받아 latent space만큼 데이터를 압축시키는 encoder와, 압축된 데이터를 다시 원본과 비슷하게 복원시키는 decoder로 이루어져 있는 것을 볼 수 있다. 보통 input data에서 feature를 추출하는데 사용하며, DAE(Denoising Auto Encoder) 등의 여러 변형된 auto encoder가 존재한다. 그 중에서 이미지에 적용되는 convolutional auto encoder를 사용할 것이다. 

<img src="https://www.researchgate.net/profile/Xifeng-Guo/publication/320658590/figure/fig1/AS:614154637418504@1523437284408/The-structure-of-proposed-Convolutional-AutoEncoders-CAE-for-MNIST-In-the-middle-there.png">

위 사진은 convolutional auto encoder의 기본적인 형태를 보여준다. 유명한 MNIST 데이터를 이용한 예시이다. 보이는 것처럼 기본적인 auto encoder와 전체적인 모양새는 같지만, 이미지에 특화된 CNN 네트워크를 사용한 형태이다. 이 convolutional auto encoder를 통해 이미지를 압축하고, 그 압축된 이미지를 다시 복원하는 decoder를 훈련할 수 있다. 이 decoder를 이용하면 화질이 저하된 이미지를 다시 복원시킬 수 있을 것이다.
추가로, denoising auto encoder의 원리를 이에 적용하여, 학습 과정에서 이미지에 랜덤으로 blur를 부여하고 이를 다시 복원하는 방식으로 모자이크 처리되어있거나 크게 손상된 이미지 역시 원본과 비슷하게 복원할 수 있다. 

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

#### 참고 코드
1. [De-blurring images using convolutional auto encoder](https://levelup.gitconnected.com/de-blurring-images-using-convolutional-neural-networks-with-code-51d3f8d7b1d7)
2. [Image Deblurring Auto Encoder Network](https://github.com/AryanSethi/Deblurring_autoencoder)
3. [파이썬으로 인스타그램 이미지 크롤링하여 다운로드하기](https://dahaha.tistory.com/76)
4. [DeblurGAN](https://github.com/KupynOrest/DeblurGAN)

#### 관련 논문
1. [Image Restoration using Autoencoding Priors](https://www.google.com/url?sa=t&source=web&rct=j&url=https://arxiv.org/pdf/1703.09964&ved=2ahUKEwi0tIGoh5bwAhVVL6YKHW4mATgQFjAAegQIBBAC&usg=AOvVaw0TPO4x4mcIveMqJFVMLPr9)
2. [DeblurGAN: Blind Motion Deblurring Using Conditional Adversarial Networks](https://arxiv.org/abs/1711.07064)