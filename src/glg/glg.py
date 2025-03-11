import pygit2
import argparse


class GitRepositoryLogVisualiser:
    def __init__(self, cfg: argparse.Namespace):
        self._repository = pygit2.Repository(".")
        if cfg.all:
            self._references = [self._repository.references.get(reference) for reference in self._repository.references]
        else:
            self._references = [self._repository.head]
        self._last_column_in_use = -1

    def __repr__(self):
        return f"{self.__class__.__name__}(repository={self._repository.path}, references={self._references})"

    def visualise(self):
        for reference in self._references:
            self._visualise_reference(reference)

    def _visualise_reference(self, reference: pygit2.Reference):
        print(f"\x1b[96m{reference.shorthand}\x1b[m")
        for commit in self._repository.walk(reference.resolve().target):
            print(commit)

    def _next_available_column(self) -> int:
        self._last_column_in_use += 1
        return self._last_column_in_use


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="show all commits from refs")
    cfg = parser.parse_args()

    visualiser = GitRepositoryLogVisualiser(cfg)
    visualiser.visualise()

if __name__ == "__main__":
    main()


# repo = Repository("../../../dotfiles")
# for ref in repo.references:
#     ref = repo.references.get(ref)
#     print(ref.shorthand, ref.resolve().target)
# # for commit in repo.walk(repo.head.target):
# for commit in repo.walk(repo.references.get("refs/remotes/origin/git-difftool").target):
#     # print(dir(commit))
#     print(commit.id, commit.parents)
