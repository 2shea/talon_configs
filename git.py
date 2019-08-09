from talon.voice import Context

context = Context("git")

context.keymap(
    {
        "run get": "git ",
        "run get (R M | remove)": "git rm ",
        "[run] get add": "git add ",
        "run get bisect": "git bisect ",
        "get branch": "git branch ",
        "run get branch": "git branch\n",
        "get checkout": "git checkout ",
        "get checkout master": "git checkout master",
        "run get checkout master": "git checkout master\n",
        "[run] get checkout new": "git checkout -b ",
        "[run] get clone": "git clone ",
        "get commit": "git commit ",
        "run get commit": "git commit\n",
        "get diff": "git diff ",
        "run get diff": "git diff\n",
        "run get diff master": "git diff master\n",
        "get fetch": "git fetch",
        "run get fetch": "git fetch\n",
        "run get grep": "git grep ",
        "run get in it": "git init ",
        "get log": "git log ",
        "run get log": "git log\n",
        "get next release": "git log --oneline --no-decorate --grep 'Merge pull' ",
        "run get merge": "git merge ",
        "run get move": "git mv ",
        "get pull": "git pull ",
        "run get pull": "git pull\n",
        "get push": "git push",
        "run get push": "git push\n",
        "[run] get push origin": "git push origin ",
        "[run] get push master": "git push origin master",
        "run get rebase": "git rebase ",
        "get rebase master": "git rebase master -i",
        "run get rebase master": "git rebase master -i\n",
        "run get reset": "git reset ",
        "run get reset (had | head)": "git reset HEAD^",
        "run get show": "git show ",
        "get status": "git status",
        "run get status": "git status\n",
        "get stash": "git stash ",
        "run get stash": "git stash\n",
        "run get stash pop": "git stash pop",
        "get tag": "git tag ",
        "run get tag": "git tag\n",
        "run get rev parse (had | head)": "git rev-parse HEAD",
        "run get last commit": "git rev-parse HEAD\n",
        "get [remote] add origin": "git remote add origin ",
    }
)
