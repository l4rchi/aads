mkdir my_folder
cd my_folder
git clone https://github.com/askras/aads.git
cd aads
python -m venv venv
. ./venv/bin/activate
python -m pip install pip --upgrade
python -m pip install -r requirements.txt

jupyter notebook


git status
git add labs/lab01/lab01_XX/
