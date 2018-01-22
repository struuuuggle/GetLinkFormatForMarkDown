# -*- coding: utf-8 -*-

from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import pyperclip

# Regular expression to match URLs
regex = re.compile('(?:(?:https?|ftp|file)://|www\.|ftp\.)[-A-Z0-9+&@#/%=~_|$?!:,.]*[A-Z0-9+&@#/%=~_|$]', re.IGNORECASE)


# 入力がURL形式であることをチェック
def isURL(url):
    return re.match(regex, url) != None


# Get link format for Markdown
def getLinkFormat():
    # アクセスするURL
    while True:
        url = input('>')

        if url == 'q':
            break

        elif isURL(url):
            # URLにアクセスする htmlが帰ってくる
            html = urlopen(url)

            # htmlをBeautifulSoupで扱う
            soup = BeautifulSoup(html, 'html.parser')

            # タイトルとURLをmarkdown用にフォーマット
            result = '[' + soup.title.string + ']' + '(' + url + ')'

            #文字列をクリップボードにコピー
            pyperclip.copy(result)

            #フオーマットした文字列を出力
            print(result)

        else:
            print('invalid syntax')
            continue


def main():
    print('Type URL(or \'q\' to exit)')
    getLinkFormat()


if __name__ == '__main__':
    main()
