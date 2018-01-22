#!/bin/sh

# 'getLinkFormat.py'のフルパス
abspath=`find \`pwd\` -name "getLinkFormat.py"`

# スクリプトファイルに追記
echo "#!/bin/sh\n\n# Set command from setup.sh\npython $abspath" > mdl

# スクリプトファイルに実行権限を与える
chmod a+x mdl

# コマンドサーチパスに保存
sudo cp mdl /usr/local/bin/
