# Model settings
model = dict(
    type='ImageClassifier',
    backbone=dict(type='DenseNetCifar', arch='190'),
    neck=dict(type='GlobalAveragePooling'),
    head=dict(
        type='LinearClsHead',
        num_classes=10,
        in_channels=2190,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
    ))
