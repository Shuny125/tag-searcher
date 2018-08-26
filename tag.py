# -*- coding: utf-8 -*-

import os
import sys
import fnmatch
from bs4 import BeautifulSoup
from chardet.universaldetector import UniversalDetector

## -------------------------------------
## ファイルリスト作成
## -------------------------------------

def filelist(root):
    ## 現在のディレクトリを再帰的に検索
    for dirpath, dirs, files in os.walk(root):
        for FILENAME in files:
            ## 拡張子「.html」or「.php」のファイルに絞る
            if fnmatch.fnmatch(FILENAME, '*.html') or fnmatch.fnmatch(FILENAME, '*.php'):
                ## 対象ファイルパス
                html = os.path.join(dirpath, FILENAME)

                ## 対象ファイルの文字コード判定
                detector = UniversalDetector()
                with open(html, mode='rb') as f:
                    for binary in f:
                        detector.feed(binary)
                        if detector.done:
                            break
                detector.close()

                ## ルートパスは不要なため置換
                PATH = html.replace(root,'')
                DIRECTORY = dirpath.replace(root,'')+'/'

                ## html情報を取得
                try:
                    soup = BeautifulSoup(open(html, encoding=detector.result['encoding']), 'lxml')
                except:
                    print(PATH)
                    print('エラー')
                    sys.exit()

                ## titleタグを取得
                TITLE = soup.find('title')
                if TITLE != None:
                    ## canonicalを取得
                    CANONICAL = soup.find('link',attrs={'rel':'canonical'})
                    if CANONICAL == None:
                        print(PATH)

## 実行（カレントディレクトリ）
if __name__ == '__main__':
    filelist(os.getcwd())
