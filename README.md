# Animal-Presumed
"Animal-Presumed"は転移学習を用いて作成した動物の画像認識アプリです。

# DEMO


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

# Usage

DEMOの実行方法など、"hoge"の基本的な使い方を説明する

```bash
git clone https://github.com/ryomakawata/firstweb
cd examples
python manage.py runserver
```
# Author

作成情報を列挙する

* ryoma kawata

# License

