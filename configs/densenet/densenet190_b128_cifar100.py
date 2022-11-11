_base_ = [
    '../_base_/models/densenet190_cifar100.py',
    '../_base_/datasets/cifar100_bs128.py',
    '../_base_/schedules/cifar100_bs128.py',
    '../_base_/default_runtime.py'
]