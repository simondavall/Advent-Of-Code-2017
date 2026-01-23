import sys
import time
import re

title = "## Day 7: Recursive Circus ##"
url = "https://adventofcode.com/2017/day/7"
expectedResultPart1 = "mwzaxaj"
expectedResultPart2 = 1219

class TreeNode:
    def __init__(self, name, weight):
        self.name = name
        self.weight = int(weight)
        self.children = []
        self.child_weight = 0

    def state(self):
        return (self.name, self.weight, self.child_weight, self.children)

def build_tree(nodes_data):
    # Create all nodes
    nodes = {name: TreeNode(name, weight) for name, weight, _ in nodes_data}

    # Build children and track parents
    has_parent = {name: False for name in nodes}
    for name, _, children in nodes_data:
        for child in children:
            nodes[name].children.append(nodes[child])
            has_parent[child] = True

    # Find root (node with no parent)
    root_name = next(name for name, parent_status in has_parent.items() if not parent_status)
    return nodes[root_name]

def sum_child_weights(node):
    if (len(node.children) == 0):
        return node.weight

    weight = node.weight
    for child in node.children:
        weight += sum_child_weights(child)

    return weight

def find_unique_weight_node(nodes):
    weight_map = {}
    for node in nodes:
        weight_map.setdefault(node.child_weight, []).append(node)
    
    unique_node = None
    common_weight = None
    for weight, node_list in weight_map.items():
        if len(node_list) == 1:
            unique_node = node_list[0]
        else:
            common_weight = weight
    if unique_node and common_weight is not None:
        weight_diff = abs(unique_node.child_weight - common_weight)
        return unique_node, weight_diff
    return unique_node, 0

def process_input(input):
    nodes = []
    for match in re.finditer(r'^(\w+)\s\((\d+)\)(?:\s->\s)?(.+)?$', input, re.MULTILINE):
        children = []
        if match.group(3) != None:
            children = match.group(3).split(", ")
        nodes.append((match.group(1), match.group(2), children))
    return nodes

def partOne(input):
    nodes = process_input(input)
    root = build_tree(nodes)
    return root.name

def partTwo(input):
    nodes = process_input(input)
    root = build_tree(nodes)
    curr = root
    current_imbalance = 0
    diff = -1
    while True:
        for child in curr.children:
            child.child_weight = sum_child_weights(child)

        unbalanced_child, diff = find_unique_weight_node(curr.children)
        if diff == 0:
            return curr.weight - current_imbalance
        current_imbalance = diff
        curr = unbalanced_child

print(title)
print(url)
for filePath in sys.argv[1:]:
    print(f"\nFile: {filePath}")
    with open(filePath, 'r') as file:
        input = file.read()

    start = time.perf_counter()
    resultPartOne = partOne(input);
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Part 1 Result: {resultPartOne} in {elapsed_ms:.3f}ms");

    start = time.perf_counter()
    resultPartTwo = partTwo(input);
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Part 2 Result: {resultPartTwo} in {elapsed_ms:.3f}ms");

if (resultPartOne != expectedResultPart1 or resultPartTwo != expectedResultPart2):
        sys.exit(1)
