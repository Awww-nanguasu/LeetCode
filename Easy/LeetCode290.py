class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map = {}
        s = s.split()
        if len(s) != len(pattern):
            return False
        for x in range(len(pattern)):
            if pattern[x] not in hash_map:
                if s[x] in hash_map.values():
                    return False
                hash_map[pattern[x]] = s[x]
            else:
                if hash_map[pattern[x]] != s[x]:
                    return False

        return True 