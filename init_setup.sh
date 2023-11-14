echo [$(date)]: "START"
echo [$(date)]: "Creating conda environment for python 3.8"
conda create --prefix ./env python=3.8 -y
echo [$(date)]:"activating conda environment"
source activate ./env
echo [$(date)]:"installing project dependencies"
pip install -r requirements.txt
echo [$(date)]:"END"