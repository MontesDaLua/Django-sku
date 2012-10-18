#!/bin/sh
. $HOME/bin/DjangoTstEnv.sh 
cd $TSTSITE
cd $APP
sh update_script.sh 
cd ..
python manage.py test $APP
