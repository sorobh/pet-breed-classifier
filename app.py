import gradio as gr
from fastai.vision.all import *
import skimage

learn = load_learner('export.pkl')

labels = learn.dls.vocab
def predict(img):
    img = PILImage.create(img)
    pred,pred_idx,probs = learn.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}

title = "Pet Breed Classifier"
description = "<div style='text-align: center'>A pet breed classifier trained on the Oxford Pets dataset with fastai. Please upload image of a dog or cat, and the model will predict the breed of the pet.</div>"
article="<p style='text-align: center'><a href='https://tmabraham.github.io/blog/gradio_hf_spaces_tutorial' target='_blank'>Blog post</a></p>"
examples = []
interpretation='default'
enable_queue=True

gr.Interface(fn=predict,
             inputs=gr.inputs.Image(label="Upload a jpg image",type="filepath"),
             outputs=gr.outputs.Label(num_top_classes=3),
             title=title,
             description=description,
            ).launch()

