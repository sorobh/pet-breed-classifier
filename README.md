# Pet Breed Classifier
This demo was crceated as part of [Fast AI course](https://course.fast.ai/) as a sample deep learnng applicatoin in computer vision.

Demo: https://huggingface.co/spaces/SaurabhNayak/My-Pet-Breed-Classifier


## Steps to recreate
1. create a new conda environment: `conda create --name myenv`
2. activate the new env: `conda activate myenv`
3. install all the dependencies `pip install -r requirements.txt`
4. create your model on Google Colab with train.py 
5. run the app.py file: `python app.py`

## Training your model
You can pick an option that's convenient to you based on the system you are using. If you're using a not so powerful system, you may want to use Colab or Kaggle for GPUs to prevent spending time debugging avoidable/out-of-memory errors.

1. sample code from [Fast AI course](https://course.fast.ai/Lessons/lesson2.html): https://shorturl.at/lyDR8
2. sample code can be referred here: https://tmabraham.github.io/blog/gradio_hf_spaces_tutorial
3. use the train.py code in Colab

Once you have trained the model, place the pkl file in the working directory. If you're running a windows machine and you're getting a `NotImplementedError: cannot instantiate 'PosixPath' on your system`, then you may want to refer the windows version of the code in this repository.