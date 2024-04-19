brew install pyenv -q
pyenv install -s 3.10.1
pyenv local 3.10.1
pip install -r -q requirements.txt

python manage.py makemigrations marketplace
python manage.py migrate
echo "Import canonical.json data: $1"
python manage.py loadinitialdata "$1"
python manage.py runserver
