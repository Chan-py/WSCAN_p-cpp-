import networkx as nx

def compute_clustering_coefficient(dat_path):
    # network.dat 불러오기 (가중치 무시)
    # 파일 포맷: "u v w" 형태라고 가정 (node1, node2, weight)
    G = nx.read_weighted_edgelist(dat_path, nodetype=int)

    # 가중치 무시 (단순히 edge만 본다)
    G_unweighted = nx.Graph()
    G_unweighted.add_edges_from(G.edges())

    # 로컬 클러스터링 계수
    local_cc = nx.clustering(G_unweighted)  

    # 글로벌 클러스터링 계수 (평균)
    avg_cc = nx.average_clustering(G_unweighted)

    # Transitivity (삼각형 기반 정의)
    transitivity = nx.transitivity(G_unweighted)

    return local_cc, avg_cc, transitivity


if __name__ == "__main__":
    dat_file = "network.dat"   # 네 dataset 경로
    local_cc, avg_cc, transitivity = compute_clustering_coefficient(dat_file)

    # 결과 출력
    # print("노드별 로컬 클러스터링 계수 (일부):")
    # for node, cc in list(local_cc.items())[:10]:  # 앞 10개만 보기
    #     print(f"Node {node}: {cc:.4f}")

    print("\n평균 클러스터링 계수:", avg_cc)
    print("Transitivity:", transitivity)