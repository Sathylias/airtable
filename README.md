## What ?

Airtable API Implementation for fun and profit.

Wife and I are extensive users of Airtable, it only made sense that I would try to understand its underlying API and use it 
to develop a tool to manage my Airtable's data from my Linux Terminal

## Why ?

I was looking for a project and had just been learning Airtable, which has a simple and solid API

## How ?

You need to generate a Personal Access Token and drop either load it in an environment variable or 
use the script config/config.py to load a env.yaml file containing the Personal Access Token and other data
you might want to add to it, here's an example:

```yaml
---
airtable_api_key: '****************************...'
airtable_base: 'app**************'
airtable_table: 'projects'
```

- To run the examples, simple use the following from the root directory
```bash
$ python3 -m examples.example
```

## Installation

```bash
$ ./setup.py
```

```bash
$ echo "You're welcome" > /dev/null
```