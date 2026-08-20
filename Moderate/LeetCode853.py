class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        position = sorted(enumerate(position), key=lambda x:x[1])
        times = []

        for id, pos in position:
            times.append((target - pos)/speed[id])

        st = []
        for i in range(n):
            while st and times[st[-1]] <= times[i]:
                st.pop()
            st.append(i)

        return len(st)