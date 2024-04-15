import pyvista as pv


file_path = "MEF_beam_bulk_10.vtu"
grid = pv.read(file_path)
plotter = pv.Plotter()
plotter.add_mesh(grid, show_edges=True)
plotter.show()
