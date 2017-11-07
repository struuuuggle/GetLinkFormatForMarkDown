#!/bin/sh

# スクリプトファイルを生成
touch grl

# 'getLinkFormat.py'のフルパス
abspath=`find \`pwd\` -name "getLinkFormat.py"`

# grlに追記
echo "#!/bin/sh\n\n# set command from setup.sh\npython $abspath" > grl

# スクリプトに実行権限を与える
chmod a+x grl

# コマンドサーチパスに保存
sudo cp grl /usr/local/bin/
