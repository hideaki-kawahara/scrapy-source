# 第9章「cloudサービスで定期的実行をする」
第9章「cloudサービスで定期的実行をする」を実行する手順を下に記載します。


 1. ソースコードをCloneするディレクトリーを作成する。
     * `mkdir -p scrapy-source`
 2. Cloneする。
     * `git clone https://github.com/hideaki-kawahara/scrapy-source.git`
 3. chapter3をcheckoutする。
     * `git checkout chapter8`
 4. 仮想環境を作成する。
     * `python -m venv .venv`
 5. 仮想環境に入る。
     * `source .venv/bin/activate`
 6. ライブラリーをインストールする。
     * `pip install -r requirements.txt`
 7. Dockerディレクトリーに入る。
     * `cd docker`
 8. Dockerを起動する。
     * `docker-compose up -d`
 9. 該当のディレクトリーに入る。
     * `cd ../kurashiru_side_dishs_scrapy`
 10. 実行する。
     * `scrapy crawl kurashiru_side_dishs`
 11. https://jp.heroku.com/home にアカウントを作成する。
 12. https://jp.heroku.com/home でログインする。
 13. deployする。
 14. データベースを作成する。
 15. サイト上で実行する。
 16. データベースにアクセスして、データをダウンロードする。


※実行後に実行キャッシュディレクトリーが作成されるので、他のBrunchをcheckoutしても以前にcheckoutしたchapterのディレクトリーは消えません。気になるようなら削除してください。
```
rm -rf checkoutしたディレクトリー
```

