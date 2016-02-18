# youzan

Youzan SDK for Python

# Installation

```
pip install youzan
```

# Example

```
from youzan import YouZan

youzan = YouZan(APP_ID, APP_SECERT)

print youzan('kdt.regions.get', level=1)
```