import os
import networkx as nx
import matplotlib.pyplot as plt


class ArchitectureGraph:

    def generate(self, architecture):

        G = nx.DiGraph()

        root = "CRM APP"

        G.add_node(root)

        G.add_node("PAGES")
        G.add_node("APIS")
        G.add_node("DATABASE")

        G.add_edge(root, "PAGES")
        G.add_edge(root, "APIS")
        G.add_edge(root, "DATABASE")

        for page in architecture.pages:
            G.add_edge("PAGES", page)

        for api in architecture.apis:
            G.add_edge("APIS", api)

        for table in architecture.tables:
            G.add_edge("DATABASE", table)

        pos = {}

        pos[root] = (0, 3)

        pos["PAGES"] = (-4, 1)
        pos["APIS"] = (0, 1)
        pos["DATABASE"] = (4, 1)

        page_y = 0
        for page in architecture.pages:
            pos[page] = (-4, page_y)
            page_y -= 1

        api_y = 0
        for api in architecture.apis:
            pos[api] = (0, api_y)
            api_y -= 1

        db_y = 0
        for table in architecture.tables:
            pos[table] = (4, db_y)
            db_y -= 1

        plt.figure(figsize=(12, 8))

        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=3500,
            font_size=9
        )

        plt.title(
            "Application Architecture"
        )

        os.makedirs(
            "generated_app",
            exist_ok=True
        )

        output_file = os.path.join(
            "generated_app",
            "architecture_graph.png"
        )

        plt.savefig(output_file)

        plt.close()

        return output_file