# mmdl

## Environment setup
```shell
module load anaconda # Server Only
conda create -n mmdl python=3.8
conda activate mmdl
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia

pip install -U openmim
mim install mmcv-full

git clone https://github.com/open-mmlab/mmclassification.git
cd mmclassification
pip install -v -e .
pip install tensorboard
```

## Run training
### Local
```shell
python tools/train.py configs/mobilenet_v3/mobilenet_v3_small_b128_cifar10.py
```

### On Server
```shell
sbatch tools/server_train.sh configs/mobilenet_v3/mobilenet_v3_small_b128_cifar10.py
```