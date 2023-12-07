# Training the model
from fastai.vision.all import *
path = untar_data(URLs.PETS)
dls = ImageDataLoaders.from_name_re(path, get_image_files(path/'images'), pat='(.+)_\d+.jpg', item_tfms=Resize(460), batch_tfms=aug_transforms(size=224, min_scale=0.75))
learn = vision_learner(dls, models.resnet50, metrics=accuracy)
learn.fine_tune(1)
learn.path = Path('.')
learn.export()

# Allow Google Colab access to your Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Give the address of the folder where you want the pkl file to be saved. Note, given the size of the model, it may take a minute for the file to appear even if the code has been run
learn.path = Path('/content/drive/My Drive/Colab_Notebooks')
learn.export('export.pkl')


# Donwload this pkl file and place it in the current working directory