if __name__ == "__main__":
    T = int(input())

    for _ in range(1, T+1):
        n = int(input())
        matrix = []
        row_count, column_count, diagonal_sum = 0, 0, 0
        for __ in range(n):
            row = list(map(int, input().split()))
            diagonal_sum += row[__]
            matrix.append(row)
            if len(set(row)) != n:
                row_count += 1
        
        for i in range(n):
            column = [matrix[0][i]] + [matrix[j][i] for j in range(1, n)]
            if len(set(column)) != n:
                column_count += 1
        
        print(f"Case #{_}: {diagonal_sum} {row_count} {column_count}")