# Animal-Presumed
"Animal-Presumed"は転移学習を用いて作成した動物の画像認識アプリです。

# DEMO

作成中

# Features
動物の画像を入力するとその動物の名前を当てることができます。
モデルは転移学習を用いて作成しているので自分で新たな画像をトレーニングする際も少ない枚数で済みます。

＊現時点で推定できるのはライオンとトラの2種類です。

# Requirement

* Python 3.7.6
* Django 3.0.3
* tensorflow 2.0.0
* flickrapi 2.4.0
* Pillow 7.0.0
* numpy 1.18.1
* scikit-learn 0.22.1

```bash
conda create -n djangoai pip python=3.7 Anaconda
activate djangoai
```
# Install

* pip install django
* pip install tensorflow ＊Pythonのバージョンは3.5~3.7にする。
* pip install flickrapi
* pip install PIL
* pip install numpy
* pip install scikit-learn

# Note

ファイル容量が大きいため

* imagefiles_224.npy
* vgg16_transfer.h5

は除いていますがアプリを動かす際は必須のファイルです。

# Usage

```bash
git clone https://github.com/ryomakawata/image-app
cd examples
python manage.py runserver
```
# Author

* ryoma kawata
