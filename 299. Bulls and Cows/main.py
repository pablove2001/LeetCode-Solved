class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sl, gl = list(secret), list(guess) # sl = secretList; gl = guessList
        sd, gd = {}, {} # sd = secret dictionary; gd = guessDictionary
        a = b = 0 # a = number of "bulls"; b = number of "cows"
        sdk = set() # secretDictionaryKeys

        i = 0
        while i < len(sl):
            if sl[i] == gl[i]:
                sl.pop(i)
                gl.pop(i)
                a += 1
            else:
                sd[sl[i]] = sd.get(sl[i], 0) + 1
                gd[gl[i]] = gd.get(gl[i], 0) + 1
                sdk.add(sl[i])
                i += 1
        
        for k in sdk:
            b += min(sd.get(k, 0), gd.get(k, 0))

        return str(a)+'A'+str(b)+'B'