class Solution:
    def findOrder(self, numCourses, prerequisites):
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()
        # if a course is in cycle set it means we're visiting it twice meaning we have detected a cycle
        # In this case, we're gonna return false and terminate our algorithm and return an empty list

        # if a course has already been visited it means we do not need to visit it twice

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    # break algorithm and return False if a course is in cycle
                    # else it means the cours is not in cycle and we will continue to run dfs
                    return False
            # after we complete running dfs on a path, we will remove the cours from cycle
            # as it is no longer along the path that we're going.
            cycle.remove(crs)

            # we add the course to visit
            visit.add(crs)

            # add it to our output
            # note that the prerequisites are added to the output first
            output.append(crs)
            return True

        for c in range(numCourses):
            # it is impossible to take the course if there is a cycle loop
            if dfs(c) == False:
                return []
        return output


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

print(Solution().findOrder(4, prerequisites))
