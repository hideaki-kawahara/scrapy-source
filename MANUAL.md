# 第4章「データベースを使用する」
第4章「データベースを使用する」を実行する手順を下に記載します。

 1. ソースコードをCloneするディレクトリーを作成する。
     * `mkdir -p scrapy-source`
 2. Cloneする。
     * `git clone https://github.com/hideaki-kawahara/scrapy-source.git`
 3. chapter3をcheckoutする。
     * `git checkout chapter3`
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
     * `cd qiita_trend_scrapy`
 11. 実行する。
     * `scrapy crawl qiita_trend_scrapy`

※実行後に実行キャッシュディレクトリーが作成されるので、他のBrunchをcheckoutしても以前にcheckoutしたchapterのディレクトリーは消えません。気になるようなら削除してください。
```
rm -rf checkoutしたディレクトリー
```
