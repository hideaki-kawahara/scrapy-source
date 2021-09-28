# 第8章「Cloud環境を使ってスクレイピング」
第8章「Cloud環境を使ってスクレイピング」を実行する手順を下に記載します。


 1. ソースコードをCloneするディレクトリーを作成する。
     * `mkdir -p scrapy-source`
 2. Cloneする。
     * `git clone https://github.com/hideaki-kawahara/scrapy-source.git`
 3. chapter6をcheckoutする。
     * `git checkout chapter6`
 4. 仮想環境を作成する。
     * `python -m venv .venv`
 5. 仮想環境に入る。
     * `source .venv/bin/activate`
 6. ライブラリーをインストールする。
     * `pip install -r requirements.txt`
 7. 該当のディレクトリーに入る。
     * `cd itmedia_news_scrapy`
 8. 実行する。
     * `scrapy crawl itmedia_news`
 9. https://www.zyte.com/ にアカウントを作成する。
 10. https://www.zyte.com/ でログインする。
 11. deployする。
 12. サイト上で実行する。
 13. Exportしてダウンロードする。

※実行後に実行キャッシュディレクトリーが作成されるので、他のBrunchをcheckoutしても以前にcheckoutしたchapterのディレクトリーは消えません。気になるようなら削除してください。
```
rm -rf checkoutしたディレクトリー
```

