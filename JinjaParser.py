from jinja2 import Environment, PackageLoader, select_autoescape
import os

# Parameters

# Place the path relative to the folder JinjaParser/templates.
# For example, if the file is at C:\\...\\JinjaParser\\templates\\myfile.txt, place only myfile.txt
template_path = "purchase_data\\FACT_PENDING_TRANSPORT\\HTR_LOAD_FACT_PENDING_TRANSPORT_TENANTS.jsql"


app_name = "JinjaParser"
env = Environment(
    loader=PackageLoader(app_name),
    autoescape=select_autoescape()
)

template = env.get_template(template_path.replace("\\", "/"))
rendered_result = template.render()

result_path = "Target\\" + template_path.replace("jsql", "sql").replace("/", "\\")
os.makedirs(os.path.dirname(result_path), exist_ok=True)
sql_file = open(result_path, "w")
sql_file.write(rendered_result)

print("all gucci")
