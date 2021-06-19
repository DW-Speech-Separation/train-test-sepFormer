# train-test-sepFormer
pip freeze > requirements.txt

# Steps

1. git clone https://github.com/DW-Speech-Separation/train-test-sepFormer.git
2. cd train-test-sepFormer
3. sh requirements.sh (Esto instala las dependencias usando pip3, si usted tiene pip cambiar pip3 por pip en el archivo requirements.sh)
4. python3 download_resources.py (Puede usar python solamente)
5. python3 train.py hparams/sepformer.yaml (Puede usar python solamente)

