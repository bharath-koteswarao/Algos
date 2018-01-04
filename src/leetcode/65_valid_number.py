class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if s.isnumeric():
            # print("Yes")
            return True
        else:
            l = list(s)
            ret = True
            dot, e, m, p = 0, 0, 0, 0
            for i in l:
                if i == '.':
                    dot += 1
                    if dot > 1:
                        ret = False
                elif i == 'e':
                    e += 1
                    if e > 1:
                        ret = False
                    if l.index('e') == 0 or l[-1] == 'e':
                        ret = False
                    elif l[0] == '.' and l[1] == 'e':
                        ret = False
                    elif len(l) > 0 and l[-1] == '.' and l[-2] == 'e':
                        ret = False
                    if l.index('e') == 1 and l[0] == '0' and len(l) == 2:
                        ret = False
                elif i == '-':
                    m += 1
                    if m > 1:
                        ret = False
                    if l.index('-') != 0:
                        if 'e' in l and l.index('-') == l.index('e') + 1:
                            ret = True
                        else:
                            ret = False
                    if len(l) > 1 and l[1] == 'e':
                        ret = False
                    if l[-1] == '-':
                        ret = False
                elif i == '+':
                    p += 1
                    if p > 1:
                        ret = False
                    if l.index('+') != 0:
                        if 'e' in l and l.index('+') == l.index('e') + 1:
                            ret = True
                        else:
                            ret = False
                    if len(l) == 1 and l[1] == 'e':
                        ret = False
                    if l[-1] == '+':
                        ret = False
                elif not i.isnumeric():
                    ret = False
                if not ret:
                    break
            # print(ret)
            if len(l) == dot or len(l) == p or len(l) == m or len(l) == e:
                ret = False
            if len(list(filter(lambda a: (a != '.' and a != 'e' and a != '+' and a != '-'), l))) == 0:
                ret = False
            if e > 0 and dot > 0:
                ret = ret and l.index('e') > l.index('.')
            if p > 0 and m > 0:
                if 'e' in l:
                    if l.index('+') <= l.index('e') <= l.index('-') or l.index('-') <= l.index('e') <= l.index('+'):
                        ret = ret and True
                    else:
                        ret = False
                else:
                    ret = False
            print(ret)
            return ret and len(l) != 1 and len(l) > 0


Solution().isNumber(input())
