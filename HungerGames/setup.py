import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="AU-HG_v0.0.1",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["headshots"]}},
    executables = executables
    )