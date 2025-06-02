import pandas as pd
import ast
import networkx as nx
import os

# Load initial data
file_path = f'./data/raw_files/test.csv'  # Update this path if needed
df = pd.read_csv(file_path)

# Ensure edgelist is parsed from string to list of tuples
df['edgelist'] = df['edgelist'].apply(ast.literal_eval)

def detect_leakage(row):
    """
    Given a directed edge list (from a rooted tree), check whether it creates
    a tree with directionality and can reveal the root.
    """
    directed_graph = nx.DiGraph()
    directed_graph.add_edges_from(row['edgelist'])

    try:
        # If there's only one node with in-degree 0, it's a strong indicator of leakage
        in_degrees = dict(directed_graph.in_degree())
        roots = [node for node, deg in in_degrees.items() if deg == 0]

        if len(roots) == 1:
            return roots[0]  # Leaked root
        else:
            return None
    except Exception as e:
        print(f"Error processing ID {row['id']}: {e}")
        return None

# Apply leakage detection
df['leaked_root'] = df.apply(detect_leakage, axis=1)

# Summary of leakage
leaked_count = df['leaked_root'].notnull().sum()
total = len(df)
print(f"\n  Leakage Detected in {leaked_count}/{total} samples ({(leaked_count/total)*100:.2f}%)")

# Show a few examples of leaked roots
print("\n Example of Leaked Roots:")
print(df[['id','leaked_root']].dropna().head())

# Optional: Save flagged data
output_path = './data/tests/results.csv'
df = df[['id', 'leaked_root']]
df.to_csv(output_path, index=False)
print(f"\n Results saved to: {output_path}")
