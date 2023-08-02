import os


PROJECT_HOME = "/Users/ruixinwang/d4j/d4j_bugs/"

project = "Chart"
id = 9

project_path = f'{PROJECT_HOME}{project}/{project}_{id}_buggy'
Cure_patches = f'./new_result/{project}_{id}/cure_rank.log'

with open(Cure_patches, 'r') as f_patches:
    for idx, patch in enumerate(f_patches.readlines()):
        with open(f'concrete_patches/{project}_{id}/0-correct-patch', 'r') as f_sample:
            lines = f_sample.readlines()
            for i, line in enumerate(lines):
                if line.startswith("+  "):
                    lines[i] = f'+{" " * (len(line[1:]) - len(line[1:].lstrip(" ")))}{patch}'
                    break

            with open(f'concrete_patches/{project}_{id}/cure-patch{idx+1}', 'w') as f_target:
                f_target.writelines(lines)