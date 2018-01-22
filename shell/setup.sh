#!/bin/sh

abs_path_to_mdl=`find \`pwd\` -name "mdl"`

chmod a+x mdl

cp ./mdl /usr/local/bin/
