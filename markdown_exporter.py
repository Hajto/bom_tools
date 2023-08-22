def export_bom(bom, export_line):
    for component, sub_bom in bom.items():
        export_line(f"# {component}")
        export_line("| Item | Quantity |")
        export_line("| - | - |")
        for item, quantity in sub_bom.items():
            export_line(f"| {item} | {quantity} |")
        export_line("\n\n")

def export_bom_to_stdout(bom):
    export_bom(bom, print)

