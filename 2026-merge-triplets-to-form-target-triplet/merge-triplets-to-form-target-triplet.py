class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        mergedTriplet = [-float("inf")] * 3

        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                mergedTriplet = [max(mergedTriplet[0], triplet[0]), max(mergedTriplet[1], triplet[1]), max(mergedTriplet[2], triplet[2])]
        
        return mergedTriplet[0] == target[0] and mergedTriplet[1] == target[1] and mergedTriplet[2] == target[2]