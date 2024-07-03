

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



# Attributions
https://fonts.google.com/selection

