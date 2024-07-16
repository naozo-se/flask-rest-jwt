

# マイグレーション(初回のみ)
MGN_PATH=/usr/src/app/api/migrations
if [ ! -d $FILE ]; then
  mkdir $MGN_PATH
  flask db init
fi
# マイグレーション(修正)
flask db migrate
flask db upgrade

# パッケージインストール
python -m pip install --user -r requirements.txt

# サーバー起動
uwsgi --ini uwsgi.ini
