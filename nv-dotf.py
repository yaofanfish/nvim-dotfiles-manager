#!/usr/bin/env python3

import sys, os, subprocess
import argparse, json
class mdict(dict):
    pass
try:
    import rich
except:
    rich = mdict()
    rich.print_json = lambda x: json.dumps(x, indent="\t")

HOME=os.getenv("NV_DOTF_HOME", os.getenv("HOME", "/tmp"))
p = argparse.ArgumentParser("nvim dotfiles")
p.add_argument("name", nargs="?", default="--removeonly", help="the name of the nvim dotfile")
p.add_argument("-y", "--noconfirm", help="don't confirm", action="store_true")
p.add_argument("-c", "--configfile", default=f"{HOME}/.config/nvim-dotf/dirs.json", help="configfile")
p.add_argument("-r:n", "--noremovefile", action="store_true", help="don't remove any previously existing item (*uses -r*)")
p.add_argument("-r:f", "--force", action="store_true", help="use -f on the rm command")

p.add_argument("--removeonly", action="store_true")
#p.add_
args = p.parse_args()
if args.name == "--removeonly" and not args.removeonly:
    p.print_help()
    sys.exit(2)

dirs = {
        f"{HOME}/.config": "nvim", # "nvim" is the dir being replaced
        f"{HOME}/.local/share": "nvim",
        f"{HOME}/.local/state": "nvim",
        f"{HOME}/.cache": "nvim",
        }
try:
    with open(args.configfile) as f:
        dirs = json.load(f)
except:
    print("Using default config:")
    rich.print_json(data=dirs)
    print(f"add dirs.json in ~/.config/nvim-dotf/dirs.json for an actual configuration. alternately, edit your python source code to remove this annoying message.")

if input(f"\033[36mAre you sure you want to replace your dotfiles with {args.name}? \033[0m").lower() == "n":
    print("\033[32mExiting without doing anything\033[0m")
    sys.exit(2)

for d in dirs.keys():
    if not args.noremovefile:
        subprocess.run(["rm", "-r", "-f" if args.force else "-i", f"{d}/{dirs[d]}"])
    if not args.removeonly:
        subprocess.run(["ln", "-sfn", f"{d}/{args.name}", f"{d}/{dirs[d]}"])


