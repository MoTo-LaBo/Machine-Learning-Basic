# Python Machine Learning Basic
- データ処理・機械学習に必要とされる<u>基本的な機能</u>について学ぶ
  - 実習 base で体験し詳しく学ぶ
  - 基本的な API(function/method)の扱い方
  - 自力で programing ができるように・実装できるようにする
  - フォルダー
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
### <u>sciket-learn, Keras, PyTorch, etc...</u>
- 上記の library を扱うための基礎を固める
- 基盤知識・前提知識を固める事を前提
- 本格的な AI(人工知能)・機械学習の program を自分自身で組むための知識基盤
### **使用するソフトウェア**
- python 3 pyenv (version切り替え)
  - venv (virtual env:仮想環境)
- Jupyter Lab
- library
  - 数値計算　　Numpy　(data処理の基本機能)
  - 可視化　　　matplotlib　(各種のグラフ作成)
  - 画像処理　　OpenCV　(画像の入出力と前処理)
  - 音声data　　wave　(サウンドfileの取り扱い)
  - file入出力　　os, pathlib　(file取り扱い)
##  環境構築
### <u>1. Dockerfile build で docker image を作成</u>
    docker build .<directory>
- .(ドット)はカレントdirectory ※ 基本は Dockerfile のある directory に移動して docker build を使用するので、$ `docker build .< directory >` の形で覚えておく
### <u>2. Dockerfile build -t を付けると name も一緒に付けることができる</u>
    docker build -t <name> .<directory>
### <u>3. image 確認</u>
    docker images
### <u>4. docker images で name が < none > だと使いにくい</u>
    docker build -t < name >:latest .
- . ( ドット ) はカレントdirectory で Dockerfile の場所を指定する
- latest :
- docker build の時に -t を付ける(tag): 名前をつけて build する
- 名前をつけないと none で表示される
  - **dangling : ダングリングイメージ(ぶら下がっているの意)**
### <u>5. 1, 2, 3 を踏まえて docker build する</u>
    docker build -t ai:latest .
- biuld する時の場所は scikit_learn directory にいる事
- .(ドット：カレントディレクトリを指定している)
### <u>6. container を立てる</u>
    docker run -v ~/udemy/Machine_Learning:/work -p 1111:8888 --name ml-env ai
- -v option を付けると、container の file system を Host に mount する事ができる
- -p option : port (ポート) Jupyterlab は web のアプリケーション。ネットワークを介してアクセスするものなので、指定した port の上で動かす必要がある
- 今回は *1111*:8888 という port の上で動くようにしてある default の Jupyter の port の番号
- container の port を Host に繋げてあげないと動かない。なので host 側の localhost.8888 に接続すると container 8888 に届くようになっている
-   -- name で container に名前を付ける事ができる
    -   名前を付けないと container の方で default で変な名前が付けられてしまう
### <u>7. browser に移動 -> Jupyter lab 起動</u>
-  ブラウザで **localhost:8888** アクセス
   -  Firefox, chrome が良い
-  Jupyter lab が表示される
-  Docker を使用する事で簡単に環境構築ができる
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


