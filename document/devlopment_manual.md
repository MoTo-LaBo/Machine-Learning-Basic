# 環境構築
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
### 1. image 一覧表示
    docker images
### 2. container 一覧表示
    docker ps -a
### 3. 使用したい image が up かどうか status 確認
    # up でない場合は下記のコマンド実行
    docker restart < container名 >
### 4. image がなければ Docker image から container を起動
    docker run -v ~/filepath/buildcontext:/work -p <portは個人で指定>:8888 --name < images > < images ID >
### 5. container を止める
    dockre stop < container名・ID >
### 6. container 削除
    docker rm < container名・ID >
### 7. docker image を削除する
    docker rmi <image>

