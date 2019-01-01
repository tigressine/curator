# A handful of scripts to automate aspects of this repository.
# Part of Curator by Tiger Sachse.

EXE_NAME="curate"

# Build the project into a mobile, executable zip file.
build_project() {
    cd source
    zip -r $EXE_NAME *
    mv $EXE_NAME.zip ..
    cd ..

    echo '#!/usr/bin/env python3' | cat - $EXE_NAME.zip > $EXE_NAME
    chmod +x $EXE_NAME

    rm $EXE_NAME.zip
}

build_project
