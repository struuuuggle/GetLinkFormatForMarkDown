# coding: UTF-8

import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyperclip


def isMatchUrl(url):
    pattern = r"http(s)?://([\w-]+\.)+[\w-]+(/[\w- ./?%&=]*)?"
    matchObj = re.match(pattern, url)

    if matchObj:
        return True
    else:
        return False

def getTitleAndUrl():
    # アクセスするURL
    while True:
        url = input('>')

        #if isMatchUrl(url) == True:
        if url == 'exit':
            break

        # TODO: isMatchUrl関数を使ってエラーハンドリングを行う

        else:
            # URLにアクセスする htmlが帰ってくる
            html = urlopen(url)

            # htmlをBeautifulSoupで扱う
            soup = BeautifulSoup(html, "html.parser")

            # タイトルとURLをmarkdown用にフォーマット
            str1 = '[' + soup.title.string + ']' + '(' + url + ')'

            #文字列をクリップボードにコピー
            pyperclip.copy(str1)

            #フオーマットした文字列を出力
            print(str1)


def main():
    print('Type URL(or exit)')
    getTitleAndUrl()


if __name__ == '__main__':
    main()
