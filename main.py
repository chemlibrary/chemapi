"""
REQUIREMENTS:
python3 -m pip install fastapi[standard]

USAGE:
uv run fastapi dev
"""

from fastapi import FastAPI
from chempy.rdm import random_number
from chempy.secure import generate_pgp_key


app = FastAPI()


@app.get('/')
async def root():
    return {
        'message': 'ChemAPI'
    }


@app.get('/rdm/wheel/{comma_delimited_choices}')
async def random_wheel(comma_delimited_choices:str):
    if comma_delimited_choices == None or comma_delimited_choices == '':
        choices = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    else:
        choices = comma_delimited_choices.split(',')
    return {
        'message': f'{choices[random_number(max_number = (len(choices) - 1))]}'
    }


@app.get('/pgp/create')
async def create_pgp_key():
    private_key, public_key = generate_pgp_key()
    return {
        'private_key': private_key,
        'public_key': public_key
    }