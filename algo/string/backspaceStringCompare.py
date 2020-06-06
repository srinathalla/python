class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:

        sp = len(S) - 1
        tp = len(T) - 1
        sskip = 0
        tskip = 0

        while sp >= 0 or tp >= 0:

            while sp >= 0:
                if S[sp] == '#':
                    sp -= 1
                    sskip += 1
                elif sskip > 0:
                    sp -= 1
                    sskip -= 1
                else:
                    break
            while tp >= 0:
                if T[tp] == '#':
                    tp -= 1
                    tskip += 1
                elif tskip > 0:
                    tp -= 1
                    tskip -= 1
                else:
                    break

            if sp >= 0 and tp >= 0 and S[sp] != T[tp]:
                return False

            if (sp >= 0) != (tp >= 0):
                return False
            sp -= 1
            tp -= 1

        return True


S = "ab##"
T = "c#d#"
s = Solution()
# print(s.backspaceCompare(S, T))
S = "bbbextm"
T = "bbb#extm"
print(s.backspaceCompare(S, T))
