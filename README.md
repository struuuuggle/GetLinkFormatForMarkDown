# grl 

My own command grl enables you to copy a link format for Markdown.

## 環境
- maxOS Sierra version 10.12.6
- Python 3.6.1

## デモ

![https://gyazo.com/755fb3175e4e4d54511c2e76c2c35c4b](https://gyazo.com/755fb3175e4e4d54511c2e76c2c35c4b.gif)

## 仕様
URLを入力すると、Markdownに最適な形式で、webページタイトルとURLを出力します。出力結果はコンソールに表示すると同時に、クリップボードにもコピーされます。

## 準備

- 以下のコマンドを打ってください。

```
$ git clone https://github.com/struuuuggle/GetLinkFormatForMarkDown.git
$ cd ./GetLinkFormatForMarkDown
$ sh setup.sh
// パスワードの入力が求められます
```
 
- これで準備は終了です。

## 使い方

```
$ grl
Type URL(or exit)
> <input URL>
```