## What ?

Airtable API Implementation for fun and profit.

Wife and I are extensive users of Airtable, it only made sense that I would try to understand its underlying API and use it 
to develop a tool to manage my Airtable's data from my Linux Terminal


## Why ?

I was looking for a project and had just been learning Airtable, which has a simple and solid API


## How ?

You need to generate a Personal Access Token and drop either load it in an environment variable or 
use the script the package airtable.config.utils containing utilities such as load_yaml to load a env.yaml 
file containing the Personal Access Token and other data you might want to add to it, here's an example:

```yaml
---
airtable_api_key: '****************************...'
airtable_base: 'app**************'
airtable_table: 'projects'
```


## Installation

```bash
$ pip install .
```

You're welcome!