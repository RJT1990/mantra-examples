import numpy as np

from mantraml.data.Dataset import Dataset
from mantraml.data.ImageDataset import ImageDataset


class SkateboardDecks(ImageDataset):

    # These class variables contain metadata on the Dataset
    data_name = 'Skateboard Decks'
    data_tags = ['decks']
    files = ['decks.tar.gz']
    has_labels = False
    image_dim = (128, 128) # default - can override with command line