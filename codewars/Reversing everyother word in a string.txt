6.)Reverse every other word in the string
task:Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly one space 
between each word. Punctuation marks should be treated as if they are apart of the word in this kata.
tests:
Test.describe("Basic tests")
Test.assert_equals(reverse_alternate("Did it work?"), "Did ti work?")
Test.assert_equals(reverse_alternate("I really hope it works this time..."), "I yllaer hope ti works siht time...")
Test.assert_equals(reverse_alternate("Reverse this string, please!"), "Reverse siht string, !esaelp")
Test.assert_equals(reverse_alternate("Have a beer"), "Have a beer")
Test.assert_equals(reverse_alternate(""), "")
My Soln:
def reverse_alternate(string):
    k = string.split()
    new_string = ""
    for i, value  in enumerate (k):
        word = k[i]
        if i % 2 == 1:
            new_string += word[::-1] + " "
        else:
            new_string += word + " "
    return new_string.strip()
others soln:
def reverse_alternate(string):
    return " ".join(y[::-1] if x%2 else y for x,y in enumerate(string.split()))

def reverse_alternate(s):
  words = s.split()
  words[1::2] = [word[::-1] for word in words[1::2]]

def reverse_alternate(string):
    res = []
    arr = string.split()
    for i in arr:
        if arr.index(i) % 2 == 1:
            res.append(arr[arr.index(i)][::-1])
        else:
            res.append(arr[arr.index(i)])
    return " ".join(res)

def reverse_alternate(s):
  return ' '.join(w[::-1] if i % 2 else w for i, w in enumerate(s.split()))

reverse_alternate=lambda s:' '.join(w[::1-n%2*2]for n,w in enumerate(s.split()))

def reverse_alternate(string):
  string = ' '.join(string.split())
  rev = ''
  count = 1
  for i in string.split(' '):
      if count % 2 == 0:
          rev += i[::-1] + ' '
      else:
          rev += i + ' '
      count += 1
  return(rev.rstrip())

def reverse_alternate(string):
    words = string.split(' ')
    
    while words.count('') > 0:
        words.remove('')
    
    for i, w in enumerate(words):
        if i % 2 == 1:
            words[i] = w[::-1]
    
    return ' '.join(words).strip()
  return ' '.join(words)