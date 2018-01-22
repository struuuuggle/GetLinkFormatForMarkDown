#!/bin/sh

# 実行時にコマンドラン引数の数が1でなければ終了
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>" 1>&2
    exit 1
fi

# コマンドライン引数から受け取ったURL
url=$1

# 該当webページのタイトル
title=`curl -s $url | grep '\<title\>.*<.title>$' | tr -d '(*<title>)(</title>*)'`

# 出力
result="[$title]($url)"

# resultの出力が成功したら、クリップボードにコピー
echo $result && echo $result | pbcopy
