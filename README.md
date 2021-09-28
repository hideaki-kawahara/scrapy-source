# 説明

このRepositoryは「PythonとScrapyを使ったWebスクレイピング実践編～あのサイトをスクレイピングするまで！～」技術同人誌版、「PythonとScrapyを使ったWebスクレイピング実践編」商業誌版で使用したRepositoryになります。


##  ソースコードについて
本書に記載された内容は、情報の提供のみを目的としています。したがって、Repositoryを用いた開発、製作、運用は、必ずご自身の責任と判断によって行ってください。
これらの情報による開発、製作、運用の結果について、著者はいかなる責任も負いません。


## 第2章「最初のスクレイピング」
第2章「最初のスクレイピング」を実行する手順を下に記載します。

 1. ソースコードをCloneするディレクトリーを作成する。
    * `mkdir -p scrapy-source`
 2. Cloneする。
    * `git clone https://github.com/hideaki-kawahara/scrapy-source.git`
 3. chapter1をcheckoutする。
    * `git checkout chapter1`
 4. 仮想環境を作成する。
    * `python -m venv .venv`
 5. 仮想環境に入る。
    * `source .venv/bin/activate`
 6. ライブラリーをインストールする。
    * `pip install -r requirements.txt`
 7. 該当のディレクトリーに入る。
    * `cd yahoo_news_scrapy`
 8. 実行する。
    * `scrapy crawl yahoo_news`

※実行後に実行キャッシュディレクトリーが作成されるので、他のBrunchをcheckoutしても以前にcheckoutしたchapterのディレクトリーは消えません。気になるようなら削除してください。
```
rm -rf 以前にcheckoutしたディレクトリー
```
