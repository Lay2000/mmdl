# optimizer
optimizer = dict(type='SGD', lr=0.1, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(policy='step', step=[100, 150])
runner = dict(type='EpochBasedRunner', max_epochs=200)

# python mmdl/tools/visualizations/vis_lr.py mmdl/configs/mobilenet_v3/bsconvu_mobilenet_v3_small_b128_cifar100.py --save-path ./mmdl/logs/lr_vis.png