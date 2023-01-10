import time

import uvicorn

from git import Repo, RemoteProgress
from git import InvalidGitRepositoryError, NoSuchPathError

from constants import IPTV_REPOSITORY_URL, IPTV_REPOSITORY_PATH


class CloneProgress(RemoteProgress):
    def update(self, op_code, cur_count, max_count=None, message=""):
        print(f"\r{int(cur_count)}/{int(max_count)}: {message}", end="")


if (__name__ == "__main__"):
    # Check if the repository exists if not fetch it
    print(f"[Warning]: Fetching iptv-org repository at {IPTV_REPOSITORY_PATH}")

    try:
        repo = Repo(IPTV_REPOSITORY_PATH)
    except (InvalidGitRepositoryError, NoSuchPathError):
        repo = Repo.clone_from(
            url=IPTV_REPOSITORY_URL,
            to_path=IPTV_REPOSITORY_PATH,
            progress=CloneProgress(),
            branch="master"
        )

    # Check updates
    repo.remotes.origin.pull()

    # Get the date and the last commit
    head = repo.head
    last_commit = head.commit
    print(f"Branch: {head.reference}")
    print(f"Last Commit: {last_commit}")
    print(f"{last_commit.message}")
    last_commit_date = time.gmtime(last_commit.committed_date)
    last_commit_date = time.strftime('%Y-%m-%d %H:%M:%S', last_commit_date)
    print(last_commit_date)

    #  Running the GraphQL server
    print("[Warning]: running the server with uvicorn")
    uvicorn.run("api:app")
