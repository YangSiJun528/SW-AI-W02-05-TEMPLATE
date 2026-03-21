"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    # 구현 참고한 코드: https://youtu.be/xeSz3pROPS8?si=XuSG5KmUeW-IdBzB

    indegree = {v:0 for v in range(vertices)} # dict가 value 간의 폭이 넓은 경우에도 유리하므로
    graph = {v:[] for v in range(vertices)} # dict가 value 간의 폭이 넓은 경우에도 유리하므로
    for u, v in edges:
        graph[u].append(v) # 단방향이라 이거만
        indegree[v] += 1

    #print(indegree)
    #print(graph)

    result = []

    # 진입 차수가 0인 정점들을 큐에 삽입 (시작 가능한 노드)
    queue = deque(i for i in indegree if indegree[i] == 0)

    while queue:
        v = queue.popleft()
        result.append(v)  # 현재 정점 처리

        # 현재 정점에서 나가는 간선 제거 - 단방향이라 visited 처리 필요없음
        for u in graph[v]:
            indegree[u] -= 1  # v 제거 → u의 진입 차수 감소
            if indegree[u] == 0: # 더 이상 들어오는 진입 차수가 없으면 큐에 넣기
                queue.append(u)

    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
