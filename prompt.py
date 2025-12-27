from PIL import Image

image = Image.open("image.png")

prompt = '''
You are given a form read the form carefully and extract all the information provided in it.
Present the extracted information clearly and accurately.
'''