# Pet Breed Classifier
This demo was crceated as part of [Fast AI course](https://course.fast.ai/) as a sample deep learning applicatoin in computer vision. Demo is hosted [here](https://huggingface.co/spaces/SaurabhNayak/My-Pet-Breed-Classifier).

## Steps to recreate
1. create a new conda environment: `conda create --name myenv`
2. activate the new env: `conda activate myenv`
3. install all the dependencies `pip install -r requirements.txt`
4. create your own model on Google Colab with `train.py` and place the .pkl file in the working directory
5. run the app.py file: `python app.py`

## Training your model
You can pick an option that's convenient to you based on the system you are using. If you're using a not so powerful system, you may want to use Colab or Kaggle for GPUs to prevent spending time debugging avoidable/out-of-memory errors.

1. sample code from [Fast AI course](https://course.fast.ai/Lessons/lesson2.html): https://shorturl.at/lyDR8
2. another version can be referred [here](https://tmabraham.github.io/blog/gradio_hf_spaces_tutorial)
3. use the train.py code from this repo in Google Colab

Once you have trained the model, place the pkl file in the working directory. 

## Limitations
This code is compatible with UNIX based systems. If you're running a windows machine and you're getting a `NotImplementedError: cannot instantiate 'PosixPath' on your system`, then you may want to refer the another version of the code that's compatible with windows machines. The repo can be downloaded [here](https://drive.google.com/file/d/18aC-Ox6QPVrE5pduRKVZRrxdKmkK_RUP/view?usp=sharing). Note- This file is ~800 MB and it has a .pth file instead of .pkl file

## More
1. [Which image models are best? | Kaggle](https://www.kaggle.com/code/jhoward/which-image-models-are-best)
2. [The best vision models for fine-tuning | Kaggle](https://www.kaggle.com/code/jhoward/the-best-vision-models-for-fine-tuning)
