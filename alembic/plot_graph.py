import importlib
import os
import sys

sys.path.insert(0, "")

# If you want to run this script, quickly run "pip install asciidag"
from asciidag.graph import Graph  # noqa
from asciidag.node import Node  # noqa

folder = os.path.dirname(__file__)
migrations_folder = os.path.join(folder, "versions")
files = os.listdir(migrations_folder)


def main():
    nodes = {}

    for file in files:
        if file == "__init__" or file == "__pycache__":
            continue

        # -3 to remove ".py"
        m = importlib.import_module(f"versions.{file[:-3]}")

        down_revision = getattr(m, "down_revision")
        revision = getattr(m, "revision")

        if revision not in nodes:
            nodes[revision] = {"revision": revision, "down": [], "up": []}

        if type(down_revision) == str:
            down_revision = (down_revision,)

        if down_revision is None:
            down_revision = []

        for rev in down_revision:
            if rev not in nodes:
                nodes[rev] = {"revision": rev, "down": [], "up": []}

            nodes[rev]["up"].append(nodes[revision])
            nodes[revision]["down"].append(nodes[rev])

    graph = Graph()

    def create_node(n):
        if "node" not in n:
            n["node"] = Node(
                n["revision"],
                parents=[create_node(child) for child in n["down"]],
            )

        return n["node"]

    nodes = list(nodes.values())
    for node in nodes:
        create_node(node)

    tips = [n["node"] for n in nodes if len(n["up"]) == 0]

    print("+--- Head(s) ---+")
    graph.show_nodes(tips)
    print("+--- Root ---+")


if __name__ == "__main__":
    main()
