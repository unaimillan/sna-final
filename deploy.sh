APP_PATH=/pyapp
echo "[INFO] Stopping gunicorn"
kill `cat $APP_PATH/gunicorn.pid`
echo "[INFO] Removing old app"
rm -rf $APP_PATH
echo "[INFO] Coping new one from github"
git clone https://github.com/unaimillan/sna-final.git $APP_PATH
pip3 install gunicorn
cd $APP_PATH
pip3 install -r requirements.txt
echo "[INFO] Firing up gunicorn"
gunicorn -D -p $APP_PATH/gunicorn.pid -b :80 app:app
echo "[INFO] Done, check the website"
