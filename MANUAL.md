# 第7章「Dropboxと連携する」
第7章「Dropboxと連携する」を実行する手順を下に記載します。

 1. Dropboxのアカウントを作成する。
 2. Dropbox API Tokenを作成する。
 3. ソースコードをCloneするディレクトリーを作成する。
     * `mkdir -p scrapy-source`
 4. Cloneする。
     * `git clone https://github.com/hideaki-kawahara/scrapy-source.git`
 5. chapter1をcheckoutする。
     * `git checkout chapter6`
 6. 仮想環境を作成する。
     * `python -m venv .venv`
 7. 仮想環境に入る。
     * `source .venv/bin/activate`
 8. ライブラリーをインストールする。
     * `pip install -r requirements.txt`
 9. 該当のディレクトリーに入る。
     * `cd hatena_bookmarks_scrapy`
 10. 実行する。
     * `scrapy crawl hatena_bookmarks`
 11. Dropboxで確認する。


※実行後に実行キャッシュディレクトリーが作成されるので、他のBrunchをcheckoutしても以前にcheckoutしたchapterのディレクトリーは消えません。気になるようなら削除してください。
```
rm -rf checkoutしたディレクトリー
```
