//Container With Most Water

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1  # Corrected this line from right += 1 to right -= 1
        
        return max_area
