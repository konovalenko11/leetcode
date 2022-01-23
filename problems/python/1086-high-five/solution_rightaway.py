import dis
from typing import List

class Solution:
  def highFive(self, items: List[List[int]]) -> List[List[int]]:

    student_scores = {}
    result = []

    for item in items:
      student_id, score = item[0], item[1]

      if not student_id in student_scores:
        student_scores[student_id] = [score]
      else:
        student_scores[student_id].append(score)

    for student_id in sorted(student_scores.keys()):
      top_scores = sorted(student_scores[student_id], reverse= True)[:5]
      avg_scores = sum(top_scores) // len(top_scores)

      result.append([student_id, avg_scores])

    return result

f = Solution()

inputs = [ 
  {
    'items': [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
  },
]

for input in inputs:
  print(f'Input: {input}')
  print(f'Answer: {f.highFive(**input)}')