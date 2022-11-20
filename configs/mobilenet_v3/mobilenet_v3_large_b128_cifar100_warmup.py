_base_ = [
    '../_base_/models/mobilenet_v3_large_cifar100.py',
    '../_base_/datasets/cifar100_bs128.py',
    '../_base_/schedules/cifar100_bs128_warmup.py', '../_base_/default_runtime.py'
]

lr_config = dict(policy='poly', power=0.7, min_lr=1e-4, by_epoch=False, warmup='exp', warmup_ratio=0.1, warmup_iters=5, warmup_by_epoch=True)
runner = dict(type='EpochBasedRunner', max_epochs=200)
