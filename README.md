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
  - 数値計算　　Sicpy　( 数値計算 )
  - 代数計算　　Sympy　( 代数計算 )
  - DF　　　　　pandas ( DataFrame )
  - 可視化　　　matplotlib　( 各種のグラフ作成 )
  - 可視化　　　seaborn ( グラフ )
  - 画像処理　　OpenCV　( 画像の入出力と前処理 )
  - 音声data　　wave　( サウンドfileの取り扱い )
  - file入出力　　os, pathlib　( file取り扱い )
## 機械学習
  - *線形代数*
    - スカラー・ベクトル・行列・テンソル
  - *微分*
    - 常微分・偏微分・連鎖率
  - *確率・統計*
    - 標準偏差・正規分布・尤度
    - データ傾向・確率としての捉え方
  - *単回帰分析*
  - *重回帰分析*
### labrary install (docker + pip)
    # variableinspector
    pip install ipywidgets

    pip install lckr-jupyterlab-variableinspector

    # glaph 日本語対応
    pip install japanize-matplotlib
- *Jupyter Labと拡張機能 install・有効化*
  - 「jupyterlab_variableinspector」( 変数エクスプローラとなる機能)
> https://github.com/lckr/jupyterlab-variableInspector

> https://insilico-notebook.com/jupyter-lab-setting/#

> https://pypi.org/project/japanize-matplotlib/
## 線形代数
1. **連立一次方程式**
   - *問題の定式化，Gauss-Jordanの消去法，幾何学的解釈*

2. **ベクトルと行列**
   - *ベクトルとそのPythonによる取扱い，行列とそのPythonによる取扱い，行列の積*

3. **数学の基礎**
   - *集合論，論理，写像，二項演算，群論*

4. **ベクトル空間**
   - *基底，部分空間，線形写像とその行列表現*

5. **解が一意的に存在する連立方程式の現代的解法**
   - *Gaussの消去法，LU分解，PA_LU分解*

6. **解が無限に存在する連立方程式の現代的解法**

   - *階段行列とLU分解，線形写像の核，一般行列のPA_LDU分解，Pythonによる解法*

7. **内積**
   - *ユークリッド空間，ピタゴラスの定理と直交性，内積と転置行列，射影，ユニタリ空間，グラム・シュミットの正規直交化法*

8. **解が存在しない連立方程式の近似解法**
   - *最小2乗法と射影，回帰分析*

9. **固有値と固有ベクトル**
   - *線形変換とベクトル場，固有値問題の解法，複素共役と随伴行列，エルミート行列のスペクトル分解*

10. **行列の対角化**
    - *相似と対角化，正規行列，フィボナッチ数列，マルコフ過程，主成分分析*
## Data analysis
- <u>データ分析演習（実際の研究開発で使いそうなファイルを用いた演習）</u>

  - Excelの実験データを読み込み、回帰直線の算出・Graph作成

  - スペクトルのフィッティングや数値積分

  - センサーなどが出力するtxtファイルからのデータの抽出、データ分析

  - 実験データとSIMデータの比較。SIMデータの決定係数算出
### 3D (３次元plot)
> https://github.com/matplotlib/ipympl
### 1. pip install
    pip install ipympl
### 2 jupyter
    %matplotlib widget
- 先頭行に Jupyter magic command を使用するこで Interactive な描画ができる
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


