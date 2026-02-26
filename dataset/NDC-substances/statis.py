import networkx as nx
import numpy as np

def analyze_network(file_path, output_path):
    # 그래프 객체 생성 (가중치 그래프)
    G = nx.Graph()
    
    weights = []
    
    try:
        with open(file_path, 'r') as f:
            for line in f:
                if line.strip():  # 빈 줄 제외
                    u, v, w = line.split()
                    w = float(w)
                    G.add_edge(u, v, weight=w)
                    weights.append(w)
        
        # 통계량 계산
        num_nodes = G.number_of_nodes()
        num_edges = G.number_of_edges()
        
        # Degree 계산
        degrees = [d for n, d in G.degree()]
        avg_degree = sum(degrees) / num_nodes if num_nodes > 0 else 0
        max_degree = max(degrees) if degrees else 0
        
        # Weight 계산
        avg_weight = np.mean(weights) if weights else 0
        max_weight = max(weights) if weights else 0
        
        # 결과 파일 작성
        with open(output_path, 'w') as out_f:
            out_f.write(f"{'Metric':<20} | {'Value':<15}\n")
            out_f.write("-" * 40 + "\n")
            out_f.write(f"{'Total Nodes':<20} | {num_nodes:<15}\n")
            out_f.write(f"{'Total Edges':<20} | {num_edges:<15}\n")
            out_f.write(f"{'Average Degree':<20} | {avg_degree:<15.4f}\n")
            out_f.write(f"{'Max Degree':<20} | {max_degree:<15}\n")
            out_f.write(f"{'Average Weight':<20} | {avg_weight:<15.4f}\n")
            out_f.write(f"{'Max Weight':<20} | {max_weight:<15.4f}\n")
            
        print(f"Success: Statistics saved to {output_path}")

    except FileNotFoundError:
        print("Error: The input file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# 실행
analyze_network('network.dat', 'network_stats.txt')