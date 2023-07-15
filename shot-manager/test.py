import shotman

# shotman.create_project("project", path="F:/BCIT/repo/bcit-shot-manager/shot-manager/master", current_directory=False)

shotman.set_working_directory("F:/BCIT/repo/bcit-shot-manager/shot-manager/master/project")
shotman.create_show("Castle", "ABC Studios", "Andrew W. Marlowe", 6)

shotman.print_shows_list()