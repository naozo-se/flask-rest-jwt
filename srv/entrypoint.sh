# パッケージインストール
python -m pip install --user -r requirements.txt

# マイグレーション(初回のみ)
MGN_PATH=/srv/migrations
if [ ! -d $MGN_PATH ]; then
  mkdir $MGN_PATH
  flask db init
fi
# マイグレーション(修正)
flask db migrate
flask db upgrade

# サーバー起動
uwsgi --ini uwsgi.ini
