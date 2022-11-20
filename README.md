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

## Draw the training graph
```shell
python tools/analysis_tools/analyze_logs.py plot_curve work_dirs/xxx directory/xxx.log.json --keys train_accuracy accuracy_top-1 --title "xxx" --legend train val --out xxx.jpg 

# Example
python tools/analysis_tools/analyze_logs.py plot_curve work_dirs/mobilenet_v3_large_b128_cifar100/20221120_045648.log.json --keys train_accuracy accuracy_top-1 --title "Baseline MobileNetV3_Large on CIFAR100" --legend train val --out baseline_cifar100.jpg 
```