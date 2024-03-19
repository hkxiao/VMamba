python -m torch.distributed.run --nnodes=1 --node_rank=0 --nproc_per_node=1 --master_addr="127.0.0.1" --master_port=29501 main.py \
--cfg configs/vssm/vssm_tiny_256.yaml \
--batch-size 128 \
--data-path ../imagenet1k \
--output tmp \
--resume /data/tanglv/xhk/VMamba/classification/tmp/vssm_tiny/20240301101917/ckpt_epoch_234.pth