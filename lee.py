from graphviz import Digraph

dot = Digraph(comment='Test Graph')
dot.node('A', 'Hello')
dot.node('B', 'World')
dot.edge('A', 'B')
print(dot.source)
dot.render('test-output/test.gv', view=True)