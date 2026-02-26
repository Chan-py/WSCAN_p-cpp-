#include "utils.h"
#include <fstream>
#include <stdexcept>
#include <iostream>
#include <iomanip>

std::unordered_map<int, int> LoadGroundTruthLabelDat(
    const std::string& labels_path,
    bool nodes_are_one_based
) {
    std::ifstream fin(labels_path);
    if (!fin) {
        return {};
        // throw std::runtime_error("Failed to open labels file: " + labels_path);
    }

    // map original label string -> compressed int label
    std::unordered_map<std::string, int> label_to_id;
    label_to_id.reserve(1024);

    std::unordered_map<int, int> gt; // node -> int label
    gt.reserve(1024);

    int node_raw;
    std::string label_str;

    while (fin >> node_raw >> label_str) {
        int node = node_raw;
        if (nodes_are_one_based) node -= 1; // convert to 0-based internally

        auto it = label_to_id.find(label_str);
        if (it == label_to_id.end()) {
            int new_id = (int)label_to_id.size();
            it = label_to_id.emplace(label_str, new_id).first;
        }
        gt[node] = it->second;
    }

    return gt;
}

void SaveResultCSV(
    const Args& args,
    double runtime_sec,
    double similarity_time_sec,
    double ari,
    double nmi,
    double modularity,
    double conductance,
    int num_clusters,
    int num_hubs,
    int num_outliers
) {
    // const std::string path = "results.csv";
    const std::string path = args.output_file + ".csv";

    // Check if file exists
    std::ifstream fin(path);
    bool exists = fin.good();
    fin.close();

    // Open file for appending
    std::ofstream fout(path, std::ios::app);
    if (!fout) {
        std::cerr << "Failed to open " << path << "\n";
        return;
    }

    // If file didn't exist, write header
    if (!exists) {
        fout << "dataset,similarity,eps,mu,gamma,edge_p,delta_p,weight_method,is_parallel,num_threads,similarity_time,"
             << "runtime_sec,ARI,NMI,modularity,conductance,num_clusters,num_hubs,num_outliers\n";
    }

    // Write result line
    fout << args.network << ","
         << args.similarity_name << ","
         << args.eps << ","
         << args.mu << ","
         << args.gamma << ","
         << args.edge_p << ","
         << args.delta_p << ","
         << args.weight_method << ","
         << (args.parallel ? "true" : "false") << ","
         << args.threads << ","
         << std::fixed << std::setprecision(6) << similarity_time_sec << ","
         << runtime_sec << ","
         << ari << ","
         << nmi << ","
         << modularity << ","
         << conductance << ","
         << num_clusters << ","
         << num_hubs << ","
         << num_outliers
         << "\n";

    std::cout << "Saved result to results.csv\n";
}