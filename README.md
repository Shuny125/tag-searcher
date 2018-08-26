# tag-searcher
カレントディレクトリのタグを検索する機能です。  
公開しているものは以下の内容となっています。

- canonical タグの無いページ
- インクルードファイルは除く、HTML/PHPファイルが対象

の洗い出し。  
※tag.py ファイルを編集することで別のタグを検索することも可能

## Dependency
動作確認済み環境  
macOS Sierra 10.13.4  
Python 3.5.0  

## Setup
### Python
https://www.python.org/downloads/windows/  
3系の最新バージョンをインストール  
→「Download Windows x86-64 executable installer」

ターミナルを開いて、以下のコマンドを実行。
```
$ python —V
```
バージョンが表示されたらOK。

### pip
ターミナルを開いて、以下のコマンドを実行。
```
$ easy_insatll pip
```

### Python ライブラリインストール
ターミナルを開いて「requirements.txt」と同じディレクトリにいる状態で、以下のコマンドを実行。
```
$ pip install -r requirements.txt
```

## Usage
### tag.py
検索したいファイルのルートディレクトリに配置してください。  

### 実行
ターミナルを開いて、以下のコマンドを実行。
```
$ python tag.py
```

## Licence
This software is released under the MIT License, see LICENSE.

## Author
[Shuny125](https://github.com/Shuny125)
