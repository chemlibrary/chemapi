"""
REQUIREMENTS:
python3 -m pip install fastapi[standard]

USAGE:
uv run fastapi dev
"""

from fastapi import FastAPI
from chempy.rdm import (
    random_number,
    dice,
)
from chempy.secure import (
    generate_pgp_keypair,
    generate_password,
)


app = FastAPI()


@app.get('/')
async def root():
    return {
        'message': 'ChemAPI'
    }


@app.get('/random/wheel/{comma_delimited_choices}')
async def random_wheel(comma_delimited_choices:str):
    if comma_delimited_choices == None or comma_delimited_choices == '':
        choices = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    else:
        choices = comma_delimited_choices.split(',')
    return {
        'message': f'{choices[random_number(max_number = (len(choices) - 1))]}'
    }


@app.get('/random/dice/{rolls}/{dice_type}')
async def roll_dice(rolls:str, dice_type:str):
    if rolls.isnumeric(): rolls = int(rolls)
    else: rolls = 1
    result = dice(rolls=rolls, dice_type=dice_type)
    if len(result) > 1:
        return {'rolls': result}
    else:
        return {'roll': result[0]}    


@app.get('/generate/pgp_keypair')
async def create_pgp_key():
    private_key, public_key = generate_pgp_keypair()
    return {
        'private_key': private_key,
        'public_key': public_key
    }


@app.get('/generate/password/{length}')
async def create_new_password(length:int = None):
    if length == None:
        length = 16
    password = generate_password(length=length)
    return {
        'password': password
    }
