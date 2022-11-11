_base_ = [
    '../_base_/models/densenet190_cifar10.py',
    '../_base_/datasets/cifar10_bs128.py',
    '../_base_/schedules/cifar10_bs128.py',
    '../_base_/default_runtime.py'
]