import vtk
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Ruta al archivo VTU
file_path = "MEF_beam_bulk_10.vtu"


# Crear un lector para el archivo VTU
reader = vtk.vtkXMLUnstructuredGridReader()
reader.SetFileName(file_path)
reader.Update()

# Crear un mapper y un actor para visualizar la malla
mapper = vtk.vtkDataSetMapper()
mapper.SetInputConnection(reader.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Crear un renderizador, una ventana y un interactor
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Configurar y empezar la interacción
interactor.Initialize()
interactor.Start()