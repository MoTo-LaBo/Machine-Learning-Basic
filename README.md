# Python Machine Learning Basic
- データ処理・機械学習に必要とされる<u>基本的な機能</u>について学ぶ
  - 実習 base で体験し詳しく学ぶ
  - 基本的な API(function/method)の扱い方
  - 自力で programing ができるように・実装できるようにする
### **主な内容**
- data 処理と機械学習に必要となる基本的な機能
  - 「data構造」(配列data)の扱い方
  - 可視化の方法
    - 折れ線グラフ、ヒストグラム、散布図、etc...
- 画像data・音声dataの扱い方
  - file入出力、機械学習の為の前処理など
- 統計処理の基本機能
- dataの入出力
  - file の読み込みと保存(CSV)
  - folder(directory)の内容の一括処理
- scikit-learn
- AI の為の数学
- Kaggle
- 統計学
### <u>scikit-learn, Keras, PyTorch, etc...</u>
- 上記の library を扱うための基礎を固める
- 基盤知識・前提知識を固める事を前提
- 本格的な AI(人工知能)・機械学習の program を自分自身で組むための知識基盤
### **使用するソフトウェア**
- python 3 pyenv (version切り替え)
- Docker を使用した環境構築
  - ANACONDA, Jupyterlab, ubuntu, docker
- Jupyter Lab
- library
  - 数値計算　　Numpy　( data処理の基本機能 )
  - DF　　　　　pandas ( DataFrame )
  - 可視化　　　matplotlib　( 各種のグラフ作成 )
  - 可視化　　　seaborn ( グラフ )
  - 画像処理　　OpenCV　( 画像の入出力と前処理 )
  - 音声data　　wave　( サウンドfileの取り扱い )
  - file入出力　　os, pathlib　( file取り扱い )
## AIの為の数学
  - *線形代数*
    - スカラー・ベクトル・行列・テンソル
  - *微分*
    - 常微分・偏微分・連鎖率
  - *確率・統計*
    - 標準偏差・正規分布・尤度
    - データ傾向・確率としての捉え方
###
## scikit learn basic
> https://scikit-learn.org/stable/index.html
- scikit-learnによる機械学習ライブラリの利用
  - numpy
  - matplotlibによるデータの可視化
    - seaborn
  - pandasによるデータの前処理
  - 基本統計量のプログラミング
### 機械学習
- k-means法
- PCAによる時限削減
- 線形回帰（単回帰分析・重回帰分析）
- SVM（サポート・ベクトル・マシン）
- ランダムフォレストによる分類
## Kaggle
### Titanic - Machine Learning from Disaster
<u>機械学習を使用して、タイタニック号の難破船を生き延びた乗客を予測するモデルを作成</u>
- data science・機械学習・統計
1. Pythonの基本code
2. data分析・機械学習の基本知識
3. Pythonの応用 code
4. Pythonの機械学習
### labrary install & 起動
    # pandas_profiling 表示の為のcommand

    pip install pandas_profiling
    pip install ipywidgets jupyterlab matplotlib
> https://pypi.org/project/pandas-profiling/
> https://ipywidgets.readthedocs.io/en/stable/user_install.html

# 環境構築
### <u>1. docker build する</u>
    docker build -t ai:latest .
- biuld する時の場所は scikit_learn directory にいる事
- .(ドット：カレントディレクトリを指定している)
### <u>2. container を立てる</u>
    docker run -v ~/udemy/Machine_Learning:/work -p 1111:8888 --name ml-env ai
- -v option を付けると、container の file system を Host に mount する事ができる
- -p option : port (ポート) Jupyterlab は web のアプリケーション。ネットワークを介してアクセスするものなので、指定した port の上で動かす必要がある
- 今回は *1111*:8888 という port の上で動くようにしてある default の Jupyter の port の番号
- container の port を Host に繋げてあげないと動かない。なので host 側の localhost.8888 に接続すると container 8888 に届くようになっている
-   -- name で container に名前を付ける事ができる
    -   名前を付けないと container の方で default で変な名前が付けられてしまう
### <u>3. browser に移動 -> Jupyter lab 起動</u>
-  ブラウザで **localhost:8888** アクセス
   -  Firefox, chrome が良い
-  Jupyter lab が表示される
## Docker の基本操作
### コンテナ一覧表示
    docker ps -a
### docker image 一覧表示
    docker images
### docker image から container 起動
    docker run -v ~/udemy/Machine_Learning:/work -p 1111:8888 --name ml-env ai
### コンテナを止める
    docker stop <container>
### コンテナを削除
    docker rm <container>
### コンテナを restart
    docker restart <container>


