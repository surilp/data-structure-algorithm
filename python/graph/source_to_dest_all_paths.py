from typing import List, Set, Dict

data = {
    'NY': ['LA', 'CHI', 'SF', 'ATL', 'PA'],
    'CHI': ['NY', 'SF', 'LA', 'PA'],
    'PA': ['NY', 'LA'],
    'SF': ['PA', 'LA', 'CHI'],
    'ATL': [],
    'LA': ['PA']

}


def all_paths(data: Dict[str, str], source: str, destination: str) -> List[List[str]]:
    result = []
    visited = set()
    _dfs(data, source, destination, [], visited, result)
    return result


def _dfs(data: Dict[str, str], source: str, destination: str, ds: List[str], visited: Set[str], result: List[List[str]]):
    ds.append(source)
    visited.add(source)

    if source == destination:
        result.append(list(ds))
        return

    for c_destination in data[source]:
        if c_destination not in visited:
            _dfs(data, c_destination, destination, ds, visited, result)
            ds.pop()
            visited.remove(c_destination)


print(all_paths(data, 'NY', 'LA'))