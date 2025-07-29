import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
dfd = nx.DiGraph()

# Add nodes (processes, entities, and data stores)
dfd.add_node("User", pos=(0, 1), shape='s', color='lightblue')  # External entity
dfd.add_node("Voice Assistant", pos=(1, 1), shape='o', color='orange')  # Process
dfd.add_node("Database", pos=(2, 1), shape='s', color='lightgreen')  # Data store

# Add edges (data flow between nodes)
dfd.add_edge("User", "Voice Assistant", label="Voice Input")
dfd.add_edge("Voice Assistant", "User", label="Voice Response")
dfd.add_edge("Voice Assistant", "Database", label="Query/Store")
dfd.add_edge("Database", "Voice Assistant", label="Data/Response")

# Extract node positions
pos = nx.get_node_attributes(dfd, 'pos')

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(dfd, pos, with_labels=True, node_size=3000, node_color=['lightblue', 'orange', 'lightgreen'], font_size=10, font_weight='bold', arrows=True)

# Add edge labels (data flow labels)
edge_labels = {('User', 'Voice Assistant'): 'Voice Input', ('Voice Assistant', 'User'): 'Voice Response',
               ('Voice Assistant', 'Database'): 'Query/Store', ('Database', 'Voice Assistant'): 'Data/Response'}
nx.draw_networkx_edge_labels(dfd, pos, edge_labels=edge_labels)

plt.title("Level 1 DFD for Voice Assistant")
plt.show()