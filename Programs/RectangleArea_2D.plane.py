# Area of a Rectangle in 2D Plane

def computeArea(ax1: int, ay1: int, ax2: int, ay2: int,
                    bx1: int, by1: int, bx2: int, by2: int) -> int:

        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        overlap_width = min(ax2, bx2) - max(ax1, bx1)
        overlap_height = min(ay2, by2) - max(ay1, by1)

        overlap = 0

        if overlap_width > 0 and overlap_height > 0:
            overlap = overlap_width * overlap_height

        return area1 + area2 - overlap
# 2 rectangles are defined by their bottom-left and top-right corners: (ax1, ay1), (ax2, ay2) for the first rectangle and (bx1, by1), (bx2, by2) for the second rectangle. The function calculates the area of each rectangle, determines the overlap area if they intersect, and then returns the total area covered by both rectangles without double-counting the overlapping region.
ax1, ay1, ax2, ay2 = map(int, input("Enter the coordinates of the first rectangle (ax1, ay1, ax2, ay2): ").split())
bx1, by1, bx2, by2 = map(int, input("Enter the coordinates of the second rectangle (bx1, by1, bx2, by2): ").split())
area = computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
print(f"The total area covered by the two rectangles is: {area}")
