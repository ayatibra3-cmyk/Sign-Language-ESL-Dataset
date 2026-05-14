# Sign Language ESL Dataset: Letters & Numbers
## Overview
This dataset is designed for Sign Language Translation and Alphabet Recognition tasks. It contains high-quality images representing the English Sign Language (ESL) characters (A-Z) and digits (0-9). The dataset is optimized for educational applications and accessibility tools for the deaf and hard-of-hearing community.
### Dataset Preview
| ![A](https://raw.githubusercontent.com/ayatibra3-cmyk/Sign-Language-ESL-Dataset/main/ASL/A/A.jpg) | ![B](https://raw.githubusercontent.com/ayatibra3-cmyk/Sign-Language-ESL-Dataset/main/ASL/B/B.jpg) | ![C](https://raw.githubusercontent.com/ayatibra3-cmyk/Sign-Language-ESL-Dataset/main/ASL/C/C.jpg) |
![D](https://raw.githubusercontent.com/ayatibra3-cmyk/Sign-Language-ESL-Dataset/main/ASL/D/D.jpg) | ![E](https://raw.githubusercontent.com/ayatibra3-cmyk/Sign-Language-ESL-Dataset/main/ASL/E/E.jpg) | 
 ![1](https://raw.githubusercontent.com/ayatibra3-cmyk/Sign-Language-ESL-Dataset/main/ASL/1/1.jpg) | ![2](https://raw.githubusercontent.com/ayatibra3-cmyk/Sign-Language-ESL-Dataset/main/ASL/2/2.jpg) | ![3](https://raw.githubusercontent.com/ayatibra3-cmyk/Sign-Language-ESL-Dataset/main/ASL/3/3.jpg) | ![4](https://raw.githubusercontent.com/ayatibra3-cmyk/Sign-Language-ESL-Dataset/main/ASL/4/4.jpg) | ![5](https://raw.githubusercontent.com/ayatibra3-cmyk/Sign-Language-ESL-Dataset/main/ASL/5/5.jpg) |

## Dataset Structure
The data is organized into folders, where each folder represents a specific label (Character or Number).
• Total Classes: 37 (A-Z, 0-9, and a special SPACE class).
• Format: Images are in .jpg / .png format.
• Naming Convention: ASL/{Label}/{image_name}.jpg
Special Classes:
• SPACE: Contains neutral hand positions used to represent intervals between words in a sentence.
## Context & Inspiration
This dataset was developed as part of a graduation project aimed at bridging the communication gap between hearing and non-hearing individuals. Inspired by professional sign language dictionaries, the images focus on clarity and consistency in hand gestures.
## Usage & Implementation
You can use the provided Python script sign.py to translate text into a visual sign sequence.
Quick Start:
1.Clone the repository:
git clone https://github.com/ayatibra3-cmyk/Sign-Language-ESL-Dataset.git
2.Run the translator script:
python sign.py
## Key Features
• Sequential Display: Supports letter-by-letter rendering for fingerspelling.
• Variable Speed: Includes functionality to control translation speed (0.2s to 2.0s delay).
• Word Segmentation: Implements a neutral "Space" image for better sentence readability.
## License
This dataset is available for public and educational use.
