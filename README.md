# ColabKit

```
pip install git+https://github.com/johnpaulbin/ColabKit.git
```

Easily importable scripts to be used in your colab runtime.


## Features

### Text

```py
from ColabKit.text.transcript import transcript
textfile = transcript("transcript.txt")
```

- Prefix / Suffix creator

`textfile.psfix(suffix="this is a suffix o/")`
  
- Arpabet converter

`textfile.arpa()`

### Tacotron2

```py
from ColabKit.tacotron2.dataset import dataset
tacoset = dataset("transcript.txt")
```

- Pickle a dataset

`tacoset.pickle(. . .)` (View dataset.py for required parameters)