class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.d = defaultdict(int)
        self.ttl = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.d[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.d[tokenId] != 0 and self.d[tokenId] + self.ttl > currentTime:
            self.d[tokenId] = currentTime
        else:
            self.d.pop(tokenId)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        currentTime -= self.ttl
        res = 0
        d = []
        for k, t in self.d.items():
            if t > currentTime:
                res += 1
            else:
                d.append(k)
        for i in d:
            self.d.pop(i)
        return res
                
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)