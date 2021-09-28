# 説明
このRepositoryは下の書籍で使用する物です。
1. 技術同人誌版「PythonとScrapyを使ったWebスクレイピング実践編～あのサイトをスクレイピングするまで！～」
2. 商業誌版「PythonとScrapyを使ったWebスクレイピング」

技術同人誌版は第2章～第6章、商業誌版は第2章～第9章で使用します。

## 書籍リンク
技術同人誌版
1. BOOTH [https://bright-system.booth.pm/items/3056624](https://bright-system.booth.pm/items/3056624)
2. 技術書典 [https://techbookfest.org/product/6080956333031424?productVariantID=5063798069133312](https://techbookfest.org/product/6080956333031424?productVariantID=5063798069133312)

商業誌版
1. Amazon印刷版 [https://www.amazon.co.jp/dp/484437981X/](https://www.amazon.co.jp/dp/484437981X/)
2. Amazon電子書籍版 [https://www.amazon.co.jp/dp/B09GVNZX54/](https://www.amazon.co.jp/dp/B09GVNZX54/)
3. 楽天 [https://books.rakuten.co.jp/rk/03dbcfb9748f350b8f7f9ed56ebeb739/](https://books.rakuten.co.jp/rk/03dbcfb9748f350b8f7f9ed56ebeb739/)
4. 紀伊國屋書店 [https://www.kinokuniya.co.jp/f/dsg-08-EK-1059652](https://www.kinokuniya.co.jp/f/dsg-08-EK-1059652)
5. Google [https://play.google.com/store/books/details/?id=DTBEEAAAQBAJ](https://play.google.com/store/books/details/?id=DTBEEAAAQBAJ)
6. Reader Store [https://ebookstore.sony.jp/item/LT000153910001339409/](https://ebookstore.sony.jp/item/LT000153910001339409/)
7. BOOK TECH [https://book-tech.com/books/d018e9c0-c9b9-4106-bda0-12dfcfcd5265](https://book-tech.com/books/d018e9c0-c9b9-4106-bda0-12dfcfcd5265)

##  ソースコードについて
本書に記載された内容は、情報の提供のみを目的としています。したがって、Repositoryを用いた開発、製作、運用は、必ずご自身の責任と判断によって行ってください。
これらの情報による開発、製作、運用の結果について、著者はいかなる責任も負いません。

Licenceについては[Licenceファイル](/LICENSE)を確認してください。

## 各章のサンプルコードの取得
各章のサンプルコードはcheckoutすると取得できます。


### 第2章「最初のスクレイピング」
```
git checkout chapter1
```
手順は[マニュアル](/blob/chapter1/MANUAL.md)を確認してください。

### 第3章「POSTメソッドがあるサイトでスクレイピング」
```
git checkout chapter2
```
手順は[マニュアル](/blob/chapter2/MANUAL.md)を確認してください。

### 第4章「データベースを使用する」
```
git checkout chapter3
```
手順は[マニュアル](/blob/chapter3/MANUAL.md)を確認してください。

### 第5章「動的画面のスクレイピング」
```
git checkout chapter4
```
手順は[マニュアル](/blob/chapter4/MANUAL.md)を確認してください。

### 第6章「Lazy loading画面のスクレイピング」
```
git checkout chapter5
```
手順は[マニュアル](/blob/chapter5/MANUAL.md)を確認してください。

### 第7章「Dropboxと連携する」
```
git checkout chapter6
```
手順は[マニュアル](/blob/chapter6/MANUAL.md)を確認してください。

### 第8章「Cloudサービスを使ってスクレイピング」
```
git checkout chapter7
```
手順は[マニュアル](/blob/chapter7/MANUAL.md)を確認してください。

### 第9章「cloudサービスで定期的実行をする」
```
git checkout chapter8
```
手順は[マニュアル](/blob/chapter8/MANUAL.md)を確認してください。

## 実行後の注意点
実行後に実行キャッシュディレクトリーが作成されるので、他のBrunchをcheckoutしても以前にcheckoutしたchapterのディレクトリーは消えません。
気になるようなら下のコマンドで削除してください。

```
rm -rf checkoutしたディレクトリー
```
