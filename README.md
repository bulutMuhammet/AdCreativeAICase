# AdCreativeAICase
Background Remover with OpenCV Python
See live demo at https://mbulut.pythonanywhere.com/

A background can also be generated directly from text using libraries such as DALL·E. I was going to try that too but I didn't have the API key :)

Here is example DALLE usage;

```python
import openai

PROMPT = "Newyork city night time"

openai.api_key = "API KEY"

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
)
```

# How does the system work? 

There are 3 files in the project. 

## add_background.py 
Adds a background to your image if your image is transparent. 

## check_is_transparent.py 
Checks whether the image you have given is transparent. 

## remove_background.py

Tries to remove the background of the picture with the canny edge detection algorithm. 
This is not a deep learning algorithm. So you may have to change the parameters to get the right result. 

# As technology, python and opencv are used.


