def container_with_most_water(height):
    max_area = float('-inf')
    left = 0
    right = len(height) - 1
    while left <= right:
        h_left = height[left]
        h_right = height[right]

        min_height = min(height[left], height[right])
        area = (right - left) * min_height
        max_area = max(area, max_area)

        if h_left <= h_right:
            while left <= right and height[left] <= h_left:
                left += 1
        else:
            while left <= right and height[right] <= h_right:
                right -= 1
    return max_area

print(container_with_most_water([1, 1,1,1,1,1,]))
