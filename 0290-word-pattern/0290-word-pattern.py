class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
      words = s.split(" ")
      print(words)
      if len(words) != len(pattern): return False

      c_to_w = {}
      w_to_c = {}
      for char, word in zip(pattern, words):
        if char in c_to_w:
          if c_to_w[char]!= word : return False
        else:
          c_to_w[char] = word
        if word in w_to_c:
          if w_to_c[word] != char: return False
        else:
          w_to_c[word] = char
      return True      