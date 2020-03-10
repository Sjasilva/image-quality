import os.path

import tensorflow as tf
import tensorflow_datasets.public_api as tfds

from . import CHECKSUMS_PATH

tfds.download.add_checksums_dir(CHECKSUMS_PATH)

CITATION = r"""
@article{wang2004image,
  title={Image quality assessment: from error visibility to structural similarity},
  author={Wang, Zhou and Bovik, Alan C and Sheikh, Hamid R and Simoncelli, Eero P and others},
  journal={IEEE transactions on image processing},
  volume={13},
  number={4},
  pages={600--612},
  year={2004}}
"""
DESCRIPTION = """
Quality Assessment research strongly depends upon subjective experiments to provide calibration 
data as well as a testing mechanism. After all, the goal of all QA research is to make quality 
predictions that are in agreement with subjective opinion of human observers. In order to calibrate 
QA algorithms and test their performance, a data set of images and videos whose quality has been ranked by 
human subjects is required. The QA algorithm may be trained on part of this data set, and tested on the rest.

At LIVE (in collaboration with The Department of Psychology at the University of Texas at Austin), 
an extensive experiment was conducted to obtain scores from human subjects for a number of images 
distorted with different distortion types. These images were acquired in support of a research 
project on generic shape matching and recognition.
"""
URLS = ["https://live.ece.utexas.edu/research/quality/subjective.htm"]
LICENSE = """
-----------COPYRIGHT NOTICE STARTS WITH THIS LINE------------ 
Copyright (c) 2003 The University of Texas at Austin 
All rights reserved. 

Permission is hereby granted, without written agreement and without license or royalty fees, to use, copy, modify, and distribute this database (the images, the results and the source files) and its documentation for any purpose, provided that the copyright notice in its entirety appear in all copies of this database, and the original source of this database, Laboratory for Image and Video Engineering (LIVE, http://live.ece.utexas.edu ) and Center for Perceptual Systems (CPS, http://www.cps.utexas.edu ) at the University of Texas at Austin (UT Austin, http://www.utexas.edu ), is acknowledged in any publication that reports research using this database.

The database and our papers are to be cited in the bibliography as:

H. R. Sheikh, Z. Wang, L. Cormack and A. C. Bovik, "LIVE Image Quality Assessment Database", http://live.ece.utexas.edu/research/quality . 
H. R. Sheikh, M.F. Sabir and A.C. Bovik, "A statistical evaluation of recent full reference image quality assessment algorithms", IEEE Transactions on Image Processing, vol. 15, no. 11, pp. 3440-3451, Nov. 2006.
Z. Wang, A.C. Bovik, H.R. Sheikh and E.P. Simoncelli, "Image quality assessment: from error visibility to structural similarity," IEEE Transactions on Image Processing , vol.13, no.4, pp. 600- 612, April 2004.
IN NO EVENT SHALL THE UNIVERSITY OF TEXAS AT AUSTIN BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF THIS DATABASE AND ITS DOCUMENTATION, EVEN IF THE UNIVERSITY OF TEXAS AT AUSTIN HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. 

THE UNIVERSITY OF TEXAS AT AUSTIN SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE DATABASE PROVIDED HEREUNDER IS ON AN "AS IS" BASIS, AND THE UNIVERSITY OF TEXAS AT AUSTIN HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS. 

The following input images are from the CD "Austin and Vicinity" by Visual Delights Inc.  
( http://www.visualdelights.net ) coinsinfountain.bmp, dancers.bmp, flowersonih35.bmp, studentsculpture.bmp, carnivaldolls.bmp, cemetry.bmp, manfishing.bmp, churchandcapitol.bmp, building2.bmp These images were modified from the original (resized) and then compressed to obtain images in the database. Permission to release these images and their distorted versions was graciously granted by Visual Delights Inc. These images may not be used outside the scope of this database without their prior permission. The rest of the images were public domain Kodak PhotoCD images obtained from the Internet. 
-----------COPYRIGHT NOTICE ENDS WITH THIS LINE------------
"""
SUPERVISED_KEYS = ("distorted_image", "dmos")


