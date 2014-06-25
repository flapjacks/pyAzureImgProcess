pyAzureImgProcess
=================

Process uploaded images and upload to Azure blob storage

Requires [PIL](http://pillow.readthedocs.org/en/latest/)

`upload_original_image` resizes an image to fit within the constraints of `maxwidth` and `maxheight` and uploads the image to a supplied Azure blob

`create_thumbnail` crops and resizes an image to a square with sides `thumb_size` pixels long and uploads the image to a supplied Azure blob

Azure blobs must be provided from the [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python)
