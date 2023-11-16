from utilities import to_string


class Solution:
    def restoreIpAddresses(self, s):
        self.response = []
        self.s = s
        self.back_track(0, [])
        return self.response

    def back_track(self, start, cur):
        if len(cur) == 4:
            if start == len(self.s):
                self.response.append(".".join(cur))
            return

        for i in range(start, min(start + 3, len(self.s))):
            # this is for the 0.0.0.0 cases where we have 0s, but we don't want 02.01, checked by i > start
            if self.s[start] == "0" and i > start:
                break
            if int(self.s[start: i + 1]) <= 255:
                # cur.append(self.s[start: i + 1])
                # self.back_track(i + 1, cur)
                # cur.pop()
                # if you do backtracking on lists, you list + list(item) which concatenates them. It acts as making a new variable
                self.back_track(i + 1, cur + [self.s[start:i + 1]])


flashcard = to_string.file_to_string(__file__)
print(flashcard)
