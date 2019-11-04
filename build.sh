source .venv/bin/activate

export FLASK_APP=main.py
export FLASK_ENV=development
echo "main.py exported..."

flask db init
flask db migrate
flask db upgrade

echo "db created write this command: flask run "
