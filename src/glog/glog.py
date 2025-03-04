from pygit2 import Repository

repo = Repository("../../../dotfiles")
for ref in repo.references:
    ref = repo.references.get(ref)
    print(ref.shorthand, ref.resolve().target)
# for commit in repo.walk(repo.head.target):
for commit in repo.walk(repo.references.get("refs/remotes/origin/git-difftool").target):
    # print(dir(commit))
    print(commit.id, commit.parents)