class LiveIQA(tfds.core.GeneratorBasedBuilder):
    VERSION = tfds.core.Version("1.0.0")

    def _info(self):
        return tfds.core.DatasetInfo(
            builder=self,
            description=DESCRIPTION,
            features=tfds.features.FeaturesDict({
                "distortion": tfds.features.Text(),
                "index": tf.int32,
                "distorted_image": tfds.features.Image(),
                "reference_image": tfds.features.Image(),
                "dmos": tf.float32,
                "dmos_realigned": tf.float32,
                "dmos_realigned_std": tf.float32,
            }),
            supervised_keys=SUPERVISED_KEYS,
            homepage=URLS[0],
            citation=CITATION,
            redistribution_info={
                'license': LICENSE,
            },
        )

    def _split_generators(self, manager):
        live_url = "https://public.boxcloud.com/d/1/b1!b8VxfaGfvAZG5cv-zhursuZGAJXFlXocptfdul6wuB3mcJh515xKHJ9dRfNKikW33rDbVJWE9LcOq6Q2zq2mttWQxuVDnphCwdHpS11SiIc4ixL63AVDoDyBqf8WHopCnLJBqNs-vl7XUFly-W4C47M6yPzNiARh_YvFW2BOZ_7k_lqXoYbfOSZbIoq7QR8SwCwMiDZc3pKLK5r5Ocw0nj55_7u9MxS95FDUnBLxeDMSt1GN_9AKPwiav3nxPt5O_cAOTXkd2ZA-KqfBW9JIUKb5Rf3WI7xCV1u1UW51KzUssqOLWHZd24rPBYKfZdsWuQRDsTGrQ5Vv_WDt1sKjy3FXl7YYSCaryNeRrvxr-SA8AtY6pWI6VVVBmCV8n4Ofg9XyhB21etHbFiX01bWS5Il0BUES8iBFktswr9kgcjvhBe9spWmqA8FYIjenRUiD6mVIFSEfpjPwb5fz2Y1Tb_yQnbmPrHMYpeHaLJAEdyY1D0GRgXXEzHzRa1z_lHFEng0q3mWFvNrTzCXPBp3NKA4ayAQy8OxbBrHBjpc8iVivpM-7y_cJyx9yfXaUP0cU_ApePQcKVTd5d5hXTpmrEGZXVW02vc-CXezMKYZB0DAmXglZRzn30qOZxTnRQm7qmlB5QTCNxpTP1VgUlBzuF2pOaz4POHL-P-9lDKXz0Ld6r1JDvXq1W0oMM6MnREDmBgS58nV2c4C_vzctdsm6yXyL8jbGv75xqqQkqtChLWpiYGu5DnfakGOfrWQ23yWrBIfMXql729o3511tbOt7TZPeaLe9UxvjO_JFNQ1goHrAmQZmclruOMJmgNmuwdrt0bdzjrejAVYmRJOUjyQ5qBKAD1D2k39fNfEY5tUIjKg3DUg7rLTymo4tpdtGQ-Y_V9nlD64BCPmxTc-pzHy345mAFl83-ekekjK8kM99orMIyAjfM-tlV7jSA-_Vo7H4s4PUsmMGx4rZ2MdPUMcGSmjfdpNs34BHSeS8PV_o8KJoaPu5lMaXOGt_sZ7Kr9AD_QEH1lyaD3ZlnbhRx0W7cG_kP9LtYsR_LLAumq6b3MuxWvzjfXpewvg6m0TfWO3jnbneRlGvYnyNkx4iktNb_RCIgazG0mMOelgVD1NrYfhY2i8vfP_o1Ravr_IhjLumeUIW4z701Q-7ia3Fmj5SEsXsawUK7-PyZIwNrL_3C1B6iV5nB1h08bMpXXyRX_NeYdeKqbiTAefGGL4SmKPZqsEM6PjQn5NP0bUBkreqZ_Y_RIa_te7TAZvyN2L83OZfq8IcdEw./download"
        extracted_path = manager.download_and_extract([live_url])
        images_path = os.path.join(extracted_path[0], "live")

        return [
            tfds.core.SplitGenerator(
                name=tfds.Split.TRAIN,
                gen_kwargs={
                    "images_path": images_path,
                    "labels": os.path.join(images_path, "dmos.csv")
                },
            )
        ]

    def _generate_examples(self, images_path, labels):
        with tf.io.gfile.GFile(labels) as f:
            lines = f.readlines()

        for image_id, line in enumerate(lines[1:]):
            values = line.split(",")
            yield image_id, {
                "distortion": values[0],
                "index": values[1],
                "distorted_image": os.path.join(images_path, values[2]),
                "reference_image": os.path.join(images_path, values[3]),
                "dmos": values[4],
                "dmos_realigned": values[5],
                "dmos_realigned_std": values[6],
            }
