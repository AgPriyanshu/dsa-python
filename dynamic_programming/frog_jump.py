# Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair.
# At a time the frog can climb either one or two steps. A height[N] array is also given. Whenever the frog jumps
# from a stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), where abs() means the
# absolute difference. We need to return the minimum energy that can be used by the frog to jump from stair 0 to
# stair N-1.
def frog_jump(n, heights, energy):
    if n <= 1:
        return energy
    else:
        cal_energy = abs(heights[n] - heights[n - 1])
        return min(
            frog_jump(
                n - 1,
                heights,
                energy + cal_energy,
            ),
            frog_jump(
                n - 2,
                heights,
                energy + cal_energy,
            ),
        )


if __name__ == "__main__":
    print(frog_jump(4 - 1, [10, 20, 30, 10], 0))
