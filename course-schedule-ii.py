class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        remainingPrerequisites = Solution.getInDegree(prerequisites,
                                                      numCourses)
        nextCourses = Solution.getAdjList(prerequisites, numCourses)
        answer = []
        print(nextCourses, remainingPrerequisites)
        while len(answer) < numCourses:
            current = Solution.findNextCourse(remainingPrerequisites)
            if current == -1:
                return []
            answer.append(current)
            remainingPrerequisites[current] = -1
            for nextCourse in nextCourses[current]:
                remainingPrerequisites[nextCourse] -= 1
        return answer

    def findNextCourse(remainingPrerequisites):
        for course, count in enumerate(remainingPrerequisites):
            if count == 0:
                return course
        return -1

    def getInDegree(prerequisites, numCourses):
        prerequisiteCount = [0] * numCourses
        for edge in prerequisites:
            prerequisiteCount[edge[0]] += 1
        return prerequisiteCount

    def getAdjList(prerequisites, numCourses):
        nextCourses = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            nextCourses[edge[1]].append(edge[0])
        return nextCourses
