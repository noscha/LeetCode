class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ''' Simulate process '''
        change = True
        while change:
            change = False
            for i in students:
                if i == sandwiches[0]:
                    students.remove(i)
                    sandwiches.pop(0)
                    change = True
        return len(students)
