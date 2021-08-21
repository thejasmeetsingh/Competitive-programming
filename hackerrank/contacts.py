from collections import defaultdict


def contacts(queries):
    contacts_dd = defaultdict(list)
    results = []

    for query in queries:
        if query[0] == 'add':
            for idx in range(1, len(query[1])+1):
                contacts_dd[query[1][:idx]].append(query[1])
        else:
            results.append(str(len(contacts_dd.get(query[1], []))))

    return results


if __name__ == '__main__':
    queries_rows = int(input().strip())
    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    print('\n'.join(result))
