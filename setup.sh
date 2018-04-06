#!/bin/bash
################################################################################
## Configure the system to use all config in this repos
################################################################################

CWD=$(pwd)
DIRECTORIES=()

# Make sure our configuration directories exist
check_dirs() 
{
    for dir in ${DIRECTORIES[*]}
    do
        if [ ! -d "$dir" ]; then
            mkdir -p $dir
        fi
    done
}

# Setup the way-cooler environment
setup_way_cooler() 
{
    DIRECTORIES+=("$HOME/.config/dunst")
    DIRECTORIES+=("$HOME/way-cooler")
    DIRECTORIES+=("$HOME/.local/bin")
    
    echo "installing dunstrc"
    ln -s $CWD/way-cooler-env/dunstrc $HOME/.config/dunst/dunstrc

    echo "installing init.lua"
    ln -s $CWD/way-cooler-env/init.lua $HOME/way-cooler/init.lua

    echo "installing lemon bar scripts"
    ln -s $CWD/way-cooler-env/lemonbar/start_lemonbar.sh $HOME/.local/bin/start_lemonbar.sh
    ln -s $CWD/way-cooler-env/lemonbar/lemonbar_data.sh $HOME/.local/bin/lemonbar_data.sh
    ln -s $CWD/way-cooler-env/lemonbar/status.py $HOME/.local/bin/status.py
}

main()
{
    check_dirs
    setup_way_cooler
}
main