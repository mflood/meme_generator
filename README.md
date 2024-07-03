

TODO: the README should include an overview of the project
TODO: the README should include sinstructions for  setting up and running the program
TODO: t=he README should include a brief description of the roles and respobsibilities 
of all sub-modules including dependencies  and examples of how to use the model


## Setup

> Setup the virtual environment

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

> fyi - to stop using this virtual env

```
deactivate
```

> Install xpdf for Mac
```
brew install xpdf
```

> run the Web app
```
python app.py
```

> open a webbrowser to view the web app
```
open http://127.0.0.1:5000
```



## Sub-Modules

### Quote Engine module

The Quote Engine sub-module defines the QuoteModel and Ingestor 
which provides the ability to parse QuoteModel data from 
various file types including .csv, .pdf, .docx and .txt

> Dependencies

- xpdf (cli tool)
- python-docx (python library)

> Usage:

```
from typing import List
from quote_engine.ingestor import Ingestor
from quote_engine.models import QuoteModel

input_filepath = "_data/SimpleLines/SimpleLines.csv"
if Ingestor.can_ingest(input_filepath):
    quote_list: List[QuoteModel] = Ingestor.parse(input_filepath)

for quote in quote_list:
    print(quote)
```

### Meme Generator module

The Meme Generator sub-module defines the MemeEngine, which
takes an image and a qoute and creates a new image, resized, with
the quote text overlaid.

> Dependencies

- PIL

> Usage:

```
from meme_generator.meme_engine import MemeEngine

meme_engine = MemeEngine.make_default_engine(output_directory="./static")

meme_output_path = meme_engine.make_meme(
    img_path="_data/photos/landscape/landscape_2.jpeg",
    text="Waste no more time arguing about what a good man should be. Be one.",
    author="Marcus Aurelius"
)

print(f"meme image generated at {meme_output_path}")

```


# Attributions
https://fonts.google.com/selection

