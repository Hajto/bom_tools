import csv_processor
import markdown_exporter

files = {
    "Gantry": "/Users/hajto/Downloads/Gantry Bom.csv",
    "Counterweight": "/Users/hajto/Downloads/Counterweight.csv",
    "Chains": "/Users/hajto/Downloads/Chains.csv",
    "Extensions Assembly": "/Users/hajto/Downloads/Extensions Assembly.csv",
    "Spool Holder": "/Users/hajto/Downloads/Spool Holder.csv",
    "Panels": "/Users/hajto/Downloads/Panels bom.csv",
    "Bed motion asembly": "/Users/hajto/Downloads/Y axis assembly bom.csv",
    "Ender 3 Pro Frame": "/Users/hajto/Downloads/Ender 3 Pro bom.csv",
}
bom = csv_processor.summarize(files)
markdown_exporter.export_bom_to_stdout(bom)