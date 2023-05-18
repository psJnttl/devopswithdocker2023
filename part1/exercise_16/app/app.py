import os
import random
from flask import Flask

app = Flask(__name__)

doc = """
<html>
  <body>
    <h4>Choose your Lotto flavour</h4>
    And get the numbers for the next round!
    <ul>
      <li><a href='/lottery'>Veikkaus Lotto</></li>
      <li><a href='/vikinglottery'>Viking Lotto</></li>
      <li><a href='/eurolottery'>Euro Jackpot Lotto</></li>
    </ul>
  </body>
</html>
"""

@app.route('/')
def hello():
    return doc

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper+1))
    weekly_draw = random.sample(number_pool, amount)
    weekly_draw.sort()
    return weekly_draw

def get_lotto_numbers(amount: int, start: int, end: int):
    output = ""
    for number in lottery_numbers(amount, start, end):
        output += f'{number}\n'
    return output

@app.route('/lottery')
def lottery():
    return get_lotto_numbers(7, 1, 40)

@app.route('/vikinglottery')
def vikinglottery():
    return get_lotto_numbers(6, 1, 48)

@app.route('/eurolottery')
def eurolottery():
    numbers = get_lotto_numbers(5, 1, 50)
    star_numbers = get_lotto_numbers(2, 1, 12)
    return numbers + " " + star_numbers

if __name__ == '__main__':
    app.run(host='0.0.0.0')
