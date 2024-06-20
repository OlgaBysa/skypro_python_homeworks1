import pytest
from string_utils import StringUtils

utils = StringUtils()

#    ***capitalize***

def test_capitalize():
         #  ***positive***
   assert utils.capitilize("мама") =="Мама"
   assert utils.capitilize("доброе утро") =="Доброе утро"
   assert utils.capitilize("567") =="567"
        #  ***negative***
   assert utils.capitilize("") ==""
   assert utils.capitilize(" ") ==" "
   
         
    #  ***trim***

def test_trim():
##    ***positive***
   assert utils.trim(" mom") =="mom"
   assert utils.trim(" доброе утро") =="Доброе утро "
   assert utils.trim(" SKY ") =="SKY "
    #  ***negative***
   assert utils.trim("") == ""
@pytest.mark.xfail()
def tes_trim_with_spaces_output():
   assert utils.trim(" SKY ") == " SKY "

@pytest.mark.xfail()
def test_trim_with_numbers_input():
   assert utils.trim(" SKY ") =="SKY "


#    ***to_list***
@pytest.mark.parametrize('string, delimeter, result', [
    # POSITIVE
    ("яблоко,банан,апельсин", ",", ["яблоко", "банан", "апельсин"]),
    ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
    ("*@$@%@&", "@", ["*", "$", "%", "&"]),
    # NEGATIVE
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3", "4 5"]),
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
       res = utils.to_list(string)
    else:
       res = utils.to_list(string, delimeter)
    assert res == result


   # ***contains***
@pytest.mark.parametrize('string, symbol, result',[
         #  positive
   ("клубника", "к", True),
   (" вишня", "я", True),
   ("слива ", "о", True),
   ("стол-книжка", "-",True),
   ("567", "5", True),
   ("", "", True),
         #  negative 
   ("Мама", "м", False),
   ("мама", "о", False),
   ("мир", "?", False),
   ("", "и", False),
])
@pytest.mark.xfail()
def test_contains(string, symbol, result):
   res = utils.contains(string, symbol)
   assert res == result, f"Expected: {result}, Got: {res} for string '{string}' and symbol '{symbol}'"


      # ***delete_symbol***
@pytest.mark.parametrize('string, symbol, result',[
         #  positive
   ("клубника", "б", "лубника"),
   ("Вишня", "В", "ишня"),
   ("Слива ", "С", "лива"),
   ("Доброу Утро", "", "ДоброеУтро"),
         #  negative 
   ("Мама", "о", "мама"),
   ("мама", "", "мама"),
   ("", "?", ""),
   ("", "", ""),
])
@pytest.mark.xfail()
def test_delete_symbol(string, symbol, result):
    res = utils.delete_symbol(string, symbol)
    assert res == result


      # ***starts_with***
@pytest.mark.parametrize('string, symbol, result',[
         #  positive
   ("клубника", "к", True),
   ("", "", True),
   ("Слива ", "С", True),
   ("567", "5", True),
 
         #  negative 
   ("Мама", "м", False),
   ("Ваня", "в", False),
   ("", "?", False),
   ])
@pytest.mark.xfail()
def test_starts_with(string, symbol, result):
    res = utils.starts_with(string, symbol)
    assert res == result

   
      # ***end_with***
@pytest.mark.parametrize('string, symbol, result',[
         #  positive
   ("клубника", "к", True),
   ("ВИШНЯ", "Я", True),
   ("", "", True),
   ("книга", "",True),
   ("567", "5", True),
 
        #  negative 
   ("мама", "н", False),
   ("книга", "о", False),
   ("мир", "Р", False),
   ("", "*", False),
])
@pytest.mark.xfail()
def test_end_with(string, symbol, result):
    res = utils.end_with(string, symbol)
    assert res == result

      # ***is_empty***

@pytest.mark.parametrize('string, result',[
         #  positive
   ("", True),
   (" ",  True),
   ("   ", True),
         #  negative 
   ("доброе утро", False),
   ("567", False)
])
@pytest.mark.xfail()
def test_is_empty(string, result):
    res = utils.contains(string)
    assert res == result


      # ***list_to_string***

@pytest.mark.parametrize('lst, joiner, result',[
         #  positive
   (["w", "o", "k"], "," , "w,o,k"),
   ([5, 6, 7], None, "5,6,7"),
   (["стол", "книжка"], "-","стол-книжка"),
         #  negative 
   ([], None, ""),
   ([], ",", ""),
   ([], "мир", "")
])
@pytest.mark.xfail()
def test_list_to_string(lst, joiner, result):
    if joiner == None:
        res = utils.list_to_string(lst)
    else:
        res = utils.list_to_string(lst, joiner)
    assert res == result
