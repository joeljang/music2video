# music2video Overview

A repo for making a music video with Wav2CLIP and VQGAN-CLIP. 

The base code was derived from [VQGAN-CLIP](https://github.com/nerdyrodent/VQGAN-CLIP)
The CLIP embedding for audio was derived from [Wav2CLIP](https://github.com/descriptinc/lyrebird-wav2clip)

Environment:

* Tested on Ubuntu 20.04
* GPU: Nvidia RTX 3090
* Typical VRAM requirements:
  * 24 GB for a 900x900 image
  * 10 GB for a 512x512 image
  * 8 GB for a 380x380 image

## Set up

This example uses [Anaconda](https://www.anaconda.com/products/individual#Downloads) to manage virtual Python environments.

Create a new virtual Python environment for VQGAN-CLIP:

```sh
conda create --name vqgan python=3.9
conda activate vqgan
```

Install Pytorch in the new enviroment:

Note: This installs the CUDA version of Pytorch, if you want to use an AMD graphics card, read the [AMD section below](#using-an-amd-graphics-card).

```sh
pip install torch==1.9.0+cu111 torchvision==0.10.0+cu111 torchaudio==0.9.0 -f https://download.pytorch.org/whl/torch_stable.html
```

Install other required Python packages:

```sh
pip install ftfy regex tqdm omegaconf pytorch-lightning IPython kornia imageio imageio-ffmpeg einops torch_optimizer
```

Or use the ```requirements.txt``` file, which includes version numbers.

Clone required repositories:

```sh
git clone 'https://github.com/nerdyrodent/VQGAN-CLIP'
cd VQGAN-CLIP
git clone 'https://github.com/openai/CLIP'
git clone 'https://github.com/CompVis/taming-transformers'
```

Note: In my development environment both CLIP and taming-transformers are present in the local directory, and so aren't present in the `requirements.txt` or `vqgan.yml` files.

As an alternative, you can also pip install taming-transformers and CLIP.

You will also need at least 1 VQGAN pretrained model. E.g.

```sh
mkdir checkpoints

curl -L -o checkpoints/vqgan_imagenet_f16_16384.yaml -C - 'https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1' #ImageNet 16384
curl -L -o checkpoints/vqgan_imagenet_f16_16384.ckpt -C - 'https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fckpts%2Flast.ckpt&dl=1' #ImageNet 16384
```
Note that users of ```curl``` on Microsoft Windows should use double quotes.

The `download_models.sh` script is an optional way to download a number of models. By default, it will download just 1 model.

See <https://github.com/CompVis/taming-transformers#overview-of-pretrained-models> for more information about VQGAN pre-trained models, including download links.

By default, the model .yaml and .ckpt files are expected in the `checkpoints` directory.
See <https://github.com/CompVis/taming-transformers> for more information on datasets and models.

## Run

To generate video from music, specify your music as shown in the example below:

```sh
python generate.py -vid -i 200 -vl 5 -o outputs/output.png -ap "music_sample/meeting_easy.wav" -gid 0
```

```sh
python generate.py -vid -i 200 -vl 5 -o outputs2/output.png -ap "music_sample/merry_go_round.wav" -gid 0
```


## Citations

```bibtex
@misc{unpublished2021clip,
    title  = {CLIP: Connecting Text and Images},
    author = {Alec Radford, Ilya Sutskever, Jong Wook Kim, Gretchen Krueger, Sandhini Agarwal},
    year   = {2021}
}
```

```bibtex
@misc{esser2020taming,
      title={Taming Transformers for High-Resolution Image Synthesis}, 
      author={Patrick Esser and Robin Rombach and Björn Ommer},
      year={2020},
      eprint={2012.09841},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

```bibtex
@article{wu2021wav2clip,
  title={Wav2CLIP: Learning Robust Audio Representations From CLIP},
  author={Wu, Ho-Hsiang and Seetharaman, Prem and Kumar, Kundan and Bello, Juan Pablo},
  journal={arXiv preprint arXiv:2110.11499},
  year={2021}
}
```