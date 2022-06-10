# music2video Overview

A repo for making a AI-generated music video from any song with Wav2CLIP and VQGAN-CLIP. 

The base code was derived from [VQGAN-CLIP](https://github.com/nerdyrodent/VQGAN-CLIP)
The CLIP embedding for audio was derived from [Wav2CLIP](https://github.com/descriptinc/lyrebird-wav2clip)

A technical paper describing the mechanism is provide in the following link: [Music2Video: Automatic Generation of Music Video with fusion of audio and text](https://arxiv.org/abs/2201.03809v2)

The citation for the technical paper is provided below:
```bibtex
@article{jang2022music2video,
  title={Music2Video: Automatic Generation of Music Video with fusion of audio and text},
  author={Jang, Joel and Shin, Sumin and Kim, Yoonjeon},
  journal={arXiv preprint arXiv:2201.03809},
  year={2022}
}
```

## Sample

A sample of a music video created with this repository is available at [this youtube link](https://youtu.be/CaS-ruEiUcg)
Here is a sample of snapshots in a generated music-video with its lyrics:
![sample](https://user-images.githubusercontent.com/41067235/146651217-6fee9676-42a6-4359-9c5b-49beef42c6c9.png)

You can make one with your own song too!

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
pip install ftfy regex tqdm omegaconf pytorch-lightning IPython kornia imageio imageio-ffmpeg einops torch_optimizer wav2clip
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

## Making the music video

To generate video from music, please specify your music and the following code examples can be used depending on the need. We provide a sample music file & lyrics file from Yannic Kilcher's [repo](https://github.com/yk/clip_music_video). 

If you have a lyrics file with time-stamp information such as the example in 'lyrics/imagenet_song_lyrics.csv', you can make a lyrics-audio guided music video with the following command:

```sh
python generate.py -vid -o outputs/output.png -ap "imagenet_song.mp3" -lyr "lyrics/imagenet_song_lyrics.csv" -gid 2 -ips 100
```

To interpolate between audio representation and text representation, use to following code (gives a more "music video" feeling) 

```sh
python generate_interpolate.py -vid -ips 100 -o outputs/output.png -ap "imagenet_song.mp3" -lyr "lyrics/imagenet_song_lyrics.csv" -gid 0
```

If you do not have lyrics information, you can run the following command using only audio prompts:

```sh
python generate.py -vid -o outputs/output.png -ap "imagenet_song.mp3" -gid 2 -ips 100
```

If there was an error with any of the above commands during merging of the video segments, please use combine_mp4.py to separately concat the video segments from the output directory or download the video segments from output directory and manually merge them using video editing software.

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
