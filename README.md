# train-test-sepFormer
pip freeze > requirements.txt


# 1. Instalar dependencias
- pip install -r requirements.txt

Nota: Se tiene que tener torch instalado.
# 2. Descargar data
python download_resources.py

# 3.Train
- python train.py hparams/sepformer.yaml




1. git clone https://github.com/DW-Speech-Separation/train-test-sepFormer.git
2. cd train-test-sepFormer
3. sh requirements.sh
4. python3 download_resources.py
5. python3 train.py hparams/sepformer.yaml
