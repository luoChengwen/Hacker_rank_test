class Solution:
    def intervalIntersection(self, A, B): # AB are lists

        output = []
        ai,bi = 0, 0

        while ai < len(A) and bi < len(B):
            start_A, end_A = A[ai]
            start_B, end_B = B[bi]

            start = max(start_A, start_B)
            end = min(end_A, end_B)

            if start <= end: output.append([start, end])

            if end_A < end_B: ai+=1
            else: bi+=1

        return output

    #
A = [[8, 15]]
B = [[2, 6], [8, 10], [12, 20]]

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]