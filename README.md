# 説明

このRepositoryは「PythonとScrapyを使ったWebスクレイピング実践編～あのサイトをスクレイピングするまで！～」技術同人誌版、「PythonとScrapyを使ったWebスクレイピング実践編」商業誌版で使用したRepositoryになります。


##  ソースコードについて
本書に記載された内容は、情報の提供のみを目的としています。したがって、Repositoryを用いた開発、製作、運用は、必ずご自身の責任と判断によって行ってください。
これらの情報による開発、製作、運用の結果について、著者はいかなる責任も負いません。


## 第6章「Lazy loading画面のスクレイピング」
第6章「Lazy loading画面のスクレイピング」を実行する手順を下に記載します。

 1. ソースコードをCloneするディレクトリーを作成する。
     * `mkdir -p scrapy-source`
 2. Cloneする。
     * `git clone https://github.com/hideaki-kawahara/scrapy-source.git`
 3. chapter5をcheckoutする。
     * `git checkout chapter5`
 4. 仮想環境を作成する。
     * `python -m venv .venv`
 5. 仮想環境に入る。
     * `source .venv/bin/activate`
 6. ライブラリーをインストールする。
     * `pip install -r requirements.txt`
 7. dockerのディレクトリーに入る。
     * `cd docker`
 8. dockerを起動する。
     * `docker-compose up -d`
 9. 元のディレクトリーに入る。
     * `cd ..`
 10. 該当のディレクトリーに入る。
     * `cd techbookfest_scrapy`
 11. 実行する。
     * `scrapy crawl techbookfest_url`

※実行後に実行キャッシュディレクトリーが作成されるので、他のBrunchをcheckoutしても以前にcheckoutしたchapterのディレクトリーは消えません。気になるようなら削除してください。
```
rm -rf 以前にcheckoutしたディレクトリー
```

## URLの変更
技術書典のサイトは会期ごとにURLが変化します。書籍の時点では技術書典10をベースに執筆しました。


35行目にある`start_url`を変更することで他のURLにも対応できます。

```
start_url = 'https://techbookfest.org/event/tbf10/market/newbook'
```

なお、技術書典11では下のURLが有効になっています。

 * 技術書典11オンラインマーケット
    * https://techbookfest.org/event/tbf11/market
 * 技術書典11オンラインマーケット　新刊
    * https://techbookfest.org/event/tbf11/market/newbook
 * 技術書典11オンラインマーケット　物理本
    * https://techbookfest.org/event/tbf11/market/paperbook
 * 技術書典11オンラインマーケット　出展一覧
    * https://techbookfest.org/event/tbf11/offline

