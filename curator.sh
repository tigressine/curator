# A handful of scripts to automate aspects of this repository.
# Part of Curator by Tiger Sachse.

#BIN_DIR="bin"
EXE_NAME="curate"
SOURCE_DIR="source"

# Build the project into a mobile, executable zip file.
build_project() {
    rm -rf $EXE_NAME

    cd $SOURCE_DIR
    zip -r $EXE_NAME *
    mv $EXE_NAME.zip ..
    cd ..

    echo '#!/usr/bin/env python3' | cat - $EXE_NAME.zip > $EXE_NAME
    chmod +x $EXE_NAME

    rm $EXE_NAME.zip
}

# Entry point of the script.
case "$1" in
    "--build")
        build_project
        ;;
esac

#python3 -m compileall $SOURCE_DIR
#rm -r -f $BIN_DIR
#mkdir $BIN_DIR
#for FILE in $SOURCE_DIR/__pycache__/*; do
#    FILENAME="${fullfile##*/}"
#    mv $FILE ../../$BIN_DIR/$FILENAME.py
#done
#rm -r $SOURCE_DIR/__pycache__
#build_project && ./$EXE_NAME "$@"
