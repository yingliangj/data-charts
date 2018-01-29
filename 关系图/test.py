from pyecharts import Graph

nodes = [
    {
        'name': 'node 1', 'symbolSize': 10
    },
    {
        'name': 'node 2', 'symbolSize': 20
    },
    {
        'name': 'node 3', 'symbolSize': 30
    },
    {
        'name': 'node 4', 'symbolSize': 40
    },
    {
        'name': 'node 5', 'symbolSize': 50
    },
    {
        'name': 'node 6', 'symbolSize': 40
    },
    {
        'name': 'node 7', 'symbolSize': 30
    },
    {
        'name': 'node 8', 'symbolSize': 20
    }
]

links = []
for i in nodes:
    for j in nodes:
        links.append(
            {
                'source': i.get('name'),
                'target': j.get('name')
            }
        )

graph = Graph('关系图')
graph.add('', nodes, links, is_label_show=True, repulsion=8000, layout='circular', label_text_color=None)
graph.show_config()
graph.render()

