# `funcapsolver` 

funcapsolver is a funcaptcha audio-solving module, which allows captchas to be interacted with and solved with the use of google's speech-recognition api.

## Table of Contents

* [Examples](#Examples)
* [Getting started](#getting-started)
* [Documentation](#documentation)

## Installation

To pip install `funcapsolver` from github:

```bash
pip install git+https://github.com/AcierP/rpi.git
```

## Examples

### Obtaining an unsolved captcha token
```python
token = funcapsolver.get_token(host='api.funcaptcha.com', pkey='69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC')
```

### Solving a captcha and returning the captcha response
```python
token = funcapsolver.get_token('api.funcaptcha.com', '69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC')
solved = funcapsolver.solveCaptcha(token)
print(solved)
```
