# 第2章「最初のスクレイピング」
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
rm -rf checkoutしたディレクトリー
```
