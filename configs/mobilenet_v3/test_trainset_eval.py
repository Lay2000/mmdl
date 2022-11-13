_base_ = [
    '../_base_/models/mobilenet_v3_small_cifar100.py',
    '../_base_/datasets/cifar100_bs128.py',
    '../_base_/schedules/cifar100_bs128.py', '../_base_/default_runtime.py'
]

lr_config = dict(policy='step', step=[100, 150, 180])
runner = dict(type='EpochBasedRunner', max_epochs=200)

model = dict(
    head=dict(
        type='StackedLinearClsHeadWithPred',
        num_classes=100,
        in_channels=576,
        mid_channels=[1280],
        act_cfg=dict(type='HSwish'),
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 5))
)