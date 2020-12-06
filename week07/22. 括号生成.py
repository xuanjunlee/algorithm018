class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = list()

        def back_tracking(left, right, path, count):
            if count == n * 2:
                ans.append(path)
                return

            if left < n:
                back_tracking(left + 1, right, path + '(', count + 1)

            if right < left:
                back_tracking(left, right + 1, path + ')', count + 1)

        back_tracking(0, 0, '', 0)
        return ans

