![Banner](banner.png)

## 📖About

Welcome to our comprehensive project on autoencoder archictectures, where start with introducing the motivations and purposes of autoencoder architectures. From there, we cover how to implement the (Vanilla) Autoencoder (AE), Variational Autoencoder (VAE), and finally, the more SOTA [Vector-Quantized Variational Autoencoder (VQVAE)](https://arxiv.org/pdf/1711.00937.pdf). These implemntations are supplemented with an array of informative ablations, visualizations, and conceptual problems to give the learner a more complete understanding of the topic. Our "Where to Go Next" and "References" sections are great resources for additional learning. 

This resource was created as a final project for UC Berkeley's Deep Learning course [CS 182](https://inst.eecs.berkeley.edu/~cs182/).

## 💻 Setup

There are two ways to interact with our project. One can choose to utilize Google Colab OR run the notebooks locally. Regardless of the environment, we recommend using a GPU for the VQ-VAE notebook.

### Google Colab Setup
1. Clone or copy the repository to your local device.
2. Upload the entire repository folder to Google Colab.
3. When you start with the notebooks, ensure your RunTime is GPU enabled.

### Local Setup

1. Clone or copy the repository to your local device.
2. We recommend setting up a [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) environment for this project. Once you have Conda set up on your device, create an 
```bash
conda create --name your_env_name python=3.8
```
3. Now, setup the project to be editable using:
```bash
python setup.py develop
```
4. Finally, install dependencies, and you should be ready to learn!
```bash
pip install -r requirements.txt
```

Start with the AE_VAE.ipynb notebook. The directions should be very detailed and sequential, and it is recommended to have the conceptual guide open as a companion to your work.

## Meta-Commentary

## Where to Go Next

## References

bibtex here + remember to potentially have a license for the repo

## About Us

Just our names + links to our personal linkedin and github
