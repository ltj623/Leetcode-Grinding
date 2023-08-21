class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)  # Sort the citations in non-ascending order
        h_index = 0
    
        for i, citation in enumerate(citations, start=1):
            if citation >= i:
                h_index = i  # Update the h-index if condition is met
            else:
                break  # Stop the loop when condition is not met
    
        return h_index
