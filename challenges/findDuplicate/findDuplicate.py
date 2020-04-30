def findDuplicate(self, nums: List[int]) -> int:
    """
        -> Find duplicate number and return it
        - Input _always_ has a duplicate
        - Cannot use extra space - O(1)
        - Cannot use nested loop - Must be less than O(n^2) Quadratic
        - Treat input as read-only
        """

    # This method doesn't follow restrictions, but is a starting point
    # O(n) time | O(n) space
    counts = {}

    for n in nums:
        if counts.get(n):
            counts[n] += 1
        else:
            counts[n] = 1

    for n in counts:
        if counts[n] > 1:
            return n

