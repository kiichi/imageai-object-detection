## What this project do?

Just another experimental machine learning project of using  [Hyper-Kvasir](https://osf.io/mkzcq/) Endoscopy dataset, and I tried [ImageAI](https://github.com/OlafenwaMoses/ImageAI). After running a few days, half of polyps are correctly identified, although a few false-postive happened. After a week of training, it went to overfitting, that means, it grabs good chunk of true-positive but false-positive ones also increased.

### True-Positive Results

They detected polyps correctly. This is at 10th epic. Loss is around 11.0 or so. After this, the loss goes overfitting and reached plato of learning curve.

<img src="https://raw.githubusercontent.com/kiichi/imageai-object-detection/main/preview-picked/positive/output/0b4f0370-b25b-4e6a-a7ac-b09097bfecc3.jpg" height="300"/> <img src="https://github.com/kiichi/imageai-object-detection/blob/main/preview-picked/positive/output/87ede682-dd3d-4415-ac02-b5518a606c79.jpg" height="300"/>


### False-Positive Results

These are non-polyp images. Ok many of them are passed but some of them are detected as polyps, duh. I'll add those calculations: accuracy, recall, IOU, etc...

<img src="https://raw.githubusercontent.com/kiichi/imageai-object-detection/main/preview-picked/negative/output/0c8c6bb6-3b70-4a88-80d8-6c46fc129c30.jpg" height="300"/> <img src="https://raw.githubusercontent.com/kiichi/imageai-object-detection/main/preview-picked/negative/output/0c020c03-da6c-46ec-bc00-09564351e63a.jpg" height="300"/>



On top of my chicken test, how about roast beef and so on?


<img src="https://raw.githubusercontent.com/kiichi/imageai-object-detection/main/preview-picked/negative/output/chicken.jpg" height="300"/> <img src="https://raw.githubusercontent.com/kiichi/imageai-object-detection/main/preview-picked/negative/output/chicken2.jpg" height="300"/>

At least this image with Shiba-inu and bumpy wall passed the test... I also tried some tunnel-ish pichture though. looks ok. it doesn't think it's polyps.

<img src="https://raw.githubusercontent.com/kiichi/imageai-object-detection/main/preview-picked/negative/output/shiba.jpg" height="300"/> <img src="https://github.com/kiichi/imageai-object-detection/blob/main/preview-picked/negative/output/tunnel.jpg" height="300"/>

See some picked preview results [here](https://github.com/kiichi/imageai-object-detection/tree/main/preview-picked/negative/output)

## Background

Since I wasn't happy Apple's CreateML [Results](https://github.com/kiichi/create-ml-object-detection), I took Image.AI in this project which is using YOLO v3 + Tensorflow underneath. Effort is almost same. Basicallyl, Apple's CreateML seems to use YOLO v2 but I'm not sure why it was giving offset rectable boundly and I triple check my coordinate and pixel conversion are ok (inluding HTML picture viewer). Comparing between Apple's CreateML and Wrapper Framework like Image.AI, in terms of setup effort, it's just matter of difference between GUI or CUI although you have more room to play with in Image.AI. In this project, I tried smaller batch size and see if I can compare with bigger batch size. 

## Setup and Reporo

I took an approch recommended by [Richard](https://blogemtech.medium.com/object-detection-with-imageai-106d584984e9), which uses Conda and create boxed environment. When I need it, I just activate it. In this way, you don't have to struggle library version glitch; such as, Python 2 vs 3.

```
conda create -n imageai -c conda-forge python=3.6
conda activate imageai
conda install -c conda-forge tensorflow keras mkl-service opencv numpy scipy pillow matplotlib h5py
```

I also installed coremltools because I wanted convert model to work with iPhone. I'm still working on - just need additional steps to convert custom training files I believe.

```
conda install coremltools
```

(I'll fill in the rest of steps and the training script - super simple no-brain)

## References

- https://blogemtech.medium.com/object-detection-with-imageai-106d584984e9
- https://github.com/OlafenwaMoses/ImageAI/releases/tag/essential-v4
- https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Detection/Custom/CUSTOMDETECTIONTRAINING.md


## Citation

```
@misc{borgli2020, title={Hyper-Kvasir: A Comprehensive Multi-Class Image and Video Dataset for Gastrointestinal Endoscopy}, url={osf.io/mkzcq}, DOI={10.31219/osf.io/mkzcq}, publisher={OSF Preprints}, author={Borgli, Hanna and Thambawita, Vajira and Smedsrud, Pia H and Hicks, Steven and Jha, Debesh and Eskeland, Sigrun L and Randel, Kristin R and Pogorelov, Konstantin and Lux, Mathias and Nguyen, Duc T D and Johansen, Dag and Griwodz, Carsten and Stensland, H{\aa}kon K and Garcia-Ceja, Enrique and Schmidt, Peter T and Hammer, Hugo L and Riegler, Michael A and Halvorsen, P{\aa}l and de Lange, Thomas}, year={2019}, month={Dec}}
```
