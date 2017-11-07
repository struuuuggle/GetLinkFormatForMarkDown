#!/bin/sh

# スクリプトに実行権限を与える
chmod a+x grl

# 'GetTitleAndUrl.py'のフルパス
abspath=`find \`pwd\` -name "GetTitleAndUrl.py"`

# grlに追記
echo "#!/bin/sh\n\n# set command from setup.sh\npython $abspath" > grl

# コマンドサーチパスに保存
sudo cp grl /usr/local/bin/
