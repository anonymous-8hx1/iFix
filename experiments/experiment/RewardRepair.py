import json
import javalang
import copy
from utils.ranking import *

def get_parsed_code(code):
    tokens = javalang.tokenizer.tokenize(code)
    try:
        parsed_code = list(tokens)
        return parsed_code
    except TypeError:
        print(code)
        return []

def rr_get_patch_list(bug_id, parsed=True):
    f = open(f'./RewardRepairPatches/plausible-{bug_id}.json', 'r')
    patch_data = json.load(f)
    plausible_patches = []
    for patch in patch_data:
        if patch["correctness"] == 'plausible':
            if parsed: 
                parsed_patch = get_parsed_code(patch["patch"])
                plausible_patches.append({
                    'code': patch["patch"],
                    'parsed_token': parsed_patch,
                })
            else:
                plausible_patches.append({
                    'code': patch["patch"]
                })
    return plausible_patches

def rr_get_buggy_line(buggy_line, parsed=True):
    if parsed:
        parsed_buggy_line = get_parsed_code(buggy_line)
        return {
            'code': buggy_line,
            'parsed_token': parsed_buggy_line
        }
    else:
        return {
            'code': buggy_line
        }

def rr_output_ranked_patch(bug_id, ranked_patch, prompt, format='normal'):
    with open(f'./result/RewardRepair/{bug_id}/{prompt}_rank.java', 'w') as f:
        if format == 'normal':
            for patch in ranked_patch:
                f.write(f"{patch['code']}\n")
        elif format == 's3_kv':
            for key, value in ranked_patch.items():
                f.write(f"{value}: {key}\n")

def rr_simple_ranking_result(bug_id, buggy_line):
    # parsed_buggy_line = list(javalang.tokenizer.tokenize(buggy_line))
    plausible_patches = rr_get_patch_list(bug_id)
    parsed_buggy_line = rr_get_buggy_line(buggy_line)
    tmp_patch = copy.deepcopy(plausible_patches)
    for patch in tmp_patch:
        patch['rk_score'] = levenshtein_distance(patch['parsed_token'], parsed_buggy_line['parsed_token'])
    tmp_patch.sort(key=lambda x: x['rk_score'])
    rr_output_ranked_patch(bug_id, tmp_patch, 'SIMPLE_RANK')
    return tmp_patch

def RewardRepair_ranking_result(bug_id):
    plausible_patches = rr_get_patch_list(bug_id, False)
    rr_output_ranked_patch(bug_id, plausible_patches, 'RewardRepair')

def RewardRepair_test():
    with open('./data/RR_bug_info.json', 'r') as f:
        bug_info = json.load(f)
        for bi in bug_info:
            RewardRepair_ranking_result(bi['BUG_ID'])
            rr_simple_ranking_result(bi['BUG_ID'], bi['BUGGY_LINE'])