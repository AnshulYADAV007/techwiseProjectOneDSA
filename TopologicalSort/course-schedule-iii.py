# https://leetcode.com/problems/course-schedule-iii/submissions/836436473/

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        DURATION, LASTDATE = 0, 1
        heap = []
        heapq.heapify(heap)
        courses = sorted(courses, key=lambda x: x[LASTDATE])
        time = 0
        for course in courses:
            heapq.heappush(heap, -course[DURATION])
            time += course[DURATION]
            if time > course[LASTDATE]:
                maxDuration = heapq.heappop(heap)
                time += maxDuration
        return len(heap)
