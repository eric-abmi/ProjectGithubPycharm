# functions
def count(gdb, fc):
    import arcpy
    from arcpy import management
    arcpy.env.workspace = gdb
    return (int(arcpy.management.GetCount(fc)[0]))
