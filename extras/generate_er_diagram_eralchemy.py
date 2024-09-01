# generate_erd.py

from eralchemy2 import render_er

# Specify the input as a Python source file with SQLAlchemy models
input_file = 'sqlite:///sqlmodel_database_relationships.db'
output_file = 'output_diagram.svg'

# Generate the ER diagram
render_er(input_file, output_file)

print(f"ER diagram has been generated and saved as {output_file}")
