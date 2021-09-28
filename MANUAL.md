## 第3章「POSTメソッドがあるサイトでスクレイピング」
第3章「POSTメソッドがあるサイトでスクレイピング」を実行する手順を下に記載します。

 1. ソースコードをCloneするディレクトリーを作成する。
    * `mkdir -p scrapy-source`
 2. Cloneする。
    * `git clone https://github.com/hideaki-kawahara/scrapy-source.git`
 3. chapter2をcheckoutする。
    * `git checkout chapter2`
 4. 仮想環境を作成する。
    * `python -m venv .venv`
 5. 仮想環境に入る。
    * `source .venv/bin/activate`
 6. ライブラリーをインストールする。
    * `pip install -r requirements.txt`
 7. 該当のディレクトリーに入る。
    * `cd mlit_scrapy`
 8. 実行する。
    * `scrapy crawl etsuran_mlit`

※実行後に実行キャッシュディレクトリーが作成されるので、他のBrunchをcheckoutしても以前にcheckoutしたchapterのディレクトリーは消えません。気になるようなら削除してください。
```
rm -rf checkoutしたディレクトリー
```
