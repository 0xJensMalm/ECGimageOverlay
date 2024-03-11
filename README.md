# Image Anonymizer with for sensitive images

This script is designed to anonymize a set of images by adding a "study_id" label on top of the patient information area to ensure confidentiality. It's particularly useful in medical image processing where patient data needs to be protected on a set of images, in this case - a batch of ECG´s. 

## Features

- **Anonymization**: Hides patient information by overlaying a solid rectangle over the specified area.
- **Customizable Study ID**: Allows for the input of a unique study ID which is then overlayed onto the image.

## Prerequisites

To run this script, you will need Python installed on your system along with the following packages:
- `PIL` (Pillow): For image processing functions.

## Setup

1. Ensure you have Python installed on your system.
2. Install the required packages if you haven't already:

   ```bash
   pip install Pillow
