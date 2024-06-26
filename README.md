
<div align="center">
<h1>VMamba </h1>
<h3>VMamba: Visual State Space Model</h3>

[Yue Liu](https://github.com/MzeroMiko)<sup>1</sup>,[Yunjie Tian](https://sunsmarterjie.github.io/)<sup>1</sup>,[Yuzhong Zhao](https://scholar.google.com.hk/citations?user=tStQNm4AAAAJ&hl=zh-CN&oi=ao)<sup>1</sup>, [Hongtian Yu](https://github.com/yuhongtian17)<sup>1</sup>, [Lingxi Xie](https://scholar.google.com.hk/citations?user=EEMm7hwAAAAJ&hl=zh-CN&oi=ao)<sup>2</sup>, [Yaowei Wang](https://scholar.google.com.hk/citations?user=o_DllmIAAAAJ&hl=zh-CN&oi=ao)<sup>3</sup>, [Qixiang Ye](https://scholar.google.com.hk/citations?user=tjEfgsEAAAAJ&hl=zh-CN&oi=ao)<sup>1</sup>, [Yunfan Liu](https://scholar.google.com.hk/citations?user=YPL33G0AAAAJ&hl=zh-CN&oi=ao)<sup>1</sup>

<sup>1</sup>  University of Chinese Academy of Sciences, <sup>2</sup>  HUAWEI Inc.,  <sup>3</sup> PengCheng Lab.

Paper: ([arXiv 2401.10166](https://arxiv.org/abs/2401.10166))


</div>

## Updates
* **` Feb. 18th, 2024`:** Release: all the checkpoints and logs of `VMamba` (`VSSM version 0`) have been released. These checkpoints correspond to the experiments done before date #20240119, if there is any mismatch to the latest code in main, please let me know, and I'll fix that. This is related to issue#1 and issue#37.

* **` Feb. 16th, 2024`:** Fix bug + Improvement: `SS2D.forward_corev1` is deprecated. Fixed some bugs related to issue#30 (in test_selective scan.py, we now compare `ours` with `mamba_ssm` rather than `selective_scan_ref`), issue#32, issue#31. `backward nrow` has been added and tested in selective_scan.

* **` Feb. 4th, 2024`:** Fix bug + Improvement: Do not use `SS2D.forward_corev1` with `float32=False` for training (testing is ok), as it's unstable training in float16 for selective scan. We released `SS2D.forward_corev2`, which is in float32, and is faster than `SS2D.forward_corev1`.

* **` Feb. 1st, 2024`:** Fix bug: we now calculate FLOPs with the algrithm @albertgu [provides](https://github.com/state-spaces/mamba/issues/110), which will be bigger than previous calculation (which is based on the `selective_scan_ref` function, and ignores the hardware-aware algrithm). We plan to update tabels below later.

* **` Jan. 31st, 2024`:** Add feature: `selective_scan` now supports an extra argument `nrow` in `[1, 2, 4]`. If you find your device is strong and the time consumption keeps as `d_state` rises, try this feature to speed up `nrows` x without any cost ! Note this feature is actually a `bug fix` for [mamba](https://github.com/state-spaces/mamba).

* **` Jan. 28th, 2024`:** Add feature: we cloned main into a new branch called `20240128-achieve`, the main branch has experienced a great update now. The code now are much easier to use in your own project, and the training speed is faster! This new version is totally compatible with original one, and you can use previous checkpoints without any modification. But if you want to use exactly the same models as original ones, just change `forward_core = self.forward_corev1` into `forward_core = self.forward_corev0` in `classification/models/vmamba/vmamba.py#SS2D` or you can change into the branch `20240128-archive` instead.

* **` Jan. 23th, 2024`:** Add feature:  we add an alternative for mamba_ssm and causal_conv1d. Typing `pip install .` in `selective_scan` and you can get rid of those two packages. ~~Just turn `self.forward_core = self.forward_corev0` to `self.forward_core = self.forward_corev1` in `classification/models/vmamba/vmamba.py#SS2D.__init__` to enjoy that feature.~~ The training speed is expected to raise from 20min/epoch for tiny in 8x4090GPU to 17min/epoch, GPU memory cost reduces too.

* **` Jan. 22th, 2024`:** We have released VMamba-T/S pre-trained weights. The ema weights should be converted before transferring to downstream tasks to match the module names using [get_ckpt.py](analyze/get_ckpt.py).

* **` Jan. 19th, 2024`:** The source code for classification, object detection, and semantic segmentation are provided. 


## Abstract

Convolutional Neural Networks (CNNs) and Vision Transformers (ViTs) stand as the two most popular foundation models for visual representation learning. While
CNNs exhibit remarkable scalability with linear complexity w.r.t. image resolution, ViTs surpass them in fitting capabilities despite contending with quadratic
complexity. A closer inspection reveals that ViTs achieve superior visual modeling performance through the incorporation of global receptive fields and dynamic
weights. This observation motivates us to propose a novel architecture that inherits these components while enhancing computational efficiency. To this end, we draw
inspiration from the recently introduced state space model and propose the Visual State Space Model (VMamba), which achieves linear complexity without sacrificing global receptive fields. To address the encountered direction-sensitive issue, we introduce the Cross-Scan Module (CSM) to traverse the spatial domain and convert any non-causal visual image into order patch sequences. Extensive experimental results substantiate that VMamba not only demonstrates promising capabilities across various visual perception tasks, but also exhibits more pronounced advantages over established benchmarks as the image resolution increases. 

## Overview

* [**VMamba**](https://arxiv.org/abs/2401.10166) serves as a general-purpose backbone for computer vision with linear complexity and shows the advantages of global receptive fields and dynamic weights.

<p align="center">
  <img src="assets/acc_flow_comp.png" alt="accuracy" width="80%">
</p>

* **2D-Selective-Scan of VMamba**

<p align="center">
  <img src="assets/ss2d.png" alt="arch" width="60%">
</p>

* **VMamba has global effective receptive field**

<p align="center">
  <img src="assets/erf_comp.png" alt="erf" width="50%">
</p>


## Main Results

We will release all the pre-trained models/logs in few days!

* **Classification on ImageNet-1K**


| name | pretrain | resolution |acc@1 | #params | FLOPs | checkpoints/logs | best epoch | use ema |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| DeiT-S | ImageNet-1K | 224x224 | 79.8 | 22M | 4.6G | -- | -- | -- |
| DeiT-B | ImageNet-1K | 224x224 | 81.8 | 86M | 17.5G | -- | -- | -- |
| DeiT-B | ImageNet-1K | 384x384 | 83.1 | 86M | 55.4G | -- | -- | -- |
| Swin-T | ImageNet-1K | 224x224 | 81.2 | 28M | 4.5G | -- | -- | -- |
| Swin-S | ImageNet-1K | 224x224 | 83.2 | 50M | 8.7G | -- | -- | -- |
| Swin-B | ImageNet-1K | 224x224 | 83.5 | 88M | 15.4G | -- | -- | -- |
| VMamba-T | ImageNet-1K | 224x224 | 82.2 | 22M | ~~4.5G~~ 5.6G | [ckpt](https://github.com/MzeroMiko/VMamba/releases/download/%2320240218/vssmtiny_dp01_ckpt_epoch_292.pth)/[log](https://github.com/MzeroMiko/VMamba/releases/download/%2320240218/vssmtiny_dp01_e292_woema.log) | 292 | did'nt add |
| VMamba-S | ImageNet-1K | 224x224 | 83.5 | 44M | ~~9.1G~~ 11.2G | [ckpt](https://github.com/MzeroMiko/VMamba/releases/download/%2320240218/vssmsmall_dp03_ckpt_epoch_238.pth)/[log](https://github.com/MzeroMiko/VMamba/releases/download/%2320240218/vssmsmall_dp03_e238_ema.log) | 238 | true |
| VMamba-B | ImageNet-1K | 224x224 | 83.2 | 75M | ~~15.2G~~ 18.0G | [ckpt](https://github.com/MzeroMiko/VMamba/releases/download/%2320240218/vssmbase_dp05_ckpt_epoch_260.pth)/[log](https://github.com/MzeroMiko/VMamba/releases/download/%2320240218/vssmbase_dp05_e260_woema.log) | 260 | did'nt add |
| VMamba-B* | ImageNet-1K | 224x224 | 83.7 | 75M | ~~15.2G~~ 18.0G | [ckpt](https://github.com/MzeroMiko/VMamba/releases/download/%2320240218/vssmbase_dp06_ckpt_epoch_241.pth)/[log](https://github.com/MzeroMiko/VMamba/releases/download/%2320240218/vssmbase_dp06_e241_ema.log) | 241 | true |

*Most backbone models trained without ema, `which do not enhance performance \cite(Swin-Transformer)`. We use ema because our model is still under development.*

*The checkpoints used in object detection and segmentation is `VMamba-B with droppath 0.5` + `no ema`. `VMamba-B*` represents for `VMamba-B with droppath 0.6 + ema`, the performance of which is `non-ema: 83.3 in epoch 262;  ema: 83.7 in epoch 241`. If you are about to use VMamba-B in downstream tasks, try `VMamba-B*` rather than `VMamba-B`, as it is supposed to perform better.*

* **Object Detection on COCO**
  
| Backbone | #params | FLOPs | Detector | box mAP | mask mAP | checkpoints/logs |
| :---: | :---: | :---: | :---: | :---: | :---: |:---: |
| Swin-T | 48M | 267G | MaskRCNN@1x | 42.7| 39.3 |-- |
| VMamba-T | 42M | 262G | MaskRCNN@1x | 46.5| 42.1 |[ckpt](https://drive.google.com/file/d/1SIQFPpXkVBPB4mx1VO9P9nH4ebvTH0W5/view?usp=sharing)/[log](https://drive.google.com/file/d/15nd3AZuOkHpqlZhVUEXilnsVzd1qn8Kc/view?usp=sharing) |
| Swin-S | 69M | 354G | MaskRCNN@1x | 44.8| 40.9 |-- |
| VMamba-S | 64M | 357G | MaskRCNN@1x | 48.2| 43.0 |[ckpt](https://drive.google.com/file/d/1LzytVo2wTKgOxyBadstzacslwol8Dvhq/view?usp=sharing)/[log](https://drive.google.com/file/d/1TbYZhban4VqC-9kQ8-kuZOPSBX484sSj/view?usp=sharing) |
| Swin-B | 107M | 496G | MaskRCNN@1x | 46.9| 42.3 |-- |
| VMamba-B | 96M | 482G | MaskRCNN@1x | 48.5| 43.1 |[ckpt](https://huggingface.co/sunsmarterjieleaf/VMamba/tree/main)/[log](https://huggingface.co/sunsmarterjieleaf/VMamba/tree/main) |
| Swin-T | 48M | 267G | MaskRCNN@3x | 46.0| 41.6 |-- |
| VMamba-T | 42M | 262G | MaskRCNN@3x | 48.5| 43.2 |[ckpt](https://drive.google.com/file/d/1SmsgM2SR_GbKjq1EkcLcQXCEIlPhA-_r/view?usp=sharing)/[log](https://drive.google.com/file/d/1EVUKFsPQI3bqelX7-WlTKFdToXjwmcXU/view?usp=sharing) |
| Swin-S | 69M | 354G | MaskRCNN@3x | 48.2| 43.2 |-- |
| VMamba-S | 64M | 357G | MaskRCNN@3x | 49.7| 44.0 |[ckpt](https://huggingface.co/sunsmarterjieleaf/VMamba/tree/main)/[log](https://huggingface.co/sunsmarterjieleaf/VMamba/tree/main) |

* **Semantic Segmentation on ADE20K**

| Backbone | Input|  #params | FLOPs | Segmentor | mIoU | checkpoints/logs |
| :---: | :---: | :---: | :---: | :---: | :---: |:---: |
| Swin-T | 512x512 | 60M | 945G | UperNet@160k | 44.4| -- |
| VMamba-T| 512x512 | 55M | 939G | UperNet@160k | 47.3| [ckpt](https://drive.google.com/file/d/1hLAGFBRJfaFSzyPlqsGbKXXN_gQJMLzn/view?usp=sharing)/[log](https://drive.google.com/file/d/17nh9_hdF9QQxyqj81U86HoGUnMxZQ4nN/view?usp=sharing) |
| Swin-S | 512x512 | 81M | 1039G | UperNet@160k | 47.6| -- |
| VMamba-S| 512x512 | 76M | 1037G | UperNet@160k | 49.5| [ckpt](https://drive.google.com/file/d/18GReI1A6LckwnPrnEFPXp9at7VB8GiJW/view?usp=sharing)/[log](https://drive.google.com/file/d/1m-Pd4_kPgF6Dt2E33sfIf_g9jVWxfPnG/view?usp=sharing) |
| Swin-B | 512x512 | 121M | 1188G | UperNet@160k | 48.1| -- |
| VMamba-B| 512x512 | 110M | 1167G | UperNet@160k | 50.0| [ckpt](https://huggingface.co/sunsmarterjieleaf/VMamba/tree/main)/[log](https://huggingface.co/sunsmarterjieleaf/VMamba/tree/main) |
| Swin-S | 640x640 | 81M | 1614G | UperNet@160k | 47.9| -- |
| VMamba-S| 640x640 | 76M | 1620G | UperNet@160k | 50.8| [ckpt](https://huggingface.co/sunsmarterjieleaf/VMamba/tree/main)/[log](https://huggingface.co/sunsmarterjieleaf/VMamba/tree/main) |



## Getting Started

### Installation

**step1:Clone the VMamba repository:**

To get started, first clone the VMamba repository and navigate to the project directory:

```bash
git clone https://github.com/MzeroMiko/VMamba.git
cd VMamba

```

**step2:Environment Setup:**

VMamba recommends setting up a conda environment and installing dependencies via pip. Use the following commands to set up your environment:
#### Create and activate a new conda environment

```bash
conda create -n vmamba
conda activate vmamba
```
#### Install Dependencies.
```bash
pip install -r requirements.txt
# Install selective_scan and its dependencies
cd selective_scan && pip install . && pytest
```



Optional Dependencies for Model Detection and Segmentation:
```bash
pip install mmengine==0.10.1 mmcv==2.1.0 opencv-python-headless ftfy
pip install mmdet==3.3.0 mmsegmentation==1.2.2 mmpretrain==1.2.0
```

<!-- conda create -n cu12 python=3.10 -y && conda activate cu12
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
# install cuda121 for windows
# install https://visualstudio.microsoft.com/visual-cpp-build-tools/
pip install timm==0.4.12 fvcore packaging -->


### Model Training and Inference

**Classification:**

To train VMamba models for classification on ImageNet, use the following commands for different configurations:

```bash
# For VMamba Tiny
python -m torch.distributed.launch --nnodes=1 --node_rank=0 --nproc_per_node=8 --master_addr="127.0.0.1" --master_port=29501 main.py --cfg configs/vssm/vssm_tiny_224.yaml --batch-size 128 --data-path /dataset/ImageNet2012 --output /tmp

# For VMamba Small
python -m torch.distributed.launch --nnodes=1 --node_rank=0 --nproc_per_node=8 --master_addr="127.0.0.1" --master_port=29501 main.py --cfg configs/vssm/vssm_small_224.yaml --batch-size 128 --data-path /dataset/ImageNet2012 --output /tmp

# For VMamba Base
python -m torch.distributed.launch --nnodes=1 --node_rank=0 --nproc_per_node=8 --master_addr="127.0.0.1" --master_port=29501 main.py --cfg configs/vssm/vssm_base_224.yaml --batch-size 128 --data-path /dataset/ImageNet2012 --output /tmp

```

**Detection and Segmentation:**

For detection and segmentation tasks, follow similar steps using the appropriate config files from the `configs/vssm` directory. Adjust the `--cfg`, `--data-path`, and `--output` parameters according to your dataset and desired output location.

### Analysis Tools

VMamba includes tools for analyzing the effective receptive field, FLOPs, loss, and scaling behavior of the models. Use the following commands to perform analysis:

```bash
# Analyze the effective receptive field
CUDA_VISIBLE_DEVICES=0 python analyze/get_erf.py > analyze/show/erf/get_erf.log 2>&1

# Analyze FLOPs
CUDA_VISIBLE_DEVICES=0 python analyze/get_flops.py > analyze/show/flops/flops.log 2>&1

# Analyze loss
CUDA_VISIBLE_DEVICES=0 python analyze/get_loss.py

# Further analysis on scaling behavior
python analyze/scaleup_show.py

```

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=MzeroMiko/VMamba&type=Date)](https://star-history.com/#MzeroMiko/VMamba&Date)

## Citation

```
@article{liu2024vmamba,
  title={VMamba: Visual State Space Model},
  author={Liu, Yue and Tian, Yunjie and Zhao, Yuzhong and Yu, Hongtian and Xie, Lingxi and Wang, Yaowei and Ye, Qixiang and Liu, Yunfan},
  journal={arXiv preprint arXiv:2401.10166},
  year={2024}
}
```

## Acknowledgment

This project is based on Mamba ([paper](https://arxiv.org/abs/2312.00752), [code](https://github.com/state-spaces/mamba)), Swin-Transformer ([paper](https://arxiv.org/pdf/2103.14030.pdf), [code](https://github.com/microsoft/Swin-Transformer)), ConvNeXt ([paper](https://arxiv.org/abs/2201.03545), [code](https://github.com/facebookresearch/ConvNeXt)), [OpenMMLab](https://github.com/open-mmlab),
and the `analyze/get_erf.py` is adopted from [replknet](https://github.com/DingXiaoH/RepLKNet-pytorch/tree/main/erf), thanks for their excellent works.

* **We release [Fast-iTPN](https://github.com/sunsmarterjie/iTPN/tree/main/fast_itpn) recently, which reports the best performance on ImageNet-1K at Tiny/Small/Base level models as far as we know. (Tiny-24M-86.5%, Small-40M-87.8%, Base-85M-88.75%)**
