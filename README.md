# python-image_to_bytearray
Python script for converting an image to bytearray.

## Preparing your images.
Before the script is run, the image should be prepared for the screen you gonna use it on.
I needed to convert pictures for the [Waveshare ePaper 5in65](https://www.waveshare.com/wiki/Pico-ePaper-5.65#Image_Processing)
I tried to convert the colors using script, but the results was not good enough.

### Guide using photoshop.
  1.	Open the Image in Photoshop:
  	•	Open your image file in Photoshop.

  3.	Create a 7-Color Palette:
       		• Go to Image > Mode > Indexed Color.
  		• In the Palette dropdown, select Custom.
  		• Create a palette with the following colors:
  		• Black: (0, 0, 0)
  		• White: (255, 255, 255)
  		• Green: (0, 255, 0)
  		• Blue: (0, 0, 255)
  		• Red: (255, 0, 0)
  		• Yellow: (255, 255, 0)
  		• Orange: (255, 128, 0)

  5.	Convert the Image to Indexed Mode:
  	•	After creating the custom palette, click OK to convert the image to indexed mode using the 7-color palette.
		• Dither should be "Diffusion" and "Amount" 80%.

  6.	Save the Image:
  	•	Save the converted image as a PNG file.

## Running the script
1. Download image_to_bin.py and put it in a folder you gonna convert the pictures.
2. Put the images in the folder.
3. Run the script, for example by commandline "python image_to_bin.py"
4. All images will be converted and have the .bin extention.
