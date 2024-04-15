import pyvista as pv

for i in range(1, 11):
    file_path = "MEF_beam_bulk_" + str(i) + ".vtu"
    grid = pv.read(file_path)
    plotter = pv.Plotter()
    plotter.add_mesh(grid, show_edges=True)
    plotter.show()
