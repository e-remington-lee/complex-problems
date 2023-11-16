'''
Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. Only compress the string if it saves space.
'''
from nose.tools import assert_equal
class CompressString:
    def compress(self, s):
        if not s:
            return ""
        response = []
        count = 0
        prev = s[0]
        for x in s:
            if prev == x:
                count += 1
            else:
                if count > 1:
                    response.append(f'{prev}{count}')
                else:
                    response.append(f'{prev}')
                count = 1
                prev = x
        if count > 1:
            response.append(f'{prev}{count}')
        else:
            response.append(f'{prev}')
        return "".join(response)


class TestCompress(object):
    def test_compress(self, func):
        assert_equal(func(''), '')
        assert_equal(func('AABBCC'), 'A2B2C2')
        assert_equal(func('AAABCCDDDDE'), 'A3BC2D4E')
        assert_equal(func('BAAACCDDDD'), 'BA3C2D4')
        assert_equal(func('AAABAACCDDDD'), 'A3BA2C2D4')
        print('Success: test_compress')

def main():
    test = TestCompress()
    compress_string = CompressString()
    test.test_compress(compress_string.compress)

if __name__ == '__main__':
    main()